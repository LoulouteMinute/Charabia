lettres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","é","è","ê","ë","à","â","î","ï","ô","ù","û","ü","æ","œ","ç","\n"]

from numpy import zeros, array
import time


def mat_probas(doc_ref, alphabet) :
    matrice = zeros((42,42), float)
    lecture = doc_ref.read()
    nb1 = -1
    for i in alphabet :
        nb1 += 1
        p = lecture.find(i)
        while p != -1 :
            if p == len(lecture)-1 :
                p = -1
                nb2 = alphabet.index("\n")
                matrice[nb1][nb2] += 1
            else :
                position = p
                suivant = lecture[position+1]
                nb2 = alphabet.index(suivant)
                matrice[nb1][nb2] += 1
                p = lecture.find(i, position+1)
    somme_tot = [0]*len(alphabet)
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            somme_tot[i] += matrice[i][j]
        for j in range(len(alphabet)):
            if somme_tot[i] != 0:
                matrice[i][j] = (matrice[i][j])/somme_tot[i]
    return matrice
    

start_time = time.time()
with open('/Users/mathildefamelart/Desktop/liste2.txt', 'r', encoding='utf8') as ref :
    a = mat_probas(ref, lettres)
print(time.time() - start_time)
