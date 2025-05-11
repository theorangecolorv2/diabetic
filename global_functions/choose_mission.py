import time
from config import GLOBAL_ASSETS
from global_functions.refresh import refresh, talk
from modules.click_on_image import lclick_on_image, rclick_coords
from modules.find_image import exists, wait, find_image
from global_functions.travel import travel, back


def make(run, ammo, tracking, optimal, universal):

    if exists(GLOBAL_ASSETS + "accept_dialog.png"): lclick_on_image(GLOBAL_ASSETS + "accept_dialog.png")
    time.sleep(1.5)
    if exists(GLOBAL_ASSETS + "track.png"): lclick_on_image(GLOBAL_ASSETS + "track.png")
    time.sleep(0.5)
    if exists(GLOBAL_ASSETS + "close_dialog.png"): lclick_on_image(GLOBAL_ASSETS + "close_dialog.png")
    time.sleep(0.5)

    travel()

    time.sleep(0.2)
    #config(ammo=ammo, tracking=tracking, optimal=optimal, universal=universal)
    time.sleep(0.2)

    if exists(GLOBAL_ASSETS + "close.png", acc=0.92): lclick_on_image(GLOBAL_ASSETS + "close.png")

    run()

    back()
    talk()
    refresh()


def choose_mission_and_run():
    # burners
    if exists("global_functions/missions_names/vengeance_team.png", acc=0.95):
        refit_burner("vengeance_team")
        time.sleep(0.2)
        from missions.vengeance_team.run import run
        make(run, ammo="occult", tracking=0, optimal=0, universal=0) # мб не оккульт не помню


    # other missions
    elif exists("global_functions/missions_names/Exploited_Sens.png"):
        from missions.Exploted_Sens.run import run
        make(run, ammo="emp", tracking=2, optimal=0, universal=0)

    elif exists("global_functions/missions_names/Dread_Pirate_Scarlet.png"):
        from missions.Dread_Pirate_Scarlet.run import run
        make(run, ammo="phased", tracking=1, optimal=1, universal=0)

    elif exists("global_functions/missions_names/The_Serpenties_Spies.png"):  # need screenshot
        from missions.The_Serpenties_Spies.run import run
        make(run, ammo="phased", tracking=1, optimal=1, universal=0)

    elif exists("global_functions/missions_names/Surprise.png"):
        from missions.Surprise.run import run
        make(run, ammo="phased", tracking=0, optimal=2, universal=0)

    elif exists("global_functions/missions_names/pot_and_kettle.png"):
        from missions.Pot_and_Kettle.run import run
        make(run, ammo="phased", tracking=1, optimal=1, universal=0)

    elif exists("global_functions/missions_names/Massive_Attack.png"):
        from missions.Massive_Attack.run import run
        make(run, ammo="phased", tracking=0, optimal=2, universal=0)

    elif exists("global_functions/missions_names/Pirate_Invasion.png"):
        from missions.Pirate_Invasion.run import run
        make(run, ammo="phased", tracking=0, optimal=2, universal=0)

    elif exists("global_functions/missions_names/The_Mordus_Headhunters.png"): # нужен рефит в много танка вместо мжд; не проверено!!
        from missions.The_Mordus_Headhunters.run import run
        make(run, ammo="phased", tracking=1, optimal=0, universal=0)

    elif exists("global_functions/missions_names/Duo_of_Death.png"):
        from missions.Duo_of_Death.run import run
        make(run, ammo="phased", tracking=1, optimal=1, universal=0)

    elif exists("global_functions/missions_names/Buzz_Kill.png"): # fusion, 2 track comp (need explosive)
        from missions.Buzz_Kill.run import run
        make(run, ammo="fusion", tracking=2, optimal=0, universal=0) # не помню трекинг или оптимал нужен

    elif exists("global_functions/missions_names/The_Right_Hand_of_Zazzmatazz.png"):
        from missions.The_Right_Hand_of_Zazzmatazz.run import run
        make(run, ammo="fusion", tracking=1, optimal=1, universal=0)

    elif exists("global_functions/missions_names/Silence_the_Informant.png"):
        from missions.Silence.run import run
        make(run, ammo="fusion", tracking=1, optimal=1, universal=0)

    elif exists("global_functions/missions_names/Vengeance.png"):
        from missions.Vengeance.run import run
        make(run, ammo="fusion", tracking=1, optimal=1, universal=0)

    elif exists("global_functions/missions_names/Infiltrated_Outposts.png"):
        from missions.Infiltrated_Outposts.run import run
        make(run, ammo="fusion", tracking=2, optimal=0, universal=0)

    elif exists("global_functions/missions_names/Attack_of_the_Drones.png"):
        from missions.Attack_of_the_Drones.run import run
        #make(run, ammo="fusion", tracking=2, optimal=0, universal=0) # оч много дпса с баттлов рефит в танк

    elif exists("global_functions/missions_names/Recon_1.png"):
        from missions.Recon_1.run import run
        make(run, ammo="fusion", tracking=2, optimal=0, universal=0)


