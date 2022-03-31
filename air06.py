#!/usr/bin/env python3
#Créez un programme qui supprime d’un tableau tous les éléments qui ne contiennent pas une autre chaîne de caractères.
import sys
import re

def lettre_a_chercher(liste, string):
    
    string = liste[-1][1]
    string_maj = string.upper()
    lste = []

    for i in liste[:-1]:

        i= re.sub('\W', '', i)

        if string not in i and string_maj not in i : lste.append(i)

    print(", ".join(lste)) 

arg = sys.argv[1:]
lettre = arg[-1][1]

if len(arg) <= 1: print("il n'y a pas assez d'element")

lettre_a_chercher(arg, lettre)