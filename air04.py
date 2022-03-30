#!/usr/bin/env python3
#Créez un programme qui affiche une chaîne de caractères en évitant les caractères identiques adjacents.

import sys
import re

#trouver les guillemets et les supprimer
def retirer_guillemet(argu):
    liste = []

    for i in argu:
        lst = list(i)

        for j in lst:
            if j == argu[-1][-1] or j == argu[0][0]:
                lst.remove(j)

        lst = "".join(lst)    
        liste.append(lst)
    return liste

#retirer les doublon
def no_doublon(argu):
    
    liste2 = []
    for k in argu:

        new_lst = list(k)

        for l in new_lst:  
            resultat = new_lst.count(l)

            if resultat == 2:
                new_lst.remove(l)

        new_lst = "".join(new_lst)       
        liste2.append(new_lst)

        print(new_lst, end=" ")

arg = sys.argv[1:]
x = retirer_guillemet(arg)
no_doublon(x)          


            
            