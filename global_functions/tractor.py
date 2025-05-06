import time
from global_functions.get_pid import get_pid
from modules.click_on_image import lclick_on_image, rclick_on_image, click_here
from config import GLOBAL_ASSETS, LOGS_PATH
from modules.find_image import wait, find_image, exists
from logging import basicConfig, info, INFO
from global_functions.api_reader import get_eve_module_quantity


def deploy():
    rclick_on_image(GLOBAL_ASSETS + "packrat.png")
    time.sleep(0.5)
    lclick_on_image(GLOBAL_ASSETS + "launch_for_self.png")

def scoop():
    lclick_on_image(GLOBAL_ASSETS + "main_over.png")
    time.sleep(1.5)
    rclick_on_image(GLOBAL_ASSETS + "mtu.png")
    time.sleep(0.5)
    lclick_on_image(GLOBAL_ASSETS + "scoop.png")

    wait(GLOBAL_ASSETS + "cargo_container.png")

    lclick_on_image(GLOBAL_ASSETS + "cargo_container.png")
    time.sleep(0.5)
    lclick_on_image(GLOBAL_ASSETS + "loot.png")
    time.sleep(1)
    lclick_on_image(GLOBAL_ASSETS + "loot_all.png")
    time.sleep(0.4)


