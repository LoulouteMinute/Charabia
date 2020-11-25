#alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n", "o", "p"]
import numpy as np

#def genere():
#    mot = ""
#    taille_mot = np.random.randint(2, 8)
#    for i in range(taille_mot):
#        proba = np.random.randint(0, len(alphabet))
#        mot += alphabet[proba]
#    return mot


def genere_charabia(mat_enchainement, mat_size, alphabet, tailles):
    size = np.random.choice(tailles, size = None, replace = False, p = mat_size)
    ch = "\n"
    for i in range(size):
        tab = mat_enchainement[alphabet.index(ch[i])]
        new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
        ch += new_letter
    ch = ch[1:]
    return ch
