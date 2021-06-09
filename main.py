#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

# importation des modules nécessaires dans ce programme
import os
import serial
import time

"""
reste à faire :
- couper volume
- couper micro
- volume micro
"""
# connection au port série
port = "/dev/ttyACM0"
connection = False

# définition des différentes fonctions
def recup_et_nettoyage_donnees() :
    # récupère les données brutes, les affiche, et supprime les informations inutiles
    donnees_brutes = str(arduino.readline())
    print(donnees_brutes)
    donnees = donnees_brutes[2:-5]
    print(donnees)

    return donnees

def analyse_donnees(donnees) :
    # partitionne les données pour les utiliser dans le programme, et les affiche
    mode = int(donnees[0:1])
    b1 = int(donnees[1:2])
    b2 = int(donnees[2:3])
    b3 = int(donnees[3:4])
    potentiometre = int(donnees[4:7])
    print(mode, b1, b2, b3, potentiometre)

    return mode, b1, b2, b3, potentiometre

def mode1(b1, b2, b3) :
    # cette fonction est celle pour spotify

    # met le volume à la valeur du potentiomètre
    commande_son = "amixer set Master {0}%".format(potentiometre)
    os.system(commande_son)

    # pause/lecture/suivant/precedent en fonction des différentes valeurs des boutons
    if b1 == 1 :
        os.system("pytify -pp")
        time.sleep(1)
        b1 = 0
                
    if b2 == 1 :
        os.system("pytify -n")
        time.sleep(1)
        b2 = 0
                
    if b3 == 1 :
        os.system("pytify -p")
        time.sleep(1)
        b3 = 0

# boucle
while True :
    # connection au port série (uniquement lorsque le port série n'était pas connecté, afin de faire un programme plus léger à executer)
    while connection == False :
        try :
            arduino = serial.Serial(port, timeout = 1)
            connection == True
        except :
            print("FR : Un problème est survenu lors de la connection avec l'arduino. Si cette erreur apparaît à nouveau, veuillez vérifier le port com renseigné plus haut.")
            print("EN: An error occurred. If it happens again, check the serial port above.")
            connection = False
            
    try :
        # récupération de analyse des données
        donnees = recup_et_nettoyage_donnees()

        mode = analyse_donnees(donnees)[0]
        b1 = analyse_donnees(donnees)[1]
        b2 = analyse_donnees(donnees)[2]
        b3 = analyse_donnees(donnees)[3]
        potentiometre = analyse_donnees()[4]

        # appelle la fonction du mode 1 si c'est le mode qui est sélectionné
        if mode == 1 :
            mode1(b1, b2, b3)
            
    except :
        print("FR : Un problème est survenu, il peut s'agir d'une erreur lors du traitement des données. Si cette erreur apparaît à nouveau, vous pouvez contacter Erhelito (erhelito@yahoo.fr).")
        print("EN: An error occurred. If it happens again, contact Erhelito (erhelito@yahoo.fr).")