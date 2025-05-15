import time
from pyautogui import click, doubleClick, rightClick
from logging import basicConfig, info, INFO
from config import LOGS_PATH, SCREEN
from modules import mousemover
from modules.find_image import find_image

mover = mousemover.MouseMover()


# Set up logging configuration
basicConfig(level=INFO,
            filename=LOGS_PATH,
            filemode="w",
            format="%(asctime)s %(levelname)s %(message)s")


def hover(image: str, region: tuple = SCREEN, duration: float = 0.25, acc: float = 0.8):
    x1, y1, x2, y2 = find_image(image, region, acc=acc)
    mover.move_to((x1 + x2) / 2, (y1 + y2) / 2, duration)

def lclick_on_image(image: str, region: tuple = SCREEN, duration: float = 0.25, acc: float = 0.8, use_color = False):
    if use_color:
        x1, y1, x2, y2 = find_image(image, region, acc=acc, use_color = True)
    else:
        x1, y1, x2, y2 = find_image(image, region, acc=acc)
    mover.move_to((x1 + x2) / 2, (y1 + y2) / 2, duration)
    time.sleep(0.02)
    click()

    info(f"click on {image}")


def dclick_on_image(image: str, region: tuple = SCREEN, duration: float = 0.25, acc: float = 0.8):
    x1, y1, x2, y2 = find_image(image, region, acc=acc)
    mover.move_to((x1 + x2) / 2, (y1 + y2) / 2, duration)
    time.sleep(0.02)
    doubleClick()

    info(f"double click on {image}")



def rclick_on_image(image: str, region: tuple = (0,0,1920,1920), duration: float = 0.25, acc: float = 0.8):
    x1, y1, x2, y2 = find_image(image, region, acc=acc)
    mover.move_to((x1 + x2) / 2, (y1 + y2) / 2, duration)
    time.sleep(0.02)
    rightClick()

    info(f"rclick click on {image}")


def click_here():
    click()
    time.sleep(0.02)
    info(f"click on current coords")


def click_coords(x1,y1,x2,y2, duration: float = 0.25):
    mover.move_to((x1 + x2) / 2, (y1 + y2) / 2, duration)
    time.sleep(0.02)
    click()
    info(f"click on {x1,y1,x2,y2}")

def rclick_coords(x1,y1,x2,y2, duration: float = 0.25):
    mover.move_to((x1 + x2) / 2, (y1 + y2) / 2, duration)
    time.sleep(0.02)
    rightClick()
    info(f"click on {x1,y1,x2,y2}")