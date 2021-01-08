from numpy import zeros, array
import time
import numpy as np
import os
import re
#os.chdir('C:\\Users\\chhar_000\\Documents\\etudes\\L2 Cpes\\algorithmiqueinfo\\PROJET S3')


#Matrice statistiques tailles des mots
def longueur(doc_ref):
    stats=27*[0]
    Lmots=doc_ref.read().split('\n')
    for mot in Lmots:
        stats[len(mot)+1]+=1/(len(Lmots))
    return stats

#Matrice de probabilités
def mat_probas(doc_ref, alphabet):
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
    return (mat, somme_tot)

#Matrice de probilité spécifique à la fin des mots (trois dernières lettres)
def mat_proba_fin(doc_ref, alphabet):
    l = doc_ref.read()
    mots = l.split(' ')
    mat_fin = np.zeros(shape=(len(alphabet),len(alphabet)))
    somme_tot_fin = [0]*len(alphabet)
    for ch in l:
        if len(ch) > 5:
            for i in range(-4, -2, 1):
                lettre = ch[i]
                suiv = ch[i+1]
                mat_fin[alphabet.index(lettre), alphabet.index(suiv)] +=1
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            somme_tot_fin[i] += mat_fin[i, j]
        for j in range(len(alphabet)):
            if somme_tot_fin[i] != 0:
                mat_fin[i, j] = (mat_fin[i, j])/somme_tot_fin[i]
    return (mat_fin, somme_tot_fin)

#Outils généraux:
lettres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","é","è","ê","ë","à","â","î","ï","ô","ù","û","ü","æ","œ","ç","\n"]
lettres.sort()
tailles = list(range(1,28))
pas_remplacable = [' ', ',', '.', ';', ':', "'"]

#Creation des matrices de probas enchainements et taille:
start_time = time.time()
ref=open('ref_francais.txt','r',encoding='utf8')
prob = mat_probas(ref, lettres)[0]
somme_tot = mat_probas(ref, lettres)[1]
prob_fin = mat_proba_fin(ref, lettres)[0]
somme_tot_fin = mat_proba_fin(ref, lettres)[1]
for i in range(len(lettres)):
    if somme_tot_fin[i] == 0:
        prob_fin[i] = prob[i]
Lstats= longueur(ref)
ref.close()
print(time.time() - start_time)

#Fonction pour la generation d'un mot charabia de taille donnée:
def genere_charabia1(mat_enchainement, mat_enchainement_fin, alphabet, taille):
    ch = "\n"
    if taille > 3:
        for i in range(taille-3):
            tab = mat_enchainement[alphabet.index(ch[i])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n':
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
        for i in range(3):
            tab = mat_enchainement_fin[alphabet.index(ch[i])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n':
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
    else:
        tab = mat_enchainement[alphabet.index(ch[0])]
        ch += np.random.choice(alphabet, size = None, replace = False, p = tab)
        for i in range(taille-1):
            tab = mat_enchainement_fin[alphabet.index(ch[i])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n':
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
    ch = ch[1:]
    return ch


#Fonction pour la generation de charabia de taille aléatoire, en prenant en compte les probabilités de taille:
def genere_charabia2(mat_enchainement, mat_enchainement_fin, mat_size, alphabet, tailles):
    size = np.random.choice(tailles, size = None, replace = False, p = mat_size)
    ch = "\n"
    if size > 3:
        for i in range(size):
            tab = mat_enchainement[alphabet.index(ch[i])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n':
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
        for i in range(3):
            tab = mat_enchainement_fin[alphabet.index(ch[i])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n':
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
    else:
        tab = mat_enchainement[alphabet.index(ch[0])]
        ch += np.random.choice(alphabet, size = None, replace = False, p = tab)
        for i in range(size-1):
            tab = mat_enchainement_fin[alphabet.index(ch[i])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n':
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
    ch = ch[1:]
    return ch

#Fonction pour la generation de charabia à partir de la première lettre et de taille aléatoire
def genere_charabia3(premiere_lettre, mat_enchainement, mat_enchainement_fin, mat_size, alphabet, tailles):
    size = np.random.choice(tailles, size = None, replace = False, p = mat_size)+1
    ch = premiere_lettre
    if size > 3:
        for i in range(size-3):
            tab = mat_enchainement[alphabet.index(ch[i])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n':
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
        for i in range(3):
            tab = mat_enchainement_fin[alphabet.index(ch[i])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n':
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
    else:
        tab = mat_enchainement[alphabet.index(ch[0])]
        ch += np.random.choice(alphabet, size = None, replace = False, p = tab)
        for i in range(size-1):
            tab = mat_enchainement_fin[alphabet.index(ch[i])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter == '\n':
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
    return ch


#Fonction pour la generation de charabia à partir des dernieres lettres:


#Remplacer les mots d'un texte par du charabia:
def main():
    print('Bienvenue au générateur de charabia Chamama \n Quel texte voulez-vous charabier?')
    nom_fichier=str(input('introduire nom_du_fichier.txt:\n'))
    doc=open(nom_fichier, 'r')
    docstr=doc.read()
    Lmots=re.split(r'(\W+)', docstr)
    doc.close()
    print(Lmots)

    print('Choisissez le mode de remplacement des mots:\nPour remplacer aléatoirement, entrez A;\nPour remplacer par taille, entrez T;\nPour remplacer en fonction de la première lettre, entrez P.\n')
    mode=input()
    f=int(input('\nChoisissez la fréquence de remplacement: tous les ? mots : '))
#    i=np.random.randint(f)
    i = f

    Lmots_travail = Lmots[:]
    for mot in Lmots_travail:
        if len(mot) < 3:
            mot = "0"

    while i < len(Lmots):
        a_remplacer = Lmots[i]
        while Lmots_travail[i] == "0":
            i += 1
        if mode == 'T':
            Lmots[i] = genere_charabia1(prob, prob_fin, lettres, len(a_remplacer))
        elif mode == 'A':
            Lmots[i] = genere_charabia2(prob, prob_fin, Lstats, lettres, tailles)
        elif mode == 'P':
            Lmots[i] = genere_charabia3(a_remplacer[0], prob, prob_fin, Lstats, lettres, tailles)
        i+=f

    charabia=open('charabia.txt','w')
    charabia.write('\n \n')
    charabia.write(' '.join(Lmots))
    charabia.close()

main()
