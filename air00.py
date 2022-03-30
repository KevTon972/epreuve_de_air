#!/usr/bin/env python3
#Créez un programme qui découpe une chaîne de caractères en tableau (séparateurs : espaces, tabulations, retours à la ligne).
import sys
import re

def ma_fonction(argu, string_separateur):
    
    liste = []

    for i in argu:

        i = re.sub('\W', '', i)                             #retirer les guillemets de argu
        liste.append(i)

    print(liste[0],liste[1],liste[2], sep = string_separateur)     #printer les elements de la liste separer d'un retour a la ligne        

arg = sys.argv[1:]
separateur = "\n"                                           # separateur = retour a la ligne

ma_fonction(arg, separateur)