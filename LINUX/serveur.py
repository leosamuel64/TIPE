import socket
import time
# from holobot import Holobot
import sysconfig

# Indispensable au demmarage.
# holo = Holobot(sys.argv[1], 115200)
# if len(sys.argv) != 2:
#     print ("error: I need the serial port (bluetooth or wired)")
#     sys.exit(0)
# 1C:1B:B5:83:27:F9
def receive(hostMACAddress,port=3):
    """
    Entrée :    - hostMACAddress : (str)     adresse MAC de l'adaptateur du serveur
                - port : (int)              port (indiférent mais doit etre le même que celui du client)                 
    """
    # 3 is an arbitrary choice. However, it must match the port used by the client.
    backlog = 1
    size = 1024
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.bind((hostMACAddress,port))
    s.listen(backlog)
    try:
        client, address = s.accept()
        while 1:
            data = client.recv(size)
            if data:
                print(data)
                client.send(data)
    except:	
        print("Closing socket")	
        client.close()
        s.close()

receive('1c: 1b: b5: 83: 27: f9')

"""
def avancer(robot, distance, angle, vitesse):
    #Constantes :
    dt = 0.1
    t = 0.0

    #Calculs :
    distance = distance*10
    temps = distance/vitesse
    angle = angle - 45

    #Bouger :
    time.sleep(dt)
    while(t < temps):
        robot.move_toward(vitesse, angle)
        time.sleep(dt)
        t += dt

def tourner(vitesse, angleCible) :

    holo.reset_yaw()


    if (abs(angleCible) < 90) :
        correction = 6
    elif abs(angleCible) < 180 :
        correction = 10
    elif angleCible < 270 :
        correction = 6
    elif angleCible < 360 :
        correction = 10
    if angleCible == 180:
        angleCible += 1

    if angleCible < 0 :
        angleCible += 360

    angle = holo.get_yaw()

    while(angle > (angleCible+correction) or angle < (angleCible-correction)) :
        angle = holo.get_yaw()

        if angle < 0 :
            angle += 360


        if angleCible < 180 :
            holo.turn(vitesse)

        elif angleCible > 180 :
            holo.turn(-vitesse)

            """