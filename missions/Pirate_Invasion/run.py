from config import GLOBAL_ASSETS
from global_functions.kill_all import kill_frig
from missions.default import default
from modules.find_image import exists


def run():
    default(count=1, initial_gate=True, loot=True, kill_bs_only=True) # range script (x2 ) дописать то, что мы включаем два трек компа
    # переделать( нкжно убивать фрегаты, они поинтят
    if exists(GLOBAL_ASSETS + "warp_dis.png") or exists(GLOBAL_ASSETS + "warp_scram.png"):
        kill_frig()