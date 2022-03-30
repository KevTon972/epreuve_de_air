#!/usr/bin/env python3
#Créez un programme qui découpe une chaîne de caractères en tableau en fonction du séparateur donné en 2e argument.
import sys
import re

def ma_fonction(argu, separateur):
    try:
        liste = []
        argu2 = argu[0:-1]
        separateur= re.sub('\W', '', argu[-1])  #retirer les guillemets du separateur

        for i in argu2:
            i = re.sub('\W', '', i)             #retirer les guillemets des elements de argu2
            liste.append(i)

        indx = liste.index(separateur)


        print(" ".join(liste[0:indx]))
        print(" " + " ".join(liste[indx+1:]))
    except:
        print("error")

arg = sys.argv[1:]

ma_fonction(arg, arg[-1])