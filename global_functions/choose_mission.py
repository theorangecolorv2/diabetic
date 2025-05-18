import time
from config import GLOBAL_ASSETS
from global_functions.refresh import refresh, talk
from modules.click_on_image import lclick_on_image, rclick_coords, hover
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
    config_ammo(ammo=ammo)
    time.sleep(0.1)
    config_track_comps(tracking=tracking, universal=universal, optimal=optimal)
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

    if exists("global_functions/missions_names/angel_burner.png", acc=0.95):
        refit_burner("vengeance_team")
        time.sleep(0.2)
        from missions.angel_burner.run import run
        make(run, ammo="occult", tracking=0, optimal=0, universal=0) #


    if exists("global_functions/missions_names/sansha_burner.png", acc=0.95):
        refit_burner("vengeance_team")
        time.sleep(0.2)
        from missions.sansha_burner.run import run
        make(run, ammo="meson", tracking=0, optimal=0, universal=0) #


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
        make(run, ammo="fusion", tracking=2, optimal=0, universal=0) # фрегаты не убить; нужны варриоры, но все равно полчаса с ними
        # лучше рефит в две сетки или че нить такое

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
        make(run, ammo="emp", tracking=0, optimal=1, universal=0) # мжд аут # апрувед

    elif exists("global_functions/missions_names/Recon_1.png"):
        from missions.Recon_1.run import run
        make(run, ammo="fusion", tracking=2, optimal=0, universal=0)

    elif exists("global_functions/missions_names/Angel_Extravaganza.png"):
        from missions.Angel_Extravaganza.run import run
        make(run, ammo="fusion", tracking=1, optimal=1, universal=0)


def config_ammo(ammo = "phased"):

    if ammo in ['occult', 'mystic', 'tetryon', 'baryon', 'meson']:
        if exists(GLOBAL_ASSETS + "drop_it.png"): lclick_on_image(GLOBAL_ASSETS + "cargo.png") # add imgs
    else:
        if not exists(GLOBAL_ASSETS + "drop_it.png"): lclick_on_image(GLOBAL_ASSETS + "cargo.png")  # add imgs

    time.sleep(0.2)

    x1,y1,x2,y2 = find_image(GLOBAL_ASSETS + "module_static_img.png")
    guns = (x1 + 280,y1-94,x2 + 280,y2-94)

    rclick_coords(*guns)
    time.sleep(0.2)
    if exists(GLOBAL_ASSETS + "unload.png"):
        lclick_on_image(GLOBAL_ASSETS + "unload.png")
        time.sleep(0.5)

    if ammo == "phased":
        rclick_coords(*guns)
        time.sleep(0.1)
        if exists(GLOBAL_ASSETS + "phased.png"):
            lclick_on_image(GLOBAL_ASSETS + "phased.png")
    elif ammo == "emp":
        rclick_coords(*guns)
        time.sleep(0.1)
        lclick_on_image(GLOBAL_ASSETS + "emp.png")
    elif ammo == "hail":
        rclick_coords(*guns)
        time.sleep(0.1)
        lclick_on_image(GLOBAL_ASSETS + "hail.png")
    elif ammo == "fusion":
        rclick_coords(*guns)
        time.sleep(0.1)
        lclick_on_image(GLOBAL_ASSETS + "fusion.png")
    elif ammo == "occult":
        rclick_coords(*guns)
        time.sleep(0.1)
        if exists(GLOBAL_ASSETS + "occult.png"):
            lclick_on_image(GLOBAL_ASSETS + "occult.png")
    elif ammo == "mystic":
        rclick_coords(*guns)
        time.sleep(0.1)
        lclick_on_image(GLOBAL_ASSETS + "mystic.png")
    elif ammo == "meson":
        rclick_coords(*guns)
        time.sleep(0.1)
        lclick_on_image(GLOBAL_ASSETS + "meson.png")
    elif ammo == "baryon":
        rclick_coords(*guns)
        time.sleep(0.1)
        lclick_on_image(GLOBAL_ASSETS + "baryon.png")
    elif ammo == "tetryon":
        rclick_coords(*guns)
        time.sleep(0.1)
        lclick_on_image(GLOBAL_ASSETS + "tetryon.png")


    time.sleep(0.1)


def config_track_comps(universal=0, tracking=1, optimal=1):
    comps_coords = []
    for img in ['track_comp.png', 'track_comp_optimal.png', 'track_comp_tracking']: # add img
        if len(find_image(GLOBAL_ASSETS + img)) > 0:
            comps_coords.append(find_image(GLOBAL_ASSETS + img)) # find all images

    for i in range(universal):
        rclick_coords(*comps_coords[i])
        time.sleep(0.2)
        if exists(GLOBAL_ASSETS + "unload.png"):
            lclick_on_image(GLOBAL_ASSETS + "unload.png")
        time.sleep(0.2)

    hover(GLOBAL_ASSETS + 'route.png')
    time.sleep(0.4)

    for i in range(universal, universal + tracking):
        rclick_coords(*comps_coords[i])
        if exists(GLOBAL_ASSETS + "tracking.png"):
            lclick_on_image(GLOBAL_ASSETS + "tracking.png")
        time.sleep(0.2)

    hover(GLOBAL_ASSETS + 'route.png')
    time.sleep(0.4)

    for i in range(universal + tracking, universal + tracking + optimal):
        rclick_coords(*comps_coords[i])
        if exists(GLOBAL_ASSETS + "optimal.png"):
            lclick_on_image(GLOBAL_ASSETS + "optimal.png")
        time.sleep(0.2)


def refit_vargur(default = True, mjd = False, extra_tank = False): # make it
    if default:
        pass
    if mjd:
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
