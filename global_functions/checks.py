import time

import cv2
from matplotlib.pyplot import imshow

from global_functions.api_reader import get_eve_module_quantity
import matplotlib.pyplot as plt
import numpy as np
from config import TARGETS_REGION, GLOBAL_ASSETS
from modules.find_image import make_screenshot, find_image, get_green_pixel_ratio
import datetime
from PIL import Image, ImageDraw
from global_functions.get_pid import get_pid

def check_guns_old():
    pid = get_pid()
    count = get_eve_module_quantity(pid)
    time.sleep(3)
    if get_eve_module_quantity(pid) < count:
        return True
    else:
        time.sleep(2)
        if get_eve_module_quantity(pid) >= count:
            return False

def check_guns():
    _c = find_image(GLOBAL_ASSETS + "ungroup.png", acc=0.9)
    x1, y1, x2, y2 = _c
    ratios = []
    for i in range(5):
        scr = make_screenshot(region=(int(x1) + 22, int(y1) - 4, 66, 66))
        ratios.append(get_green_pixel_ratio(scr))
        time.sleep(0.2)
    if (max(ratios) + 0.0001)/(min(ratios) + 0.0001) >= 2:
        return True
    else:
        return False





def count_targets(current_count = 0):

    image_path = make_screenshot(TARGETS_REGION)

    rectangles = split_image_into_vertical_rectangles(
        image_path,
        output_path="split_visualization.png",
        rectangle_width=106,
        gap_width=32,
        visualize=False
    )

    count = count_rectangles_with_nonblack_pixels(
        image_path,
        rectangles,
        threshold=30,
        visualize=False,
        #output_path="targets_detection/",
        sample_rate=8  # берем каждый 8-oй пиксель для ускорения
    )
    if count != current_count: # если число целей изменилось, то проверяем еще раз чтобы не триггерить на анимацию
        time.sleep(1)
        print("double check")
        count = count_rectangles_with_nonblack_pixels(
        image_path,
        rectangles,
        threshold=30,
        visualize=False,
        output_path="targets_detection/",
        sample_rate=8  # берем каждый 8-oй пиксель для ускорения
    )
    return count


def split_image_into_vertical_rectangles(image_path, output_path=None, rectangle_width=106, gap_width=32,
                                         visualize=False):
    """
    Разделяет изображение на вертикальные прямоугольники.

    Параметры:
    image_path (str): Путь к исходному изображению
    output_path (str, optional): Путь для сохранения визуализации, если None - только отображение
    rectangle_width (int): Ширина каждого прямоугольника в пикселях
    gap_width (int): Расстояние между прямоугольниками в пикселях
    visualize (bool): Флаг для визуализации разделения

    Возвращает:
    list: Список координат прямоугольников в формате [(x1, y1, x2, y2), ...]
    """


    img = Image.open(image_path)
    width, height = img.size

    rectangles = []
    x = 0
    while x + rectangle_width <= width:
        rectangles.append((x, 0, x + rectangle_width, height))
        x += rectangle_width + gap_width

    if visualize:
        img_viz = img.copy()
        draw = ImageDraw.Draw(img_viz)

        for rect in rectangles:
            draw.rectangle(rect, outline="red", width=2)
        plt.figure(figsize=(10, 8))
        plt.imshow(np.array(img_viz))
        plt.axis('off')
        plt.title(f"Разделение на прямоугольники (ширина={rectangle_width}px, промежуток={gap_width}px)")

        #if output_path:
            #img_viz.save(output_path) # только для поиска багов
            #print(f"Визуализация сохранена в {output_path}")

        #plt.show()

    return rectangles


def count_rectangles_with_nonblack_pixels(image_path, rectangles, threshold=60, visualize=False, output_path=None,
                                          sample_rate=10):
    """
    Подсчитывает количество прямоугольников, у которых процент нечерных пикселей превышает порог.

    Параметры:
    image_path (str): Путь к исходному изображению
    rectangles (list): Список прямоугольников в формате [(x1, y1, x2, y2), ...]
    threshold (int): Пороговое значение для процента нечерных пикселей (по умолчанию 60%)
    visualize (bool): Флаг для создания визуализации
    output_path (str): Путь для сохранения визуализации
    sample_rate (int): Параметр уменьшения точности (анализируется каждый sample_rate-й пиксель)

    Возвращает:
    int: Количество прямоугольников с процентом нечерных пикселей > threshold
    """

    img = Image.open(image_path)
    img_array = np.array(img)

    count = 0

    if visualize:
        img_viz = img.copy()
        draw = ImageDraw.Draw(img_viz)

    for i, rect in enumerate(rectangles):
        x1, y1, x2, y2 = rect

        rect_img = img_array[y1:y2:sample_rate, x1:x2:sample_rate]

        total_pixels = rect_img.shape[0] * rect_img.shape[1]
        if total_pixels == 0:
            continue

        if len(img_array.shape) == 3:

            r_channel = rect_img[:, :, 0]
            g_channel = rect_img[:, :, 1]
            b_channel = rect_img[:, :, 2]
            significant_non_green = (r_channel > 24) | (b_channel > 24) | (g_channel > 100)

            average_brightness = (r_channel + g_channel + b_channel) / 3
            high_brightness = average_brightness > 33

            non_black_pixels = np.sum(significant_non_green | high_brightness)
        else:
            non_black_pixels = np.sum(rect_img > 16)

        non_black_percentage = (non_black_pixels / total_pixels) * 100

        if non_black_percentage > threshold:
            count += 1
            color = "green"
        else:
            color = "red"

        if visualize:
            draw.rectangle(rect, outline=color, width=2)
            text_pos = (x1 + 5, y1 + 5)
            draw.text(text_pos, f"{non_black_percentage:.1f}%", fill="white")
    if visualize and output_path:
        img_viz.save(output_path + str(datetime.datetime.now()).replace(" ", "").replace(".", "1").replace(":", "") + ".png")

    return count
