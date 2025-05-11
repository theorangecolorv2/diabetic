import time
import pyautogui
from matplotlib.pyplot import close

from config import GLOBAL_ASSETS
from missions.default import default, use_gate
from modules.click_on_image import lclick_on_image
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all
from global_functions.tractor import deploy, scoop

# два скриптна на ренж как будто
def run():
    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)
    time.sleep(15)
    default(count=3, initial_gate=True, enemy_on_initial=True, close=True, loot=True)

    use_gate(mwd=True)

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    lclick_on_image(GLOBAL_ASSETS + "main_over.png")
    time.sleep(1)
    lclick_on_image("../missions/Dread_Pirate_Scarlet/scarlet.png")
    time.sleep(0.4)
    lclick_on_image(GLOBAL_ASSETS + "lock.png")
    time.sleep(3)
    pyautogui.press("1")
    time.sleep(0.1)
    pyautogui.press("3")
    wait(GLOBAL_ASSETS + "start_conv.png")

def run_blitz():
    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)

    pyautogui.press("3")
    time.sleep(0.2)
    pyautogui.press("4")

    use_gate(mwd=True)
    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    use_gate(mwd=True)
    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    use_gate(mwd=True)
    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    lclick_on_image(GLOBAL_ASSETS + "main_over.png")
    time.sleep(1)
    lclick_on_image("./missions/Dread_Pirate_Scarlet/scarlet.png")
    time.sleep(0.4)
    lclick_on_image(GLOBAL_ASSETS + "lock.png")
    time.sleep(3)
    pyautogui.press("1")
    time.sleep(0.1)
    wait(GLOBAL_ASSETS + "start_conv.png")