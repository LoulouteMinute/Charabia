#alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p"]A
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

def mat_proba(doc_ref, alphabet):
    l = doc_ref.read()
    mat = np.zeros(shape=(len(alphabet),len(alphabet)))
    for i in range(len(alphabet)):
        for j in range(len(l)):
            if l[j] == alphabet[i] and j < len(l)-1:
                suiv = l[j+1]
                mat[i, alphabet.index(suiv)] += 1
            else:
                mat[i, len(alphabet) - 1] += 1
    somme_tot = np.sum(mat)
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            if somme_tot != 0:
                mat[i, j] = (mat[i, j])/somme_tot
    return mat

def main():
    lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'à', 'â', 'é', 'è', 'ê', 'ë', 'ç', 'ï', 'î', 'ô', 'ù', 'û', 'ü', 'æ', 'œ', '\n']
    start_time = time.time()
    with open('/Users/marilou/Documents/dev/ProjetAlgoL2/liste_mots.txt', 'r') as ref:
        matrice = mat_proba(ref, lettres)
    print(matrice)
    print(time.time() - start_time, "seconds")
    for i in range(len(lettres)):
        for j in range(len(lettres)):
            print(matrice[i, j])
    sommes = np.sum(matrice, axis = 0)
    total = 0
    print("valeurs des sommes")
    for i in sommes:
        print(i)
        total += i
    print("le total vaut:", total)


main()
