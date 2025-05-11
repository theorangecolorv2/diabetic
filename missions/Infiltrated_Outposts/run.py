import time
import pyautogui
from fontTools.misc.plistlib import dumps

from config import GLOBAL_ASSETS
from global_functions.checks import count_targets
from missions.default import turn_on, default, use_gate, loot_wreck
from modules.click_on_image import lclick_on_image, hover, rclick_coords, rclick_on_image
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all, lock_all, shoot_all
from global_functions.tractor import deploy, scoop

def run(): # neeed trackin

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    default(count=2, loot=True, enemy_on_initial=False) #
    time.sleep(0.2)

    rclick_on_image(GLOBAL_ASSETS + "bunker_text.png")
    time.sleep(0.4)
    lclick_on_image(GLOBAL_ASSETS + "lock_context.png")
    time.sleep(7)
    shoot_all()