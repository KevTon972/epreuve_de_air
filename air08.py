#!/usr/bin/env python3
#Créez un programme qui fusionne deux listes d’entiers triées en les gardant triées, les deux listes seront séparées par un “fusion”.

import sys

def fusion(array1, array2):
    
    liste = []

    [liste.append(i) for i in array1]
    [liste.append(j) for j in array2]

    liste_triee = sorted(liste)

    print(" ".join(liste_triee))

arg = sys.argv[1:]
separateur = arg.index("fusion")
lst1 = arg[:separateur]
lst2 = arg[separateur+1:]


fusion(lst1, lst2)