#Attack_of_the_Drones

def config(ammo = "phased", tracking = 1, optimal = 1, universal = 0):
    if universal + tracking + optimal > 2:
        print("too much scripts, i have only 2 track comps")
        return 0
    x1,y1,x2,y2 = find_image(GLOBAL_ASSETS + "module_static_img.png") # some static img
    guns = (x1 + 282,y1-92,x2 + 282,y2-92) # calc it
    track_comp = [(x1+380,y1-92,x2+380,y2-92), (x1+418,y1-92,x2+418,y2-92)] # calc it
    if ammo == "phased":
        rclick_coords(*guns)
        time.sleep(0.4)
        if exists(GLOBAL_ASSETS + "phased.png"):
            lclick_on_image(GLOBAL_ASSETS + "phased.png") # add img!
    elif ammo == "emp":
        rclick_coords(*guns)
        time.sleep(0.4)
        lclick_on_image(GLOBAL_ASSETS + "emp.png") # add img!
    elif ammo == "hail":
        rclick_coords(*guns)
        time.sleep(0.4)
        lclick_on_image(GLOBAL_ASSETS + "hail.png") # add img!
    elif ammo == "fusion":
        rclick_coords(*guns)
        time.sleep(0.4)
        lclick_on_image(GLOBAL_ASSETS + "fusion.png") # add img!
    elif ammo == "occult":
        rclick_coords(*guns)
        time.sleep(0.4)
        if exists(GLOBAL_ASSETS + "occult.png"):
            lclick_on_image(GLOBAL_ASSETS + "occult.png")  # add img!
    elif ammo == "mystic":
        rclick_coords(*guns)
        time.sleep(0.4)
        lclick_on_image(GLOBAL_ASSETS + "mystic.png")  # add img!

    time.sleep(0.4)

    for i in range(universal):
        rclick_coords(*track_comp[i])
        time.sleep(0.4)
        lclick_on_image(GLOBAL_ASSETS + "unload.png") # add img
        time.sleep(0.4)



    for i in range(universal, universal + tracking):
        rclick_coords(*track_comp[i])
        time.sleep(0.4)
        lclick_on_image(GLOBAL_ASSETS + "tracking_speed.png") # add img
        time.sleep(0.4)

    for i in range(universal + tracking, universal + tracking + optimal):
        rclick_coords(*track_comp[i])
        time.sleep(0.4)
        lclick_on_image(GLOBAL_ASSETS + "optimal_range.png") # add img
        time.sleep(0.4)


def refit_vargur(default = True, extra_comp = False, extra_tank = False): # make it
    if default:
        pass
    if extra_comp:
        pass
    if extra_tank:
        pass


def refit_burner(burner_type):
    if burner_type == "team_enyo":
        pass
    elif burner_type == "team_vengeance":
        pass
    # ...
    elif burner_type == "solo_angel":
        pass
