import time
import pyautogui
from config import GLOBAL_ASSETS
from modules.click_on_image import lclick_on_image
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all
from global_functions.tractor import deploy, scoop

# переделать через дефолт

def run():

    while exists(GLOBAL_ASSETS + "warping.png"):
        time.sleep(2)

    lclick_on_image(GLOBAL_ASSETS + "main_over.png")
    time.sleep(1)
    lclick_on_image(GLOBAL_ASSETS + "gate.png")
    time.sleep(0.5)
    lclick_on_image(GLOBAL_ASSETS + "jump_button.png")

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    for i in range(2):
        if exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)
        pyautogui.press("2")
        deploy()

        kill_frig()
        kill_all()
        time.sleep(1)
        pyautogui.press("2")
        time.sleep(0.1)
        pyautogui.press("m")
        time.sleep(0.1)
        pyautogui.press("3")

        scoop()

        wait(GLOBAL_ASSETS + "bastion_off.png", duration=55, acc=0.97)
        time.sleep(0.5)
        wait(GLOBAL_ASSETS + "bastion_off.png", duration=55, acc=0.97)

        lclick_on_image(GLOBAL_ASSETS + "main_over.png")
        time.sleep(1)
        lclick_on_image(GLOBAL_ASSETS + "gate.png")
        time.sleep(0.5)
        lclick_on_image(GLOBAL_ASSETS + "jump_button.png")

        time.sleep(0.5)
        lclick_on_image(GLOBAL_ASSETS + "mwd.png")

        while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
            time.sleep(2)
        time.sleep(2)

        pyautogui.press("3")