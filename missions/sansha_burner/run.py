import time
import pyautogui
from fontTools.misc.plistlib import dumps

from config import GLOBAL_ASSETS
from global_functions.checks import count_targets, check_guns
from missions.default import turn_on, default, use_gate, loot_wreck
from modules.click_on_image import lclick_on_image, hover, rclick_on_image
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all, lock_all, shoot_all
from global_functions.tractor import deploy, scoop

def run():
    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    lclick_on_image(GLOBAL_ASSETS + "armor_rep.png")
    time.sleep(0.2)
    lclick_on_image(GLOBAL_ASSETS + "resist.png")
    time.sleep(0.2)
    lclick_on_image(GLOBAL_ASSETS + "track_comp.png")
    time.sleep(0.2)

    use_gate(mwd=False)

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    lock_all(count=1)
    time.sleep(0.2)

    pyautogui.press("1")
    time.sleep(0.2)
    pyautogui.press("2")

    while count_targets() == 0:
        time.sleep(1)

    while count_targets() > 0:
        time.sleep(2)



    #loot_wreck()
