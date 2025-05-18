import time
import pyautogui
from config import GLOBAL_ASSETS
from modules.click_on_image import lclick_on_image
from modules.find_image import wait, exists
from global_functions.kill_all import kill_frig, kill_all, kill_bs
from global_functions.tractor import deploy, scoop

def turn_on(bastion = True, not_first = False):
    if bastion:
        pyautogui.press("2")
        time.sleep(0.1)
    pyautogui.press("3")
    time.sleep(0.1)
    if not not_first:
        pyautogui.press("4")
        time.sleep(0.1)
        activate_track_comps()

def activate_track_comps():
    if exists(GLOBAL_ASSETS + "track_comp.png"): lclick_on_image(GLOBAL_ASSETS + "track_comp.png")
    time.sleep(0.4)
    if exists(GLOBAL_ASSETS + "track_comp_tracking.png"): lclick_on_image(GLOBAL_ASSETS + "track_comp_tracking.png") # add
    time.sleep(0.4)
    if exists(GLOBAL_ASSETS + "track_comp_optimal.png"): lclick_on_image(GLOBAL_ASSETS + "track_comp_optimal.png") # add



def use_gate(mwd = True):
    lclick_on_image(GLOBAL_ASSETS + "main_over.png")
    time.sleep(1)
    lclick_on_image(GLOBAL_ASSETS + "gate.png")
    time.sleep(0.5)
    lclick_on_image(GLOBAL_ASSETS + "jump_button.png")
    time.sleep(0.5)
    if mwd: lclick_on_image(GLOBAL_ASSETS + "mwd.png")
    wait(GLOBAL_ASSETS + "warping.png", acc=0.92, duration=90)


def default(count, initial_gate = True, loot = True, close = False, first_gate_range = 0, enemy_on_initial = False,
            kill_bs_only = False, wait_resp = False, kill_frig_first = True, extra_comp = True):

    while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
        time.sleep(2)
    time.sleep(2)

    if close and exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)

    if enemy_on_initial:
        turn_on()
        kill_all()
        pyautogui.press("2")
        time.sleep(0.2)
        time.sleep(0.2)
        pyautogui.press("m")
        time.sleep(0.2)
        pyautogui.press("3")
        time.sleep(0.2)
        pyautogui.press("4")
        time.sleep(0.2)
        activate_track_comps()
        wait(GLOBAL_ASSETS + "bastion_off.png", duration=55, acc=0.97)

    if close and exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)

    if initial_gate:
        lclick_on_image(GLOBAL_ASSETS + "main_over.png")
        time.sleep(1)
        lclick_on_image(GLOBAL_ASSETS + "gate.png")
        time.sleep(0.5)
        lclick_on_image(GLOBAL_ASSETS + "jump_button.png")
        if enemy_on_initial: lclick_on_image(GLOBAL_ASSETS + "mwd.png")

        wait(GLOBAL_ASSETS + "warping.png", acc=0.92, duration=75)

    if close and exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)

    for i in range(count):
        while exists(GLOBAL_ASSETS + "warping.png", acc=0.92):
            time.sleep(2)
        time.sleep(2)

        if close and exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)
        time.sleep(0.5)
        if loot: deploy()
        time.sleep(0.8)

        pyautogui.press("2")
        time.sleep(0.1)
        pyautogui.press("3")
        time.sleep(0.1)
        if i == 0:
            pyautogui.press("4")
            time.sleep(0.1)
            activate_track_comps()

        if wait_resp: time.sleep(12)

        if not kill_bs_only:
            if kill_frig_first: kill_frig()
            kill_all(wait_resp=wait_resp)
        else: kill_bs()

        if close and exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png", acc=0.92)
        time.sleep(0.8)

        pyautogui.press("2")
        time.sleep(0.1)
        pyautogui.press("3")
        time.sleep(0.1)
        pyautogui.press("m")
        time.sleep(0.1)

        if loot: scoop()

        wait(GLOBAL_ASSETS + "bastion_off.png", duration=55, acc=0.97)

        time.sleep(1)

        if i+1 != count: use_gate(mwd = True)

def loot_wreck():
    print("доделай")