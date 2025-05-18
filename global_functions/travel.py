import time
from global_functions.get_pid import get_pid
from modules.click_on_image import lclick_on_image, rclick_coords, click_here
from config import GLOBAL_ASSETS, LOGS_PATH
from modules.find_image import wait, find_image, exists
from logging import basicConfig, info, INFO
from global_functions.api_reader import get_eve_module_quantity
import pyautogui


basicConfig(level=INFO,
            filename=LOGS_PATH,
            filemode="w",
            format="%(asctime)s %(levelname)s %(message)s")


def travel():
    lclick_on_image(GLOBAL_ASSETS + "undock_mission.png")
    while not (exists(GLOBAL_ASSETS + "set_dest.png") or exists(GLOBAL_ASSETS + "warp_to_location.png")):
        time.sleep(1)
    time.sleep(5)
    if exists(GLOBAL_ASSETS + "warp_to_location.png"):
        lclick_on_image(GLOBAL_ASSETS + "warp_to_location.png")
        wait(GLOBAL_ASSETS + "warping.png")
        return
    lclick_on_image(GLOBAL_ASSETS + "set_dest.png")
    time.sleep(1.5)
    lclick_on_image(GLOBAL_ASSETS + "jump_over.png")
    time.sleep(0.5)
    # deleted wait
    while not exists(GLOBAL_ASSETS + "warp_to_location.png"):
        lclick_on_image(GLOBAL_ASSETS + "gate_yellow.png", use_color=True)
        time.sleep(0.5)
        lclick_on_image(GLOBAL_ASSETS + "jump_button.png")
        wait(GLOBAL_ASSETS + "0ms.png", duration=180, acc=0.95)
        time.sleep(2)

    lclick_on_image(GLOBAL_ASSETS + "warp_to_location.png")
    time.sleep(1)
    wait(GLOBAL_ASSETS + "warping.png", duration=15)
    info("warping to mission location")

def back():
    if exists(GLOBAL_ASSETS + "dock_mission.png"):
        lclick_on_image(GLOBAL_ASSETS + "dock_mission.png")
        time.sleep(1)
        return

    if exists(GLOBAL_ASSETS + "need_to_halle.png") or exists(GLOBAL_ASSETS + "set_dest.png"): #no img
        lclick_on_image(GLOBAL_ASSETS + "set_dest.png")
        time.sleep(1.5)
        lclick_on_image(GLOBAL_ASSETS + "jump_over.png")
        time.sleep(0.5)
        click_here()

        while exists(GLOBAL_ASSETS + "gate_yellow.png", use_color=True):
            lclick_on_image(GLOBAL_ASSETS + "gate_yellow.png", use_color=True)
            time.sleep(0.5)
            lclick_on_image(GLOBAL_ASSETS + "jump_button.png")
            wait(GLOBAL_ASSETS + "0ms.png", duration=180, acc=0.95)
            time.sleep(2)

        time.sleep(1)
        lclick_on_image(GLOBAL_ASSETS + "dock_mission.png")

    else:
        info("mission not completed or have no image!")
        return 0
