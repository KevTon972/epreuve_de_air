#!/usr/bin/env python3
#Créez un programme qui découpe une chaîne de caractères en tableau en fonction du séparateur donné en 2e argument.
import sys
import re

def ma_fonction(arg):
    try:
        liste = []
        arg2 = arg[0:-1]
        arg= re.sub('[\W]', '', arg[-1]) 

        for i in arg2:
            i = re.sub('[\W]', '', i) 
            liste.append(i)

        indx = liste.index(arg)


        print(" ".join(liste[0:indx]))
        print(" " + " ".join(liste[indx+1:]))
    except:
        print("error")

arg = sys.argv[1:]

ma_fonction(arg)