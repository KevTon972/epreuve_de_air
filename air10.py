#!/usr/bin/env python3
#Créez un programme qui affiche le contenu d’un fichier donné en argument.
import sys

arg = sys.argv[1]

def open_file(fichier):
    try:
        file = open(fichier, "r")
        ligne = file.readline()

        print(ligne)
    except:
        print("error.")


arg = sys.argv[1]

open_file(arg)
