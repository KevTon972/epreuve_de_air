#!/usr/bin/env python3
#Créez un programme qui décale tous les éléments d’un tableau vers la gauche. Le premier élément devient le dernier à chaque rotation.

import sys 
import re

def rotation(array):
    liste = []

    for i in array:
        i= re.sub('\W', '', i)                                                              # retirer les guillemets des elements et les ajouter a une autre liste
        liste.append(i)

    for j in range(len(liste)):

        liste[j], liste[j+1], liste[j+2], liste[+3] = liste[j+1], liste[j+2], liste[j+3], liste[j]     #décale tous les éléments vers la gauche
        print(", ".join(liste))
        break

arg = sys.argv[1:]

if len(arg) < 4:
    print("il doit y avoir 4 elements pour ce programme")
    exit()

rotation(arg)