#!/usr/bin/env python3
#Afficher un escalier constitué d’un caractère et d’un nombre d’étages donné en paramètre.

import sys 
import string

def pyramide(argu):

    try:

        symbol = argu[0]
        longeur = int(argu[1])

        for i in range(longeur):

            print(" " * (longeur-i) + symbol)   

            symbol += "00"                      # a chaque rotation on ajoute 2 "0"

    except ValueError:
        print("le 2e argument doit etre un nombre")


arg = sys.argv[1:]

if len(arg) < 2 or len(arg) > 2:
    print("il doit y avoir 2 arguments")
    exit()

pyramide(arg)