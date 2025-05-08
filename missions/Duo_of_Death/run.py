import time
import pyautogui
from config import GLOBAL_ASSETS
from modules.click_on_image import lclick_on_image, hover
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all, kill_bs
from global_functions.tractor import deploy, scoop
from missions.default import default, use_gate, turn_on


def run():
    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    use_gate(mwd=False)
    time.sleep(0.5)

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    deploy()
    turn_on()
    kill_bs()

    time.sleep(1)
    pyautogui.press("2")
    time.sleep(0.5)
    pyautogui.press("m")
    time.sleep(0.5)
    wait(GLOBAL_ASSETS + "bastion_off.png", duration=55, acc=0.97)
    time.sleep(0.2)

    lclick_on_image(GLOBAL_ASSETS + "mtu.png")
    time.sleep(0.5)
    lclick_on_image(GLOBAL_ASSETS + "loot.png")
    time.sleep(0.5)
    while not (exists(GLOBAL_ASSETS + "need_to_halle.png") or exists(GLOBAL_ASSETS + "dock_mission.png") or exists(GLOBAL_ASSETS + "set_dest.png")):
        lclick_on_image(GLOBAL_ASSETS + "loot_all.png")
        time.sleep(0.2)
        hover(GLOBAL_ASSETS + "bs_overview.png")
        time.sleep(3)

    scoop()

