import time

from config import GLOBAL_ASSETS
from modules.click_on_image import lclick_on_image
from modules.find_image import exists, wait


def refresh():
    pass

def talk():
    wait(GLOBAL_ASSETS + "", duration=90, acc=0.9) # add img smth in dock
    if exists(GLOBAL_ASSETS + "start_conv.png"):
        lclick_on_image(GLOBAL_ASSETS + "start_conv.png")
        time.sleep(1)
        lclick_on_image(GLOBAL_ASSETS + "complete.png") # add img
        time.sleep(2)
        lclick_on_image(GLOBAL_ASSETS + "request.png") # ad img