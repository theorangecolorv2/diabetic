import time

import pyautogui

from config import GLOBAL_ASSETS
from modules.find_image import wait
from global_functions.kill_all import kill_frig, kill_all
from global_functions.tractor import deploy, scoop


def run():
    deploy()
    pyautogui.press("2")
    time.sleep(0.1)
    pyautogui.press("3")
    time.sleep(0.1)
    pyautogui.press("4")
    time.sleep(0.2)
    pyautogui.press("5")
    # добавить треикнг скрипты и перезаряжку на хеил наверно
    pyautogui.press("n")
    kill_frig()
    kill_all()
    pyautogui.press("2")
    time.sleep(0.1)
    pyautogui.press("m")
    time.sleep(0.2)
    scoop()
    wait(GLOBAL_ASSETS + "bastion_off.png", duration=55, acc=0.97)