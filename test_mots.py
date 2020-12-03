#alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p"]
#import numpy as np

#def genere():
#    mot = ""
#    taille_mot = np.random.randint(2, 8)
#    for i in range(taille_mot):
#        proba = np.random.randint(0, len(alphabet))
#        mot += alphabet[proba]
#    return mot

import numpy as np
import time
import pdb

def mat_proba(doc_ref, alphabet):
    mots = doc_ref.readlines()
    ench = []
    dico = {}
    somme_ench = [0]*(len(alphabet))
    mat = np.zeros(shape = (len(alphabet),len(alphabet)))
    for i in alphabet:
        for j in alphabet:
            clef = i+j
            dico[clef] = 0
    for mot in mots :
        for i in range(len(mot)-1):
            ench.append(mot[i]+mot[i+1])
    ench.sort()
    for clef in dico:
        i = 0
        if ench != [] and ench[i] == clef:
            while ench != [] and ench[i] == clef:
                dico[clef] += 1
                ench.remove(clef)
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            mat[i, j] += dico[alphabet[i]+alphabet[j]]
            somme_ench[i] += mat[i, j]
#            if j == len(alphabet)-1 and somme_ench[i] != 0:
#                mat[i, j] = (mat[i, j])/somme_ench[i]
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            if somme_ench[i] != 0:
                mat[i, j] = (mat[i, j])/somme_ench[i]
    return mat

def main():
    lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'à', 'â', 'é', 'è', 'ê', 'ë', 'ç', 'ï', 'î', 'ô', 'ù', 'û', 'ü', 'æ', 'œ', '\n']
    lettres.sort()
    start_time = time.time()
    with open('/Users/marilou/Documents/dev/ProjetAlgoL2/liste_mots.txt', 'r') as ref:
        matrice = mat_proba(ref, lettres)
    print(time.time() - start_time, "seconds")

    somme = [0]*42
    total = np.sum(matrice)
    print("valeurs des sommes")
    for i in range(42):
        for j in range(42):
            somme[i] += matrice[i, j]
    print(somme)
    print("le total vaut:", total)


main()
