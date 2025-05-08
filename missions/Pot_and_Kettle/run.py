import time
import pyautogui
from config import GLOBAL_ASSETS
from modules.click_on_image import lclick_on_image
from modules.find_image import wait, exists

def run():
    while exists(GLOBAL_ASSETS + "warping.png"):
        time.sleep(2)
    time.sleep(2)
    pyautogui.press("3")
    time.sleep(0.2)
    pyautogui.press("4")
    time.sleep(0.2)
    pyautogui.press("5")
    time.sleep(0.2)
    lclick_on_image(GLOBAL_ASSETS + "enemy_overview.png")
    time.sleep(0.5)
    lclick_on_image("missions/Pot_and_Kettle/prophecy.png")
    time.sleep(0.5)
    lclick_on_image(GLOBAL_ASSETS + "lock.png")
    time.sleep(7)
    pyautogui.press("1")
    time.sleep(15)