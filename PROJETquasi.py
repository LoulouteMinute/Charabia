from numpy import zeros, array
import time
import numpy as np
import string
import re
import os
os.chdir('/Users/marilou/Documents/dev/ProjetAlgoL2')


#Matrice statistiques tailles des mots
def longueur(doc_ref):
    stats = 27*[0]
    Lmots = re.split(r'(\W+)', doc_ref)
    for mot in Lmots:
        stats[len(mot)+1] += 1/(len(Lmots))
        if len(mot) > 30:
            print(mot)
    return stats

#Matrice de probabilités
def mat_probas(doc_ref, alphabet):
    mat = np.zeros(shape=(len(alphabet),len(alphabet)))
    somme_tot = [0]*len(alphabet)
    for i in range(len(doc_ref)-1):
        lettre = doc_ref[i]
        suiv = doc_ref[i+1]
        if lettre in alphabet and suiv in alphabet:
            mat[alphabet.index(lettre), alphabet.index(suiv)] += 1
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            somme_tot[i] += mat[i, j]
        for j in range(len(alphabet)):
            if somme_tot[i] != 0:
                mat[i, j] = (mat[i, j])/somme_tot[i]
    return (mat, somme_tot)

#Matrice de probilité spécifique à la fin des mots (trois dernières lettres)
def mat_proba_fin(doc_ref, alphabet):
    mots = doc_ref.split(' ')
    mat_fin = np.zeros(shape=(len(alphabet),len(alphabet)))
    somme_tot_fin = [0]*len(alphabet)
    for ch in doc_ref:
        if len(ch) > 5:
            for i in range(-4, -2, 1):
                lettre = ch[i]
                suiv = ch[i+1]
                if lettre in alphabet and suiv in alphabet:
                    mat_fin[alphabet.index(lettre), alphabet.index(suiv)] += 1
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            somme_tot_fin[i] += mat_fin[i, j]
        for j in range(len(alphabet)):
            if somme_tot_fin[i] != 0:
                mat_fin[i, j] = (mat_fin[i, j])/somme_tot_fin[i]
    return (mat_fin, somme_tot_fin)

#traitement du texte de reference
def traitement(reference):
    texte = reference.read()
    tab = re.split(r'\W+', texte)
    ponctuation = list(range(33, 41)) + list(range(91, 61)) + list(range(123, 127))
    majuscules = list(range(65, 91))
    for i in range(len(tab)):
        if len(tab[i]) > 1  and ord(tab[i][0]) in majuscules:
            tab[i][0].lower()
    texte = ' '.join(tab)
    #texte = texte.replace('   ', ' ')
    #texte = texte.replace('  ', ' ')
    return texte

