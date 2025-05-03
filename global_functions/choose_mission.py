from config import GLOBAL_ASSETS
from global_functions.refresh import refresh, talk
from modules.click_on_image import lclick_on_image
from modules.find_image import exists
from global_functions.travel import travel, back

def make(run):
    #lclick_on_image(GLOBAL_ASSETS + "accept_dialog.png")
    if exists(GLOBAL_ASSETS + "track.png"): lclick_on_image(GLOBAL_ASSETS + "track.png")
    if exists(GLOBAL_ASSETS + "cross.png"): lclick_on_image(GLOBAL_ASSETS + "cross.png")

    travel()
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

    # etc

