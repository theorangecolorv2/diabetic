import time
import pyautogui
from pyautogui import keyDown
from global_functions.checks import count_targets, check_guns
from modules.click_on_image import lclick_on_image, click_coords
from config import GLOBAL_ASSETS
from modules.find_image import exists, wait, find_image
import keyboard


def kill_all():
    if lock_all() == 0:
        return 1
    time.sleep(13)
    while count_targets() > 0:
        shoot_all()
        time.sleep(3)
        if exists(GLOBAL_ASSETS + "nothing.png"):
            continue
        else:
            lock_all()
            time.sleep(13)

def kill_all1():
    if lock_all() == 0:
        return 1
    while not exists(GLOBAL_ASSETS + "nothing.png"):
        shoot_all()
        lock_all()


def kill_frig1():
    if lock_all("frig") == 0:
        return 1
    while not exists(GLOBAL_ASSETS + "nothing.png"):
        shoot_all()
        lock_all("frig")


def kill_frig():
    if lock_all("frig") == 0:
        return 1
    time.sleep(13)
    while count_targets() > 0:
        shoot_all()
        time.sleep(3)
        if exists(GLOBAL_ASSETS + "nothing.png"):
            continue
        else:
            lock_all("frig")
            time.sleep(13)


def kill_bs():
    if lock_all("bs") == 0:
        return 1
    time.sleep(4)
    while count_targets() > 0:
        shoot_all()
        time.sleep(3)
        if exists(GLOBAL_ASSETS + "nothing.png"):
            continue
        else:
            lock_all("bs")
            time.sleep(4)


def shoot_all():
    while count_targets() > 0:
        count = count_targets()
        pyautogui.press("n")
        time.sleep(2.4)
        pyautogui.press("1")
        time.sleep(0.1)
        pyautogui.press("f")
        if not check_guns():
            pyautogui.press("1")
        cycles = 0
        while count_targets(current_count=count) >= count:
            time.sleep(1)
            cycles += 1
            if cycles > 30 and not check_guns():
                if count_targets() == 0: break
                pyautogui.press("1")
                pyautogui.press("n")
                time.sleep(0.1)
                pyautogui.press("f")
                cycles = 0


def lock_all(overview: str = "all"):
    if overview == 'bs':
        lclick_on_image(GLOBAL_ASSETS + "bs_overview.png")
    elif overview == "frig":
        lclick_on_image(GLOBAL_ASSETS + "frig_overview.png")
    elif overview == "all":
        lclick_on_image(GLOBAL_ASSETS + "enemy_overview.png")
    time.sleep(2)

    if exists(GLOBAL_ASSETS + "nothing.png"):
        return 0

    margin = 30 # расстояние между энеми (по идее фиксированное всегда)
    _c = find_image(GLOBAL_ASSETS + "name_over.png") # первый элемент энеми
    x1, y1, x2, y2 = _c
    #x1, y1, x2, y2
    keyboard.press("ctrl")
    for i in range(1,7):
        click_coords(x1, y1 + margin*i, x2, y2 + margin*i)
        time.sleep(0.3)
    keyboard.release("ctrl")


def kill_all_auto():
    time.sleep(12)
    count = count_targets()
    while count_targets(count) > 0:
        count = count_targets(count)
        pyautogui.press("f")
        pyautogui.press("1")
        iters = 0
        while count_targets(count) != count - 1:
            time.sleep(0.5)
            iters += 1
            if iters == 60:
                pyautogui.press("f")
                pyautogui.press("1")
                iters = 0
