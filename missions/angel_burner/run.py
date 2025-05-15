import time
import pyautogui
from fontTools.misc.plistlib import dumps

from config import GLOBAL_ASSETS
from global_functions.checks import count_targets, check_guns
from missions.default import turn_on, default, use_gate, loot_wreck
from modules.click_on_image import lclick_on_image, hover
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all, lock_all, shoot_all
from global_functions.tractor import deploy, scoop

# occult
def run():
    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    lclick_on_image(GLOBAL_ASSETS + "armor_rep.png")

    use_gate(mwd=False)
    time.sleep(0.1)

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    lock_all(count=1)
    while count_targets() == 0:
        time.sleep(1)

    lclick_on_image(GLOBAL_ASSETS + "keep_at_range.png")
    time.sleep(0.2)
    lclick_on_image(GLOBAL_ASSETS + "ab.png")
    time.sleep(0.2)

    pyautogui.press("1")
    time.sleep(0.2)
    pyautogui.press("2")
    time.sleep(0.2)
    pyautogui.press("3")
    time.sleep(0.5)

    if not check_guns():
        time.sleep(1)
        pyautogui.press("1")

    while count_targets() > 0:
        time.sleep(1)
        if not check_guns():
            time.sleep(1)
            if not check_guns():
                pyautogui.press("1")

    loot_wreck()
