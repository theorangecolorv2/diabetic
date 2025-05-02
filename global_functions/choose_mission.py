from global_functions.refresh import refresh, talk
from modules.find_image import exists
from global_functions.travel import travel, back

def make(run):
    travel()
    run()
    back()
    talk()
    refresh()


def choose_mission_and_run():
    if exists("./missions_names/The_Score.png"):
        from missions.The_Score.run import run
        make(run)
    elif exists("./missions_names/Angel_Extravaganza.png"):
        from missions.Angel_Extravaganza.run import run
        make(run)

    # etc

