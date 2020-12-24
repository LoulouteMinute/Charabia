import numpy as np
import time
import pdb

def mat_proba_1(doc_ref, alphabet):
    l = doc_ref.read()
    mat = np.zeros(shape=(len(alphabet),len(alphabet)))
    somme_tot = [0]*len(alphabet)
    for i in range(len(l)-1):
        lettre = l[i]
        suiv = l[i+1]
        if lettre in alphabet and suiv in alphabet :
            mat[alphabet.index(lettre), alphabet.index(suiv)] += 1
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            somme_tot[i] += mat[i, j]
        for j in range(len(alphabet)):
            if somme_tot[i] != 0:
                mat[i, j] = (mat[i, j])/somme_tot[i]
    return mat

def mat_proba_fin(doc_ref, alphabet):
    l = doc_ref.readlines()
#    mots = l.split(' ')
    mat = np.zeros(shape=(len(alphabet),len(alphabet)))
    somme_tot = [0]*len(alphabet)
    for ch in l:
        if len(ch) > 5:
            for i in range(-4, -2, 1):
                lettre = ch[i]
                suiv = ch[i+1]
                mat[alphabet.index(lettre), alphabet.index(suiv)] +=1
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            somme_tot[i] += mat[i, j]
        for j in range(len(alphabet)):
            if somme_tot[i] != 0:
                mat[i, j] = (mat[i, j])/somme_tot[i]
    return mat


def mat_proba_2(doc_ref, alphabet):
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
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            if somme_ench[i] != 0:
                mat[i, j] = (mat[i, j])/somme_ench[i]
    return mat

def mat_proba_3(doc_ref, alphabet):
    mat = np.zeros(shape = (len(alphabet), len(alphabet)))
    lecture = doc_ref.read()
    nb1 = -1
    somme_tot = [0]*(len(alphabet))
    for i in alphabet :
        nb1 += 1
        p = lecture.find(i)
        while p != -1:
            if p == len(lecture)-1:
                p = -1
                nb2 = alphabet.index('\n')
                mat[nb1][nb2] += 1
            else:
                position = p
                suivant = lecture[position+1]
                nb2 = alphabet.index(suivant)
                mat[nb1][nb2] += 1
                p = lecture.find(i, position+1)
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            somme_tot[i] += mat[i][j]
        for j in range(len(alphabet)):
            if somme_tot[i] != 0:
                mat[i][j] = (mat[i][j])/somme_tot[i]
    return mat



def main():
    lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'à', 'â', 'é', 'è', 'ê', 'ë', 'ç', 'ï', 'î', 'ô', 'ù', 'û', 'ü', 'æ', 'œ', '\n']
    lettres.sort()
    start_time_a = time.time()
    with open('/Users/marilou/Documents/dev/ProjetAlgoL2/liste_mots.txt', 'r') as ref:
        a = mat_proba_fin(ref, lettres)
    print('Temps :', time.time() - start_time_a, 'secondes')


#    start_time_b = time.time()
#    with open('/Users/marilou/Documents/dev/ProjetAlgoL2/liste_mots.txt', 'r') as ref:
#        b = mat_proba_3(ref, lettres)
#    print('Temps pour matrice Mathilde:', time.time() - start_time_b, "secondes")

#    for i in range(42):
#        for j in range(42):
#            if a[i, j] == b[i, j]:
#                print(lettres[i], lettres[j], 'True')
#            else:
#                print(lettres[i], lettres[j], 'False')

    somme = [0]*42
    total = 0
    print("valeurs des sommes")
    for i in range(42):
        for j in range(42):
            somme[i] += a[i, j]
            print(lettres[i], lettres[j], a[i, j])
        total += somme[i]
    print(somme)
    print("le total vaut:", total)

main()
