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
print(Lstats)

import numpy as np
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p"]

def genere(taille_mot):
    mot = ""
    for i in range(taille_mot):
        proba = np.random.choice()
        mot+= alphabet[proba]
    return mot


for i in range(int(input('nb de mots charabia: '))):
    long=np.random
    print(genere(Lstats.index(np.random.choice(Lstats))))
