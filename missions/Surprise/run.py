import time
import pyautogui
from missions.default import turn_on
from config import GLOBAL_ASSETS
from modules.click_on_image import lclick_on_image
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all
from global_functions.tractor import deploy, scoop
from missions.default import default, use_gate

def run():
    default(1, initial_gate=False, loot=True) #opti,al range script needed
    # я бы рефитнул в еще один трек комп, мвд не нужно, танк тоже не сильно нужен

