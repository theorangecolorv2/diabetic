from cv2 import imread, COLOR_BGR2GRAY, matchTemplate, TM_CCOEFF_NORMED, cvtColor
import numpy as np
import pyautogui
import os
from logging import basicConfig, info, INFO
import time
from config import SCREEN, LOGS_PATH

basicConfig(level=INFO,
            filename=LOGS_PATH,
            filemode="w",
            format="%(asctime)s %(levelname)s %(message)s")

def find_image(finding_element: str, region: tuple = SCREEN, acc: float = 0.8, use_color: bool = False) -> list:
    coordinates = make_template(finding_element, region, acc, use_color)
    info(f"cords of {finding_element} added") if coordinates else info(f"image {finding_element} not found")
    return coordinates

def make_template(finding_element: str, region: tuple = SCREEN, acc: float = 0.8, use_color: bool = False) -> list:
    frame = make_screenshot()

    region_x, region_y, region_width, region_height = region
    img = imread(frame)
    roi = img[region_y:region_y + region_height, region_x:region_x + region_width]

    template = imread(finding_element)
    if template is None or roi is None:
        info(f"load error of '{finding_element}' roi is empty")
        return []

    if not use_color:
        roi = cvtColor(roi, COLOR_BGR2GRAY)
        template = cvtColor(template, COLOR_BGR2GRAY)

    if len(template.shape) == 3:  # Цветное изображение (height, width, channels)
        h, w = template.shape[:2]
    else:  # Серое изображение (height, width)
        h, w = template.shape

    result = matchTemplate(roi, template, TM_CCOEFF_NORMED)
    threshold = acc
    loc = np.where(result >= threshold)

    coordinates = []
    for pt in zip(*loc[::-1]):
        coordinates.append((pt[0], pt[1], pt[0] + w, pt[1] + h))

    if coordinates:
        max_index = np.argmax(result[loc])
        best_match = coordinates[max_index]
        return list(best_match)
    else:
        info(f'cant found image {finding_element}')
        return []

def make_screenshot(region: tuple = SCREEN) -> str:
    image_path = "../global_assets/eve_screen.png"
    directory = os.path.dirname(image_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    pyautogui.screenshot(image_path, region=region)
    return os.path.abspath(image_path)

def wait(finding_element: str, region: tuple = SCREEN, duration: float = 20, interval: float = 1,
         acc: float = 0.8, use_color: bool = False):
    start_time = time.time()
    coordinates = make_template(finding_element, region, acc, use_color)

    while not coordinates:
        if time.time() - start_time > duration:
            info("didnt wait " + finding_element)
            return False
        time.sleep(interval)
        coordinates = make_template(finding_element, region, acc, use_color)
    return True

def exists(finding_element: str, region: tuple = SCREEN, acc: float = 0.8, use_color: bool = False):
    coordinates = make_template(finding_element, region, acc, use_color)
    if coordinates:
        info(finding_element + ": exists")
        return True
    else:
        info(finding_element + ": not exists")
        return False

import cv2
def get_green_pixel_ratio(image_path):
    """
    Подсчитывает соотношение зеленых пикселей на изображении.

    Аргументы:
        image_path (str): Путь к изображению

    Возвращает:
        float: Соотношение зеленых пикселей к общему количеству пикселей (0.0 - 1.0)
    """
    # Читаем изображение
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Не удалось загрузить изображение из {image_path}")

    # Конвертируем в цветовое пространство HSV для лучшего распознавания цвета
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Определяем диапазон для зеленого цвета в HSV
    # Настройте эти значения в зависимости от оттенка зеленого в вашем приложении
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    # Создаем маску для зеленых пикселей
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # Подсчитываем количество зеленых пикселей
    green_pixel_count = cv2.countNonZero(green_mask)

    # Подсчитываем общее количество пикселей
    total_pixels = img.shape[0] * img.shape[1]

    # Вычисляем соотношение
    ratio = green_pixel_count / total_pixels

    return ratio
