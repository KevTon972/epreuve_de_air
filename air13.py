#!/usr/bin/env python3

from genericpath import exists
import subprocess
def rouge(mot):
    mot = '\033[91m'+mot+'\033[0m'
    return mot
    

def vert(mot):
    mot = '\033[92m'+mot+'\033[0m'
    return mot

def air00():

    nbr_ligne = 3
    nbr_sucess = 1

    sortie = subprocess.run(['./air00.py “Bonjour les gars”'], shell = True, capture_output = True).stdout.decode()

    for ligne in sortie.splitlines():

        print(f"air00 ({nbr_sucess}/{nbr_ligne}) : {success}") if ligne == "Bonjour\n" or "les\n" or "gars\n" else print(f"air00 ({nbr_sucess}/{nbr_ligne}) : {failure}")
        nbr_sucess += 1

def air01():

    nbr_ligne = 2
    nbr_sucess = 1

    sortie = subprocess.run(['./air01.py “Crevette magique dans la mer des étoiles” “la”'], shell = True, capture_output = True).stdout.decode()
    
    for ligne in sortie.splitlines():

        print(f"air01 ({nbr_sucess}/{nbr_ligne}) : {success}") if ligne == "Crevette magique dans" or "\smer des étoiles" else print(f"air01 ({nbr_sucess}/{nbr_ligne}) : {failure}")
        nbr_sucess += 1

def air02():

    nbr_ligne = 1
    nbr_sucess = 1

    sortie = subprocess.run(['./air02.py “je” “teste” “des” “trucs” “ “'], shell = True, capture_output = True).stdout.decode()
    
    for ligne in sortie.splitlines():

        print(f"air02 ({nbr_sucess}/{nbr_ligne}) : {success}") if ligne == "je teste des trucs" else print(f"air02 ({nbr_sucess}/{nbr_ligne}) : {failure}")
        

def air03():

    nbr_ligne = 1
    nbr_sucess = 1

    sortie = subprocess.run(['./air03.py 1 2 3 4 5 4 3 2 1'], shell = True, capture_output = True).stdout.decode()
    
    for ligne in sortie.splitlines():

        print(f"air03 ({nbr_sucess}/{nbr_ligne}) : {success}") if ligne == "5" else print(f"air03 ({nbr_sucess}/{nbr_ligne}) : {failure}")

def air04():

    nbr_ligne = 1
    nbr_sucess = 1

    sortie = subprocess.run(['./air04.py “Hello milady,   bien ou quoi ??”'], shell = True, capture_output = True).stdout.decode()
    
    for ligne in sortie.splitlines():
        
        print(f"air04 ({nbr_sucess}/{nbr_ligne}) : {success}") if ligne == "Helo milady, bien ou quoi ?" else print(f"air04 ({nbr_sucess}/{nbr_ligne}) : {failure}")

def air05():

    nbr_ligne = 1
    nbr_sucess = 1

    sortie = subprocess.run(['./air05.py 1 2 3 4 5 “+2”'], shell = True, capture_output = True).stdout.decode()
    
    for ligne in sortie.splitlines():
        
        print(f"air05 ({nbr_sucess}/{nbr_ligne}) : {success}") if ligne == "3 4 5 6 7" else print(f"air05 ({nbr_sucess}/{nbr_ligne}) : {failure}")       

def air06():

    nbr_ligne = 1
    nbr_sucess = 1

    sortie = subprocess.run(['./air06.py “Michel” “Albert” “Thérèse” “Benoit” “t”'], shell = True, capture_output = True).stdout.decode()
    
    for ligne in sortie.splitlines():
        
        print(f"air06 ({nbr_sucess}/{nbr_ligne}) : {success}") if ligne == "Michel" else print(f"air06 ({nbr_sucess}/{nbr_ligne}) : {failure}")

def air07():

    nbr_ligne = 1
    nbr_sucess = 1

    sortie = subprocess.run(['./air07.py 1 3 4 2'], shell = True, capture_output = True).stdout.decode()
    
    for ligne in sortie.splitlines():
        
        print(f"air07 ({nbr_sucess}/{nbr_ligne}) : {success}") if ligne == "1 2 3 4" else print(f"air07 ({nbr_sucess}/{nbr_ligne}) : {failure}")

def air08():

    nbr_ligne = 1
    nbr_sucess = 1

    sortie = subprocess.run(['./air08.py 10 20 30 fusion 15 25 35'], shell = True, capture_output = True).stdout.decode()
    
    for ligne in sortie.splitlines():
        
        print(f"air08 ({nbr_sucess}/{nbr_ligne}) : {success}") if ligne == "10 15 20 25 30 35" else print(f"air08 ({nbr_sucess}/{nbr_ligne}) : {failure}")

def air09():

    nbr_ligne = 1
    nbr_sucess = 1

    sortie = subprocess.run(['./air09.py “Michel” “Albert” “Thérèse” “Benoit”'], shell = True, capture_output = True).stdout.decode()
    
    for ligne in sortie.splitlines():
        
        print(f"air09 ({nbr_sucess}/{nbr_ligne}) : {success}") if ligne == "Albert, Thérèse, Benoit, Michel" else print(f"air09 ({nbr_sucess}/{nbr_ligne}) : {failure}")

def air10():

    nbr_ligne = 1
    nbr_sucess = 1

    sortie = subprocess.run(['./air10.py a.txt'], shell = True, capture_output = True).stdout.decode()
    
    for ligne in sortie.splitlines():
        
        print(f"air10 ({nbr_sucess}/{nbr_ligne}) : {success}") if ligne == "Je danse le mia" else print(f"air10 ({nbr_sucess}/{nbr_ligne}) : {failure}")

def air11():

    nbr_ligne = 5
    nbr_sucess = 1

    sortie = subprocess.run(['./air11.py O 5'], shell = True, capture_output = True).stdout.decode()
    
    for ligne in sortie.splitlines():
        
        print(f"air11 ({nbr_sucess}/{nbr_ligne}) : {success}") if ligne == "0" or " 00\n" or "  000\n" or "   0000\n" or "    00000\n" else print(f"air11 ({nbr_sucess}/{nbr_ligne}) : {failure}")
        nbr_sucess += 1

def air12():

    nbr_ligne = 1
    nbr_sucess= 1

    sortie = subprocess.run('./air12.py 6 5 4 3 2 1', shell = True, capture_output = True).stdout.decode()
    
    for ligne in sortie.splitlines():
        
        print(f"air12 ({nbr_sucess}/{nbr_ligne}) : {success}") if ligne == "['1', '2', '3', '4', '5', '6']" else print(f"air12 ({nbr_sucess}/{nbr_ligne}) : {failure}")

failure = rouge("failure")
success = vert("success")
meta_exo = air00(), air01(), air02(),air03(), air04(), air05(), air06(), air07(), air08(), air09(), air10(), air11(), air12()