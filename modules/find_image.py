from cv2 import imread, COLOR_BGR2GRAY, matchTemplate, TM_CCOEFF_NORMED, cvtColor
import numpy as np
import pyautogui
import os
from logging import basicConfig, info, INFO
import time
from config import SCREEN, LOGS_PATH



# Set up logging configuration
basicConfig(level=INFO,
            filename=LOGS_PATH,
            filemode="w",
            format="%(asctime)s %(levelname)s %(message)s")


def find_image(finding_element: str, region: tuple = SCREEN, acc: float = 0.8) -> list:
    coordinates = make_template(finding_element, region, acc)
    info(f"cords of {finding_element} added") if coordinates else info(f"image {finding_element} not found")
    return coordinates


def make_template(finding_element: str, region: tuple = SCREEN, acc: float = 0.8) -> list:
    frame = make_screenshot()

    # unpack tuple
    region_x, region_y, region_width, region_height = region

    # get img, cut screen
    img = imread(frame)
    roi = img[region_y:region_y + region_height, region_x:region_x + region_width]

    # get part
    template = imread(finding_element)
    if template is None or roi is None:
        info(f"load error of '{finding_element}' roi is empty")
        return []

    # ch/b
    roi_gray = cvtColor(roi, COLOR_BGR2GRAY)
    template_gray = cvtColor(template, COLOR_BGR2GRAY)

    # find wh
    w, h = template_gray.shape[::-1]

    # match algo
    result = matchTemplate(roi_gray, template_gray, TM_CCOEFF_NORMED)

    # accuracy
    threshold = acc  # 0.8 default
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
    info(f"make screenshot region: {region}")
    return os.path.abspath(image_path)



def wait(finding_element: str, region: tuple = SCREEN, duration: float = 20, interval: float = 1,
         acc: float = 0.8):
    start_time = time.time()
    coordinates = make_template(finding_element, region, acc=acc)

    while not coordinates:
        if time.time() - start_time > duration:
            info("didnt wait " + finding_element)
            return False
        time.sleep(interval)
        coordinates = make_template(finding_element, region, acc=acc)

    return True


def exists(finding_element: str, region: tuple = SCREEN, acc: float = 0.8):
    coordinates = make_template(finding_element, region, acc=acc)
    if coordinates:
        info(finding_element + ": exists")
        return True
    else:
        info(finding_element + ": not exists")
        return False