#Fonction pour la generation d'un mot charabia de taille donnée:
def genere_charabia1(mat_enchainement, mat_enchainement_fin, alphabet, taille):
    ch = "  "
    if taille > 3:
        for i in range(taille-3):
            tab = mat_enchainement[alphabet.index(ch[-1])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n' or new_letter == ' ' or (new_letter == ch[-2] and new_letter == ch[-1]):
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
        for i in range(3):
            tab = mat_enchainement_fin[alphabet.index(ch[-1])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n' or new_letter == ' ' or (new_letter == ch[-2] and new_letter == ch[-1]):
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
    else:
        for i in range(taille):
            tab = mat_enchainement_fin[alphabet.index(ch[-1])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n' or new_letter == ' ' or (new_letter == ch[-2] and new_letter == ch[-1]):
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
    ch = ch[2:]
    #on ne veut pas de mots qui commencent par deux fois la meme lettre
    while ch[0] == ch[1]:
        tab = mat_enchainement[alphabet.index(ch[0])]
        new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
        ch = ch[0]+new_letter+ch[2:]
    #on ne veut pas d'enchainements de plus de 3 consonnes
    if len(ch)<=3:
        if len(re.findall('[aeiouy]+',ch)) == 0:
            i=np.random.randint(0,len(ch))
            voyelle=np.random.choice(['a','e','i','o','u','y'])
            ch=ch[:i]+voyelle+ch[i+1:]
    else:
        l = 0
        while l < len(ch):
            if len(re.findall('[aeiouy]+',ch[l:l+4])) == 0:
                voyelle=np.random.choice(['a','e','i','o','u','y'])
                ch=ch[:l+3]+voyelle+ch[l+4:]
            l += 3
    return ch


#Fonction pour la generation de charabia de taille aléatoire, en prenant en compte les probabilités de taille:
def genere_charabia2(mat_enchainement, mat_enchainement_fin, mat_size, alphabet, tailles):
    size = np.random.choice(tailles, size = None, replace = False, p = mat_size)
    ch = "  "
    if size > 3:
        for i in range(size):
            tab = mat_enchainement[alphabet.index(ch[i])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n' or new_letter == ' ' or (new_letter == ch[-2] and new_letter == ch[-1]):
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
        for i in range(3):
            tab = mat_enchainement_fin[alphabet.index(ch[-1])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n' or new_letter == ' ' or (new_letter == ch[-2] and new_letter == ch[-1]):
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
    else:
        for i in range(size):
            tab = mat_enchainement_fin[alphabet.index(ch[-1])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n' or new_letter == ' ' or (new_letter == ch[-2] and new_letter == ch[-1]):
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
    if len(re.findall('[aeiouy]+',ch)) == 0:
        i = np.random.randint(0,len(ch))
        ch = ch[:i] + np.random.choice(['a','e','i','o','u','y']) + ch[i + 1:]
    ch = ch[2:]
    return ch

#Fonction pour la generation de charabia à partir de la première lettre et de taille aléatoire
def genere_charabia3(premiere_lettre, mat_enchainement, mat_enchainement_fin, mat_size, alphabet, tailles):
    size = np.random.choice(tailles, size = None, replace = False, p = mat_size) + 1
    if premiere_lettre in string.ascii_lowercase:
        ch = premiere_lettre
        if size > 3:
            for i in range(size-4):
                tab = mat_enchainement[alphabet.index(ch[i])]
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
                while new_letter == '\n' or new_letter == ' ':
                    new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
                ch += new_letter
            for i in range(3):
                tab = mat_enchainement_fin[alphabet.index(ch[-1])]
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
                while new_letter == '\n' or new_letter == ' ':  #or (new_letter == ch[-2] and new_letter == ch[-1]):
                    new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
                ch += new_letter
        else:
            tab = mat_enchainement_fin[alphabet.index(ch[-1])]
            for i in range(size-1):
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
                while new_letter == '\n' or new_letter == ' ':
                    new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
                ch += new_letter
            while ch[0] ==  ch[1] or ch[1] == ch[2]:
                ch[1] = np.random.choice(alphabet, size = None, replace = False, p = tab)
        return ch
    elif premiere_lettre in string.ascii_uppercase:
        ch = premiere_lettre.lower()
        if size > 3:
            for i in range(size-4):
                tab = mat_enchainement[alphabet.index(ch[i])]
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
                while new_letter == '\n' or new_letter == ' ':
                    new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
                ch += new_letter
            for i in range(3):
                tab = mat_enchainement_fin[alphabet.index(ch[-1])]
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
                while new_letter == '\n' or new_letter == ' ': # or (new_letter == ch[-2] and new_letter == ch[-1]):
                    new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
                ch += new_letter
        else:
            for i in range(size-1):
                tab = mat_enchainement_fin[alphabet.index(ch[-1])]
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
                while new_letter == '\n' or new_letter == ' ': # or (new_letter == ch[-2] and new_letter == ch[-1]):
                    new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
                ch += new_letter
        return ch.capitalize()


#Remplacer les mots d'un texte par du charabia:
def main():

    #Outils généraux:
    alphabet_fr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","é","è","ê","ë","à","â","î","ï","ô","ù","û","ü","æ","œ","ç","\n", " "]
    alphabet_esp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ñ", "á", "é", "í", "ó", "ú", "ü", "\n", " "]
    alphabet_angl = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "\n", " "]
    alphabet_lat = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "\n", " ", "æ", "œ"]

    print('\n\nBienvenue au générateur de charabia Chamama ? Dans quelle langue voulez-vous charabier votre texte ? Taper le chiffre correspondant :\n1) Français\n2) Espagnol\n3) Anglais\n4) Latin ?\n')
    langue = int(input())
    if langue == 1:
        lettres = alphabet_fr
        document = 'ref_francais.txt'
    elif langue == 2:
        lettres = alphabet_esp
        document = 'ref_esp.txt'
    elif langue == 3:
        lettres = alphabet_angl
        document = 'ref_angl.txt'
    elif langue == 4:
        lettres = alphabet_lat
        document = 'ref_latin.txt'
    lettres.sort()
    tailles = list(range(1,28))

    #traitement texte de reference pour les matrices
    with open(document, 'r') as texte_ref:
        ref = traitement(texte_ref)
    #texte_ref.close()

    #start_time = time.time()
    #Creation des matrices de probas:

    #matrice d'enchainement
    prob = mat_probas(ref, lettres)[0]

    #matrice de d'enchainement spécifique aux fins de mots
    somme_tot = mat_probas(ref, lettres)[1]
    prob_fin = mat_proba_fin(ref, lettres)[0]
    somme_tot_fin = mat_proba_fin(ref, lettres)[1]
    for i in range(len(lettres)):
        if somme_tot_fin[i] == 0:
            prob_fin[i] = prob[i]

    #matrice de tailles des mots:
    Lstats = longueur(ref)

    #print("Temps d'exécution :", time.time() - start_time)

    nom_fichier = str(input('introduire nom_du_fichier.txt:\n'))
    doc = open(nom_fichier, 'r', encoding='utf8')
    docstr = doc.read()
    Lmots = re.split(r'(\W+)', docstr)
    doc.close()

    print('\nChoisissez le mode de remplacement des mots:\nPour remplacer aléatoirement, entrez A;\nPour remplacer par taille, entrez T;\nPour remplacer en fonction de la première lettre, entrez P\n')
    mode = input()
    f = int(input('\nChoisissez la fréquence de remplacement: tous les ? mots : '))
    i = np.random.randint(f)

    while i<len(Lmots):
        #on ne remplace pas les mots de moins de quatre lettres
        if len(Lmots[i]) <= 3:
            i += 1
        else:
            a_remplacer = Lmots[i]
            if mode == 'T':
                Lmots[i] = genere_charabia1(prob, prob_fin,lettres,len(a_remplacer))
            elif mode == 'A':
                Lmots[i] = genere_charabia2(prob, prob_fin, Lstats, lettres, tailles)
            elif mode == 'P':
                Lmots[i] = genere_charabia3(a_remplacer[0], prob, prob_fin, Lstats, lettres, tailles)
            if a_remplacer[0] in string.ascii_uppercase : #Cas ou le mot a remplacer porte une majuscule
                Lmots[i] = Lmots[i].capitalize()
        i += 2*f

    charabia = open('charabia.txt','w')
    charabia.write(''.join(Lmots))
    charabia.close()

main()
