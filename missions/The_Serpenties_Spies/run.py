import time
import pyautogui
from config import GLOBAL_ASSETS
from global_functions.travel import wait_land
from modules.click_on_image import lclick_on_image
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all
from global_functions.tractor import deploy, scoop
from missions.default import turn_on, use_gate


def run():
    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    use_gate(mwd = False)

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    lclick_on_image(GLOBAL_ASSETS + "enemy_overview.png")
    time.sleep(1)
    lclick_on_image(GLOBAL_ASSETS + "destr.png")
    time.sleep(0.5)
    lclick_on_image(GLOBAL_ASSETS + "approach.png")
    time.sleep(3)
    lclick_on_image(GLOBAL_ASSETS + "mjd.png")
    time.sleep(12.5)

    turn_on()

    kill_frig()
    kill_all()

    pyautogui.press("2")
    time.sleep(0.1)
    pyautogui.press("m")
    time.sleep(0.1)


    wait(GLOBAL_ASSETS + "bastion_off.png", duration=55, acc=0.97)

