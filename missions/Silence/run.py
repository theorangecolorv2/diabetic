import time
import pyautogui
from config import GLOBAL_ASSETS
from missions.default import default
from modules.click_on_image import lclick_on_image
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all
from global_functions.tractor import deploy, scoop

# переделать через дефолт

def run():

    while exists(GLOBAL_ASSETS + "warping.png"):
        time.sleep(2)

    default(count=3, initial_gate=True, loot=True,close=True)