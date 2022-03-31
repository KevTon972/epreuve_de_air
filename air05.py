#!/usr/bin/env python3
#Créez un programme qui est capable de reconnaître et de faire une opération (addition ou soustraction) sur chaque entier d’une liste.
import sys

def calcul_argu(argu):
    try:
        symbol = "+"
        chiffre = int(argu[-1][2])              # convertir chiffre en int pour pouvoir faire l'operation avec les elements de la liste
        liste = []

        for i in argu[:-1]:
            i = int(i)                          # convertir i en int pouvoir faire l'operation avec "chiffre"
            if argu[-1][1] == symbol:
                i += chiffre                    
                liste.append(str(i))            # reconvertir i en str pour pouvoir joindre les elements de "liste"
            else:
                i -= chiffre
                liste.append(str(i))
        print(" ".join(liste))
    except:
        print("le calcul n'est pas faisable")

arg = sys.argv[1:]

calcul_argu(arg)