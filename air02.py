#!/usr/bin/env python3
#Créez un programme qui transforme un tableau de chaînes de caractères en une seule chaîne de caractères. Espacés d’un séparateur donné en dernier argument au programme.
import sys
import re

def my_fonction(arg):
    try:
        arg2 = re.sub('\W', '', arg[-2]) + re.sub('\W', '', arg[-1])
        arg = arg[:-2]
        liste = []

        for i in arg:
            i = re.sub('\W', '', i) 
            liste.append(i)


        print(liste[0],arg2,liste[1],arg2,liste[2],arg2,liste[3])
    except:
        print("error.")

arg = sys.argv[1:]
my_fonction(arg)