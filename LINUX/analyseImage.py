import cv2
import imutils
import os
import time
import heapq
import random
import matplotlib.pyplot as plt
import copy

tailleImage = 300

orangeLower = (5, 140, 185)
orangeUpper = (30, 215, 255)

class Noeud:
	def __init__(self, position:(), parent:()):
		self.position = position
		self.parent = parent
		self.g = 0 # Distance au Noeud de départ
		self.h = 0 # Distance au Noeud de fin
		self.f = 0 # Cout total
	def __eq__(self, other):
		return self.position == other.position
	def __lt__(self, other):
		return self.f < other.f

def add_to_open(listeOuverte, voisin):
  for noeud in listeOuverte:
    if (voisin == noeud and voisin.f >= noeud.f):
      return False
  return True

def Distance_Manhattan(a,b):
	# return abs(a.position[0] - b.position[0]) + abs(a.position[1] - b.position[1])
    return ((b.position[0]-a.position[0])**2 + (b.position[1]-a.position[1])**2)**(1/2)


camera = cv2.VideoCapture(0)


# def make_480p():
#     camera.set(3, 640)
#     camera.set(4, 480)

# make_480p()

def balle(frame):
    x,y=-1,-1
    BALLE = False

    frame = imutils.resize(frame, width=tailleImage)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, orangeLower, orangeUpper)
    #mask = cv2.erode(mask, None, iterations=2)
    #mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            # cv2.circle(mask, (int(x), int(y)), int(radius), (0, 255, 255), 2)

            # u=os.system('clear')
            #print("x = "+str(int(x)))
            #print("y = "+str(int(y)))
            # print("Radius  = "+str(radius))
            pos = (300-int(x))*-1    # position par rapport au centre de l'image x=300
            # print("Pos = "+str(pos))
            BALLE = True
            diametre = radius*2
        else:
            # u=os.system('clear')
            # print("PAS DE BALLE")
            radius = -1
            x = -1
            y = -1
            BALLE = False
    else:
        # u=os.system('clear')
        # print("PAS DE BALLE")
        radius = -1
        x = -1
        y = -1
        BALLE = False

    # cv2.imshow("Frame", frame)
    # cv2.waitKey(1)
    #cv2.imshow("Mask", mask)
    return  BALLE,(x,y),frame,mask
"""
while True:
    (grabbed, frame) = camera.read()

    B,coord,frame,mask = balle(frame)
    B,coord,frame,mask = balle(frame)

    cv2.imshow("Mask", mask)
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)"""

(grabbed, frame) = camera.read()
frame = imutils.resize(frame, width=tailleImage)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, orangeLower, orangeUpper)

def nvmat(n,p):
    """
    Renvoie une matrice de n ligne et p colonne remplie de x
    """
    def nvligne(p,x):
        res=[]
        for i in range(p):
            if i==0 or i==p-1:
                res.append('#')
            else:
                res.append(x)
        return res
    res=[]
    for i in range(n):
        if i == 0 or i==n-1:
            res.append(nvligne(p,'#'))
        else:
            res.append(nvligne(p,'.'))  
    res[1][1]='$'
    res[n-2][p-2]='@'      
    return res

def ajouteBalle(mat,mask,x='#'):
    for i in range(len(mask)):
        for j in range(len(mask[0])):
            if mask[i][j]:
                mat[i][j]=x

def carteFromMatrix(M):
  largeur = len(M[0])
  hauteur = len(M)
  map = {}
  deb,fin = (0,0),(0,0)

  for j in range (hauteur):
    for i in range (largeur):
      map[(i, j)] = M[j][i]
      if M[j][i]=='@':
        deb = (i,j)
      if M[j][i]=='$':
        fin = (i,j)

  return map,deb,fin,largeur,hauteur


def Dijkstra(map, deb, fin):
  # Création des liste ouverte et fermée
  listeOuverte = []
  listeFermée = []
  # Création des noeud de départ
  start_node = Noeud(deb, None)
  goal_node = Noeud(fin, None)
  # On ajoute le noeud de départ dans la liste ouverte
  heapq.heappush(listeOuverte,start_node)

  # On s'arrêtera lorsque la liste ouverte sera vide
  while len(listeOuverte) > 0: 
    # on recupere le meilleur noeud...
    current_node = heapq.heappop(listeOuverte)
    # Et on l'ajoute à la liste fermé
    listeFermée.append(current_node)

    # On verifie si l'on a trouvé l'arrivée
    if current_node == goal_node:
      path = []
      while current_node != start_node:
        path.append(current_node.position)
        current_node = current_node.parent
      # On renvoie le chemin
      return path

    # Sinon on recupere le noeud où l'on se trouve
    (x, y) = current_node.position
    # On liste ces voisins
    Voisins = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    for next in Voisins:
      # On recupere la valeurs de la map (obstacle ou non)
      map_value = map.get(next)
      # Verifie si le noeud est un obstacle
      if(map_value == '#'):
              continue
      # creation du noeud voisin
      voisin = Noeud(next, current_node)
      # On verifie que le voisin n'est pas dans la liste fermée
      if(voisin in listeFermée):
              continue
      # Calcul de l'heuristiques (avec distance de Manhattan ) Distance_Manhattan(voisin,start_node)	Distance_Manhattan(voisin,goal_node)
      voisin.g = Distance_Manhattan(voisin,goal_node)

      voisin.f = voisin.g
      #  On verifie si le voisin est dans la liste ouverte et si il a une plus basse valeur de f
      if(add_to_open(listeOuverte, voisin) == True):
        # On ajoute le voisin dans la liste ouverte
        heapq.heappush(listeOuverte,voisin)

  # Si le chemin n'est pas trouvé, on renvoie None
  return None


def draw_Path_frame(frame,path):
    for i in range(0,len(path)-1):
        x1,y1=path[i]
        x2,y2=path[i+1]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,255))
    return frame

def draw_Path_mask(mask,path):
    for i in path:
        x,y=i
        mask[x][y]=1
    return mask





# ----- Boucle ------                

while True:
    debt=time.time()
    (grabbed, frame) = camera.read()

    B,coord,frame,mask = balle(frame)

    

    mat = nvmat(len(mask),len(mask[0]))
    ajouteBalle(mat,mask)
    map,deb,fin,largeur,hauteur = carteFromMatrix(mat)
    path = Dijkstra(map,deb,fin)

    draw_Path_frame(frame,path)

    fint=time.time()
    # print(fin)
    du=fint-debt
    print(1/du,)

    cv2.imshow("Mask", mask)
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)

    time.sleep(0.1)
          




camera.release()
cv2.destroyAllWindows()