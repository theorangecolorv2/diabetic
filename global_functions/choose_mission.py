from modules.find_image import exists
from global_functions.travel import travel, back

def choose_mission():
    if exists("./missions_names/The_Score.png"):
        from missions.The_Score.run import run
        travel()
        run()
        back()
    elif exists("./missions_names/Angel_Extravaganza.png"):
        from missions.Angel_Extravaganza.run import run
        travel()
        run()
        back()

    # etc

