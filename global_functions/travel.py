import time
from modules.click_on_image import lclick_on_image, rclick_coords
from config import GLOBAL_ASSETS
from modules.find_image import wait, find_image, exists


def travel1():
    lclick_on_image(GLOBAL_ASSETS + "undock_mission.png")
    wait(GLOBAL_ASSETS + "set_dest.png", duration=30)
    time.sleep(1)
    lclick_on_image(GLOBAL_ASSETS + "set_dest.png")
    time.sleep(1.5)

    while not exists(GLOBAL_ASSETS + "warp_to_location.png"):
        x1, y1, x2, y2 = find_image(GLOBAL_ASSETS + "route.png")
        rclick_coords(x1 - 12, y1 + 86, x2 - 12, y2 + 86)
        time.sleep(0.5)
        if exists(GLOBAL_ASSETS + "jump.png"):
            lclick_on_image(GLOBAL_ASSETS + "jump.png")
        else:
            rclick_coords(x1 - 12, y1 + 105, x2 - 12, y2 + 105)
            time.sleep(0.5)
            lclick_on_image(GLOBAL_ASSETS + "jump.png")
        wait(GLOBAL_ASSETS + "0ms.png", duration=180, acc=0.92)
        time.sleep(2)
    lclick_on_image(GLOBAL_ASSETS + "warp_to_location.png")


def travel():
    lclick_on_image(GLOBAL_ASSETS + "undock_mission.png")
    wait(GLOBAL_ASSETS + "set_dest.png", duration=30)
    time.sleep(1)
    lclick_on_image(GLOBAL_ASSETS + "set_dest.png")
    time.sleep(1.5)


time.sleep(1)
travel()