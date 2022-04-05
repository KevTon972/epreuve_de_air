#!/usr/bin/env python3
#Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri rapide (QuickSort).
import sys
import random

def quick_sort(argu):

    if len(argu) <= 1:
        return argu

    pivot = random.choice(argu)                                       # prendre un chiffre au hasard dans argu comme pivot
    petite_lst = []
    grande_lst = []
    
    
    for i in argu:
        petite_lst.append(i) if i < pivot else grande_lst.append(i)   # si i est plus petit que le pivot mettre dans la petite liste sinon dans la grande

    
    return quick_sort(petite_lst) + quick_sort(grande_lst)             # appliquer la fonction sur la petite liste et la grande pour pouvoir les triées



arg = sys.argv[1:]

if len(arg) <= 1 : print("il n'ya pas assez d'element pour le tri")

print(quick_sort(arg))