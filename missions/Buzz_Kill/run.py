from missions.default import default, use_gate, turn_on
import time
import pyautogui
from config import GLOBAL_ASSETS
from global_functions.travel import wait_land
from modules.click_on_image import lclick_on_image
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all, kill_bs, lock_all, shoot_all
from global_functions.tractor import deploy, scoop


def run():
    default(count=1, initial_gate=False, loot=True)