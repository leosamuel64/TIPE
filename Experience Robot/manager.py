import math


def scalaire(A,B):
	return A[0]*B[0]+A[1]*B[1]

def vecteur(A,B):
	return (B[0]-A[0],B[1]-A[1])


def calcul_Vecteur(robot,balle):
	xr,yr=robot
	xb,yb=balle
	A=(xr,yr+10)
	AB=vecteur(A,robot)
	BC=vecteur(robot,balle)
	cos = (scalaire(AB,BC))/(math.sqrt(scalaire(AB,AB))*math.sqrt(scalaire(BC,BC)))
	if xr>=xb:
		angle=(math.acos(cos)*180)/math.pi+180
	else:
		angle=(math.acos(cos)*180)/math.pi
	
	return angle







	


