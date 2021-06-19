#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

import 

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