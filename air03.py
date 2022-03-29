#!/usr/bin/env python3
#Créez un programme qui retourne la valeur d’une liste qui n’a pas de paire.

import sys

def trouver_intrus(arg):
    
    for i in arg:
        resultat = arg.count(i)
        
        if resultat == 1:
            print(i)
    

arg = sys.argv[1:]

if len(arg) <= 1:
    print("error.")

trouver_intrus(arg)