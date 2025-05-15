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

# occult
# orbit 15, wait point, lock + web, orbit 5, kill
# не провеерно все еще. оч много дпса
def run():
    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    lclick_on_image(GLOBAL_ASSETS + "armor_rep.png")
    time.sleep(0.2)
    pyautogui.press("4")
    time.sleep(0.2)
    pyautogui.press("5")
    time.sleep(0.2)
    use_gate(mwd=False)
    time.sleep(0.1)

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)
    lclick_on_image(GLOBAL_ASSETS + "ab.png")
    time.sleep(0.5)

    rclick_on_image("missions/enyo_team/burner_enyo.png")
    time.sleep(0.5)
    hover(GLOBAL_ASSETS + "orbit.png")
    time.sleep(0.4)
    lclick_on_image(GLOBAL_ASSETS + "15km.png")
    wait(GLOBAL_ASSETS + "point.png", duration=35)
    lclick_on_image(GLOBAL_ASSETS + "lock.png")
    time.sleep(0.2)
    pyautogui.press("2")
    time.sleep(0.2)

    lclick_on_image(GLOBAL_ASSETS + "orbit_selected.png")

    time.sleep(4)
    pyautogui.press("1")
    time.sleep(0.3)
    while not check_guns():
        pyautogui.press("1")
        time.sleep(0.3)

    while count_targets() > 0:
        time.sleep(2)

    #loot_wreck()
