# sudo usermod -a -G plugdev $USER
# sudo usermod -a -G dialout $USER
# sudo cp scripts/45-holobot.rules /etc/udev/rules.d/
# sudo service udev restart
#   [or, depending on the distribution linux]	 
# sudo restart udev

# mettre prog.py dans /holobot/
# cd MetabotAPI/python/build
# python3 ../holobot/prog.py <serial port:/dev/rfcomm0>


import math
import time
import sys
from holobot import Holobot
from collections import deque
import numpy as np
import imutils
import cv2
import os


def init():
	try:
		holo = Holobot(sys.argv[1], 115200)
		holo.reset_yaw()
		holo.calibrate_magneto()
		return holo
	except:
		raise Exception("Erreur lors de initialisation")

holo = init()
	

def deplacement(angle,vitesse):
	"""
	angle : ° (par rapport à un axe vertical)
	vitesse : mm/s
	"""
	holo.move_toward(vitesse, angle)


