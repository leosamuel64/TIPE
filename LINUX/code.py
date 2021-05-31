import math
import time
import sys

sys.path.append('.')

from holobot import Holobot
from collections import deque
import numpy as np
import os

holo = Holobot(sys.argv[1], 115200)

def init():
    holo.reset_yaw()
    holo.calibrate_magneto()
    time.sleep(5)
    print("Init OK")


init()