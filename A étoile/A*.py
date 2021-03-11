# Implementation des tas mutable en python
import heapq
import random
import time
import matplotlib.pyplot as plt


# initializing list
# li = []


# using heapify to convert list into heap
# heapq.heapify([])
# heapq.heappush(li,4)
# heapq.heappush(li,6)

# heapq.heappush(li,3)


# print(heapq.heappop(li))
# print(heapq.heappop(li))

# print(heapq.heappop(li))









# https://khayyam.developpez.com/articles/algo/astar/



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



def draw_grid(map, largeur, hauteur, spacing=2, **kwargs):
	for y in range(hauteur):
		for x in range(largeur):
						print('%%-%ds' % spacing % draw_tile(map, (x, y), kwargs), end='')
	print()


def draw_tile(map, position, kwargs):
				value = map.get(position)
				if 'path' in kwargs and position in kwargs['path']: value = '+'
				if 'deb' in kwargs and position == kwargs['deb']: value = '@'
				if 'goal' in kwargs and position == kwargs['goal']: value = '$'
				return value

def Distance_Manhattan(a,b):
	return abs(a.position[0] - b.position[0]) + abs(a.position[1] - b.position[1])


def A_étoile(map, deb, fin):
	# Création des liste ouverte et fermée
	listeOuverte = []
	listeFermée = []
	# Création des noeud de départ
	start_node = Noeud(deb, None)
	goal_node = Noeud(fin, None)
	# On ajoute le noeud de départ dans la liste ouverte
	listeOuverte.append(start_node)

	# On s'arrêtera lorsque la liste ouverte sera vide
	while len(listeOuverte) > 0:
		# Sort the listeOuverte list to get the noeud with the lowest cost first
		# On tri la liste ouverte pour avoir le meilleur noeud en premier (celui avec le cout le plus bas)
		listeOuverte.sort()																							# TODO : Utiliser un tas?
		# on recupere le meilleur noeud...
		current_node = listeOuverte.pop(0)
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
			# Calcul de l'heuristiques (avec distance de Manhattan ) d
			voisin.g = abs(voisin.position[0] - start_node.position[0]) + abs(voisin.position[1] - start_node.position[1])
			voisin.h = abs(voisin.position[0] - goal_node.position[0]) + abs(voisin.position[1] - goal_node.position[1])

			voisin.f = voisin.g + voisin.h
			#  On verifie si le voisin est dans la liste ouverte et si il a une plus basse valeur de f
			if(add_to_open(listeOuverte, voisin) == True):
				# On ajoute le voisin dans la liste ouverte
				listeOuverte.append(voisin)
	# Si le chemin n'est pas trouvé, on renvoie None
	return None

def A_étoile_Tas(map, deb, fin):
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
      voisin.h = Distance_Manhattan(voisin,start_node)

      voisin.f = voisin.g + voisin.h
      #  On verifie si le voisin est dans la liste ouverte et si il a une plus basse valeur de f
      if(add_to_open(listeOuverte, voisin) == True):
        # On ajoute le voisin dans la liste ouverte
        heapq.heappush(listeOuverte,voisin)

  # Si le chemin n'est pas trouvé, on renvoie None
  return None

# Verifie si le voisin est dans la liste ouverte et si il a une plus basse valeur de f
def add_to_open(listeOuverte, voisin):
  for noeud in listeOuverte:
    if (voisin == noeud and voisin.f >= noeud.f):
      return False
  return True

def carteFromFile(cheminFichierCarte):
		map = {}
		chars = ['c']
		deb = None
		fin = None
		largeur = 0
		hauteur = 0
		fp = open(cheminFichierCarte, 'r')

		while len(chars) > 0:
						chars = [str(i) for i in fp.readline().strip()]
						largeur = len(chars) if largeur == 0 else largeur
						for x in range(len(chars)):
										map[(x, hauteur)] = chars[x]
										if(chars[x] == '@'):
														deb = (x, hauteur)
										elif(chars[x] == '$'):
														fin = (x, hauteur)
						if(len(chars) > 0):
										hauteur += 1
		fp.close()
		return map,deb,fin,largeur,hauteur

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

def CheminGraphique(init):
				map,deb,fin,largeur,hauteur=init
				path = A_étoile(map, deb, fin)
				print()
				print(path)
				print()
				draw_grid(map, largeur, hauteur, spacing=1, path=path, deb=deb, goal=fin)
				print()
				print('Longueur du chemin: {0}'.format(len(path)))
				print()

def Chemin(init):
  map,deb,fin,largeur,hauteur=init
  path = A_étoile(map, deb, fin)
  return path

def Chemin_Tas(init):
  map,deb,fin,largeur,hauteur=init
  path = A_étoile_Tas(map, deb, fin)
  return path


carteTest = [	['#','#','#','#','#','#','#','#','#'],
								['#','$','.','.','.','.','.','.','#'],
								['#','#','#','#','#','.','#','#','#'],
								['#','.','.','.','.','.','.','@','#'],
								['#','#','#','#','#','#','#','#','#']
						]


# print(Chemin_Tas(carteFromFile('/mnt/c/Users/leosa/Desktop/INFO/TIPE_Chemin/map.txt')))
# print(Chemin_Tas(carteFromMatrix(carteTest)))
# carte('/mnt/c/Users/leosa/Desktop/INFO/TIPE_Chemin/map.txt')

def matriceAléa(n,p):
		res=[]
		ligne0=[]
		lignefinal=[]
		for i in range(n):
				ligne0.append('#')
		res.append(ligne0)
		def nvligne(n):
				res=[]
				for i in range(n):
						if i==0 or i==n-1:
								res.append('#')
						elif random.randint(0,100)>=20:
								res.append('.')
						else:
								res.append('#')
				return res
		for i in range(p-2):
				res.append(nvligne(n))
		for i in range(n):
				lignefinal.append('#')
		res.append(lignefinal)
		res[1][1]='$'
		res[p-2][n-2]='@'
		return res

def chrono(f,g,n):
		m=carteFromMatrix(matriceAléa(n,n))
		debf = time.time()
		f(m)
		finf = time.time()
		debg = time.time()
		g(m)
		fing = time.time()

		return finf-debf,fing-debg



def TestPathFinding(nMax):
		Ltaille = []
		LtempsTas = []
		Ltemps = []
		for i in range(10,nMax):
				print(i)
				Ltaille.append(i)
				ttas,tc = chrono(Chemin_Tas,Chemin,i)

				LtempsTas.append(ttas)

				Ltemps.append(tc)

		plt.plot(Ltaille,LtempsTas,label='Chemin_Tas')

		plt.plot(Ltaille,Ltemps,label='Chemin')

		plt.legend()

		plt.show()

TestPathFinding(100)


