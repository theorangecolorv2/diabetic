import time
import pyautogui
from config import GLOBAL_ASSETS
from global_functions.checks import count_targets, check_guns
from global_functions.choose_mission import config_ammo
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
    config_ammo(ammo="mystic")

    use_gate(mwd=False)

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    lclick_on_image(GLOBAL_ASSETS + "ab.png")
    time.sleep(0.2)

    lclick_on_image("missions/vengeance_team/burner_inq.png")
    time.sleep(0.3)
    lclick_on_image(GLOBAL_ASSETS + "approach.png")

    wait(GLOBAL_ASSETS + "point.png")
    time.sleep(0.2)
    hover(GLOBAL_ASSETS + "point.png")
    time.sleep(0.2)
    lclick_on_image(GLOBAL_ASSETS + "lock.png")
    time.sleep(0.2)

    pyautogui.press("1")
    time.sleep(0.2)
    pyautogui.press("2")

    while count_targets() == 0:
        time.sleep(1)
    while count_targets() > 0:
        time.sleep(1)

    time.sleep(2)

    lclick_on_image("missions/vengeance_team/burner_veng.png")
    time.sleep(0.3)
    lclick_on_image(GLOBAL_ASSETS + "orbit_selected.png")
    time.sleep(0.2)
    lclick_on_image(GLOBAL_ASSETS + "lock.png")
    time.sleep(0.2)
    config_ammo("occult")
    time.sleep(0.1)

    pyautogui.press("1")
    time.sleep(0.2)
    pyautogui.press("2")

    while count_targets() == 0:
        time.sleep(1)
    while count_targets() > 0:
        time.sleep(1)

    time.sleep(0.2)
    loot_wreck()
