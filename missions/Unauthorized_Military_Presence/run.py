import time
import pyautogui
from config import GLOBAL_ASSETS
from global_functions.travel import wait_land
from missions.default import turn_on, default
from modules.click_on_image import lclick_on_image, hover
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all, lock_all, shoot_all
from global_functions.tractor import deploy, scoop


def run():
    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    default(1, initial_gate=False, loot=False)

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    lclick_on_image(GLOBAL_ASSETS + "enemy_overview.png")
    time.sleep(0.5)
    hover(GLOBAL_ASSETS + "name_over.png")
    time.sleep(0.1)
    while not exists("missions/Unauthorized_Military_Presence/angel_cartel_personel.png"):
        pyautogui.scroll(-150)
        time.sleep(0.4)
    time.sleep(0.2)
    lclick_on_image("missions/Unauthorized_Military_Presence/angel_cartel_personel.png") # !!!! add
    time.sleep(0.3)
    lclick_on_image(GLOBAL_ASSETS + "approach.png")
    time.sleep(2)
    lclick_on_image(GLOBAL_ASSETS + "mjd.png")
    time.sleep(13)

    turn_on(not_first=True)

    deploy()

    lclick_on_image(GLOBAL_ASSETS + "frig_overview.png")

    lock_all()
    time.sleep(12)
    shoot_all()

    scoop()

    if exists("missions/Unauthorized_Military_Presence/you_need_10.png"): # u need to ...
        deploy()

        lock_all()
        shoot_all()
        time.sleep(15)
        scoop()


