import time
from pickle import GLOBAL

from config import GLOBAL_ASSETS
from global_functions.refresh import refresh, talk
from modules.click_on_image import lclick_on_image
from modules.find_image import exists, wait
from global_functions.travel import travel, back

def make(run):
    if exists(GLOBAL_ASSETS + "accept_dialog.png"): lclick_on_image(GLOBAL_ASSETS + "accept_dialog.png")
    time.sleep(0.5)
    if exists(GLOBAL_ASSETS + "track.png"): lclick_on_image(GLOBAL_ASSETS + "track.png")
    time.sleep(0.5)
    if exists(GLOBAL_ASSETS + "cross.png"): lclick_on_image(GLOBAL_ASSETS + "cross.png")
    time.sleep(0.5)

    travel()
    time.sleep(5)

    if exists(GLOBAL_ASSETS + "close.png"): lclick_on_image(GLOBAL_ASSETS + "close.png")

    run()
    back()
    talk()
    refresh()


def choose_mission_and_run():
    # if exists("./missions_names/The_Score.png"):
    #     from missions.The_Score.run import run
    #     make(run)
    # elif exists("./missions_names/Angel_Extravaganza.png"):
    #     from missions.Angel_Extravaganza.run import run
    #     make(run)
    if exists("global_functions/missions_names/Exploited_Sens.png"):
        from missions.Exploted_Sens.run import run
        make(run)
    elif exists("global_functions/missions_names/Dread_Pirate_Scarlet.png"):
        from missions.Dread_Pirate_Scarlet.run import run
        make(run)
    elif exists("global_functions/missions_names/The_Serpenties_Spies.png"):
        from missions.The_Serpenties_Spies.run import run
        make(run)
        

    # etc

