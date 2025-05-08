import time
import pyautogui
from missions.default import turn_on
from config import GLOBAL_ASSETS
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all
from global_functions.tractor import deploy, scoop


def run():
    #emp and tacking speed script

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    deploy()

    turn_on()

    kill_frig()
    kill_all()
    pyautogui.press("2")
    time.sleep(0.1)
    pyautogui.press("m")
    time.sleep(0.2)
    scoop()
    wait(GLOBAL_ASSETS + "bastion_off.png", duration=60, acc=0.97)