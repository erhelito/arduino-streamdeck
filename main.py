#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

import os
import serial
import time

"""
reste à faire :
- couper volume
- couper micro
- volume micro
"""

port = "/dev/ttyACM0"

arduino = serial.Serial(port, timeout = 1)

while True :
    donnees_brutes = str(arduino.readline())
    print(donnees_brutes)
    donnees = donnees_brutes[2:-5]
    print(donnees)

    if len(donnees) > 3 :
        pause = int(donnees[0:1])
        suivant = int(donnees[1:2])
        precedent = int(donnees[2:3])
        volume = int(donnees[3:])
        print(pause, suivant, precedent, volume)

        commande_son = "amixer set Master {0}%".format(volume)
        os.system(commande_son)


        if pause == 1 :
            os.system("pytify -pp")
            time.sleep(1)
            pause = 0
            
        if suivant == 1 :
            os.system("pytify -n")
            time.sleep(1)
            suivant = 0
        
        if precedent == 1 :
            os.system("pytify -p")
            time.sleep(1)
            precedent = 0
