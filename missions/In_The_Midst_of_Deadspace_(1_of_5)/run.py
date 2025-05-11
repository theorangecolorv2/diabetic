import time
import pyautogui
from fontTools.misc.plistlib import dumps

from config import GLOBAL_ASSETS
from global_functions.checks import count_targets
from missions.default import turn_on, default, use_gate, loot_wreck
from modules.click_on_image import lclick_on_image, hover
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all, lock_all, shoot_all
from global_functions.tractor import deploy, scoop

def run():

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    default(count=3) # там чето лутать в конце надо хз лень
