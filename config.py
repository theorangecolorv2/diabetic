import os

SCREEN = (0, 0, 1920, 1080)
TARGETS_REGION = (340,801,934,120)

LOGS_DIR = os.path.join(os.path.abspath('./logs'), "logs")  # Adjusted to point directly to logs directory
LOG_FILE = "logs.log"
LOGS_PATH = os.path.join(LOGS_DIR, LOG_FILE)

GLOBAL_ASSETS = os.path.abspath(r'C:\Users\theorr\PycharmProjects\diabolic\global_assets') + "\\"

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)
