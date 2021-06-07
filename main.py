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
- améliorer la liaison série (dans le programme arduino)
"""

port = "/dev/ttyACM0"

connection = False

def recup_et_nettoyage_donnees() :
    donnees_brutes = str(arduino.readline())
    print(donnees_brutes)
    donnees = donnees_brutes[2:-5]
    print(donnees)

    return donnees

def analyse_donnees() :
    pause = int(donnees[0:1])
    suivant = int(donnees[1:2])
    precedent = int(donnees[2:3])
    volume = int(donnees[3:])
    print(pause, suivant, precedent, volume)

    return pause, suivant, precedent, volume

while True :
    while connection == False :
        try :
            arduino = serial.Serial(port, timeout = 1)
            connection == True
        except :
            print("FR : Un problème est survenu lors de la connection avec l'arduino. Si cette erreur apparaît à nouveau, veuillez vérifier le port com renseigné plus haut.")
            print("EN: An error occurred. If it happens again, check the serial port above.")
            connection = False
            
        try :        
            donnees = recup_et_nettoyage_donnees()
        
            if len(donnees) > 3 :
                pause = analyse_donnees()[0]
                suivant = analyse_donnees()[1]
                precedent = analyse_donnees()[2]
                volume = analyse_donnees()[3]

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

        except :
            print("FR : Un problème est survenu, il peut s'agir d'une erreur lors du traitement des données. Si cette erreur apparaît à nouveau, vous pouvez contacter Erhelito (erhelito@yahoo.fr).")
            print("EN: An error occurred. If it happens again, contact Erhelito (erhelito@yahoo.fr).")