import time
from modules.click_on_image import lclick_on_image, rclick_coords
from config import GLOBAL_ASSETS
from modules.find_image import wait, find_image, exists


def travel():
    lclick_on_image(GLOBAL_ASSETS + "undock_mission.png")
    wait(GLOBAL_ASSETS + "set_dest.png", duration=30)
    time.sleep(1)
    lclick_on_image(GLOBAL_ASSETS + "set_dest.png")
    time.sleep(1.5)
    lclick_on_image(GLOBAL_ASSETS + "jump_over.png")
    time.sleep(1)

    while not exists(GLOBAL_ASSETS + "warp_to_location.png"):
        lclick_on_image(GLOBAL_ASSETS + "gate_yellow.png", use_color=True)
        time.sleep(0.5)
        lclick_on_image(GLOBAL_ASSETS + "jump_button.png")
        wait(GLOBAL_ASSETS + "0ms.png", duration=180, acc=0.95)
        time.sleep(2)

    lclick_on_image(GLOBAL_ASSETS + "warp_to_location.png")

def back():
    pass