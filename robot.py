from holobot import Holobot
import time
import sys
import math
import cv2

holo = Holobot(sys.argv[1], 115200)
camera = cv2.VideoCapture(0)

def deplacement_élémentaire(pos, dest ,poids=30 ,tps=0.1):
    x=dest[0]-pos[0]
    y=dest[1]-pos[1]
    
    holo.control(poids*x,poids*x,0)
    time.sleep(tps)

def deplacement():
    (grabbed, frame) = camera.read()
    B,coord,frame,mask = analyse(frame)
    mat = nvmat(len(mask),len(mask[0]))
    map,deb,fin,largeur,hauteur = carteFromMatrix(mat)
    path = A_étoile(map,deb,fin)
    dest=path[1]
    x=coord[0]
    y=coord[1]
    if x*y>0:
        deplacement(coord, dest)
    


camera.release()





