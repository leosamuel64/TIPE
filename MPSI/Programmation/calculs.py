import matplotlib.pyplot as plt
from math import *

gamma = 7/5     # On suppose que l'air est un gaz diatomique N_2
f = 40000       # En Hz
d = 0.2         # En m
rho = 1.225     # masse volumique de l'air (En kg.m^{-3})
g = 9.81        # En m.s^{-2}

def calcul_pression(gamma,f,d,k,rho):
    """
    Entrée :    - gamma : Coefficient isentroprique du fluide
                - f : Fréquence de l'onde
                - d : Distance entre les deux sources
                - k : entier positif (mode propre)
                - rho : masse volumique du fluide

    Sortie :    - Renvoie la difference de pression par rapport à la pression a l'equilibre
    """
    return (((d/k)**2)*(f**2)*rho)/(gamma)



def trace_pression(k):
    """
    Trace la pression en fonction de la valeur des modes propres jusqu'au mode k
    """
    P=[]
    M=[]
    for i in range (1,k):
        M.append(i)
        P.append(calcul_pression(gamma,f,d,i,rho))
    
    plt.plot(M,P,label="P = f(k)")
    plt.legend()
    plt.show()

def calcul_force(k,r):
    """
    Renvoie la norme de la force appliquée sur le bas d'un sphere de rayon r
    """
    return calcul_pression(gamma,f,d,k,rho)*(2*pi*r**2)

def trace_force(k,r):
    M=[]
    F=[]
    Fg=[]
    for i in range (1,k):
        M.append(i)
        F.append(calcul_force(i,r))
        # Fg.append((calcul_force(i,r)-g)/g)
    plt.plot(M,F,label="F=f(k")
    # plt.plot(M,Fg,label="Masse maximale à léviter")
    plt.legend()
    plt.show()

#trace_pression(20)
trace_force(20,0.001)


    

