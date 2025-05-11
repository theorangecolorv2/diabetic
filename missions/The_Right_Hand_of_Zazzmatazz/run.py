import time
import pyautogui
from missions.default import turn_on
from config import GLOBAL_ASSETS
from modules.click_on_image import lclick_on_image
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all, kill_bs
from global_functions.tractor import deploy, scoop

def run():

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    if exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)

    turn_on()

    kill_frig()
    kill_bs()

    time.sleep(0.1)
    lclick_on_image(GLOBAL_ASSETS + "main_over.png")
    time.sleep(1)
    lclick_on_image(GLOBAL_ASSETS + "outpost.png")
    time.sleep(0.4)
    lclick_on_image(GLOBAL_ASSETS + "lock.png")
    pyautogui.press("1")
    time.sleep(20)

    pyautogui.press("2")
    time.sleep(0.1)
    pyautogui.press("m")
    time.sleep(0.2)
    wait(GLOBAL_ASSETS + "bastion_off.png", duration=60, acc=0.97)