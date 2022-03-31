#!/usr/bin/env python3
#Créez un programme qui ajoute à une liste d’entiers triée un nouvel entier tout en gardant la liste triée dans l’ordre croissant. Le dernier argument est l’élément à ajouter.

import sys
import string

def tri(liste_triee, entier):
        
    lste = []

    [lste.append(i) for i in liste_triee]
    
    lste.append(entier)
    lst_final = sorted(lste)
    
    print(" ".join(lst_final))

arg = sys.argv[1:]
array = arg[:-1]
new_element = arg[-1]
alpha = string.ascii_lowercase

if new_element in alpha:
    print("le dernier argument n'est pas un nombre")
    exit()

tri(array, new_element)
