#!/usr/bin/env python3
#Créez un programme qui transforme un tableau de chaînes de caractères en une seule chaîne de caractères. Espacés d’un séparateur donné en dernier argument au programme.
import sys
import re

def my_fonction(argu, string_separateur):
    try:
        string_separateur = re.sub('\W', '', argu[-2]) + re.sub('\W', '', argu[-1])                     # retirer les guillemets pour recuperer "espace"
        argu = argu[:-2]
        liste = []

        for i in argu:
            i = re.sub('\W', '', i)                                                                     # retirer les guillemets de argu
            liste.append(i)


        print(liste[0]+string_separateur,liste[1]+string_separateur,liste[2]+string_separateur,liste[3])# concatener les elements de la liste avec "l'espace"
    except:
        print("ajouter un separateur")

arg = sys.argv[1:]
separateur = arg[-2:]

my_fonction(arg, separateur)