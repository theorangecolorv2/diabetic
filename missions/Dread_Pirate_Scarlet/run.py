import time
import pyautogui
from config import GLOBAL_ASSETS
from modules.click_on_image import lclick_on_image
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all
from global_functions.tractor import deploy, scoop

# переписать на дефолт
def run():
    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    if exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)

    lclick_on_image(GLOBAL_ASSETS + "main_over.png")
    time.sleep(1)
    lclick_on_image(GLOBAL_ASSETS + "gate.png")
    time.sleep(0.5)
    lclick_on_image(GLOBAL_ASSETS + "jump_button.png")
    time.sleep(0.5)
    lclick_on_image(GLOBAL_ASSETS + "mwd.png")

    time.sleep(5)
    wait(GLOBAL_ASSETS + "warping.png", acc=0.94, duration=60)
    time.sleep(10)

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    if exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)


    pyautogui.press("2")
    kill_all()
    pyautogui.press("2")
    pyautogui.press("3")
    wait(GLOBAL_ASSETS + "bastion_off.png", duration=55, acc=0.97)
    pyautogui.press("m")

    if exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)


    lclick_on_image(GLOBAL_ASSETS + "main_over.png")
    time.sleep(1)
    lclick_on_image(GLOBAL_ASSETS + "gate.png")
    time.sleep(0.5)
    lclick_on_image(GLOBAL_ASSETS + "jump_button.png")

    time.sleep(0.1)
    lclick_on_image(GLOBAL_ASSETS + "mwd.png")

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    if exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)

    time.sleep(0.1)
    pyautogui.press("3")
    pyautogui.press("2")
    kill_all()
    pyautogui.press("2")
    pyautogui.press("3")
    wait(GLOBAL_ASSETS + "bastion_off.png", duration=55, acc=0.97)
    pyautogui.press("m")
    if exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)


    lclick_on_image(GLOBAL_ASSETS + "main_over.png")
    time.sleep(1)
    lclick_on_image(GLOBAL_ASSETS + "gate.png")
    time.sleep(0.5)
    lclick_on_image(GLOBAL_ASSETS + "jump_button.png")

    time.sleep(0.1)
    lclick_on_image(GLOBAL_ASSETS + "mwd.png")

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    if exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)

    lclick_on_image(GLOBAL_ASSETS + "main_over.png")
    time.sleep(1)
    lclick_on_image("../missions/Dread_Pirate_Scarlet/scarlet.png")
    time.sleep(0.1)
    lclick_on_image(GLOBAL_ASSETS + "lock.png")
    time.sleep(3)
    pyautogui.press("1")
    pyautogui.press("2")
    time.sleep(0.1)
    pyautogui.press("3")
    wait(GLOBAL_ASSETS + "start_conv.png")
