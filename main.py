import time

from missions.default import default
from modules.click_on_image import lclick_on_image
from config import GLOBAL_ASSETS
from global_functions.api_reader import ping, get_eve_module_quantity
from global_functions.checks import check_guns
from global_functions.choose_mission import choose_mission_and_run
from global_functions.get_pid import get_pid
from global_functions.kill_all import kill_frig, kill_all
from global_functions.tractor import deploy, scoop
from  global_functions.travel import travel, back
import pyautogui
from modules.find_image import wait, exists

def main():
    working = True
    count = 0

    print("инициализирум и проверяем веб-сервер")
    if not ping():
        print(f"сервер лежит, код: {ping()}")
        return Exception("сервер лежит ")
    else:
        print("сервер работает")


    while working:
        choose_mission_and_run()
        count += 1
        print("\n")
        print("_"*50)
        print(f"миссий сделано: {count} \n")


time.sleep(1)
scoop()