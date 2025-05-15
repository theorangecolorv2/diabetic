from missions.default import default, use_gate, turn_on
import time
import pyautogui
from config import GLOBAL_ASSETS
from modules.click_on_image import lclick_on_image
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all, kill_bs, lock_all, shoot_all
from global_functions.tractor import deploy, scoop


def run():
    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)
    lclick_on_image("missions/Buzz_Kill/cruiser.png")
    time.sleep(0.5)
    lclick_on_image(GLOBAL_ASSETS + "approach.png")
    time.sleep(3)
    lclick_on_image(GLOBAL_ASSETS + "mjd.png")
    time.sleep(15)
    turn_on(bastion=True)
    time.sleep(0.2)
    deploy()
    time.sleep(0.1)

    lock_all()
    time.sleep(12)
    time.sleep(0.1)
    shoot_all()
    time.sleep(0.2)

    kill_frig()
    time.sleep(0.1)
    kill_all()
    time.sleep(0.1)

    pyautogui.press("2")
    time.sleep(0.1)
    pyautogui.press("3")
    time.sleep(0.1)
    pyautogui.press("m")
    time.sleep(0.1)

    scoop()

    wait(GLOBAL_ASSETS + "bastion_off.png", duration=55, acc=0.97)

    time.sleep(1)


