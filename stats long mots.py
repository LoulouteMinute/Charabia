##Projet algo

import os
os.chdir('C:\\Users\\chhar_000\\Documents\\etudes\\L2 Cpes\\algorithmiqueinfo\\PROJET S3')
#os.chdir(input('write working directory adress: ')

#Stats longueur des mots
def longueur(doc):
    stats=27*[0]
    Lmots=doc.read().split('\n')
    for mot in Lmots:
        stats[len(mot)+1]+=1/(len(Lmots))
    return stats

#algo:
doc=open('Mots.txt','r')
Lstats=longueur(doc)
doc.close()
#print(Lstats)
tailles=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

import numpy as np
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p"]

def genere(taille_mot):
    mot = ""
    for i in range(taille_mot):
        nouv_lettre= np.random.choice(alphabet)
        mot+= nouv_lettre
    return mot


for i in range(int(input('nb de mots charabia: '))):
    taille_mot=np.random.choice(tailles, size=None, replace=False, p=Lstats)
    print(genere(taille_mot))
