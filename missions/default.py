import time
import pyautogui
from config import GLOBAL_ASSETS
from global_functions.travel import wait_land
from modules.click_on_image import lclick_on_image
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all
from global_functions.tractor import deploy, scoop


def default(count, starts_with_gate, loot = True, close = False, first_gate_range = 0):

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    if starts_with_gate:
        lclick_on_image(GLOBAL_ASSETS + "main_over.png")
        time.sleep(1)
        lclick_on_image(GLOBAL_ASSETS + "gate.png")
        time.sleep(0.5)
        lclick_on_image(GLOBAL_ASSETS + "jump_button.png")

        time.sleep(0.5)
        if first_gate_range > 0: lclick_on_image(GLOBAL_ASSETS + "mwd.png")

        wait(GLOBAL_ASSETS + "warping.png", acc=0.92, duration=25)


    for i in range(count):
        while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
            time.sleep(2)
        time.sleep(2)

        if close and exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)
        time.sleep(0.5)
        if loot: deploy()
        time.sleep(0.8)

        pyautogui.press("2")
        time.sleep(0.1)
        pyautogui.press("3")
        time.sleep(0.1)
        if i == 0:
            pyautogui.press("4")
            time.sleep(0.1)
            pyautogui.press("5")

        kill_frig()
        kill_all()

        if close and exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)
        time.sleep(0.8)

        pyautogui.press("2")
        time.sleep(0.1)
        pyautogui.press("3")
        time.sleep(0.1)
        pyautogui.press("m")
        time.sleep(0.1)

        if loot: scoop()

        wait(GLOBAL_ASSETS + "bastion_off.png", duration=55, acc=0.97)

        time.sleep(1)

        lclick_on_image(GLOBAL_ASSETS + "main_over.png")
        time.sleep(1)
        lclick_on_image(GLOBAL_ASSETS + "gate.png")
        time.sleep(0.5)
        lclick_on_image(GLOBAL_ASSETS + "jump_button.png")
        time.sleep(0.5)
        lclick_on_image(GLOBAL_ASSETS + "mwd.png")
        wait(GLOBAL_ASSETS + "warping.png", acc=0.92, duration=25)