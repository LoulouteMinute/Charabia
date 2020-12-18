from numpy import zeros, array
import time
import numpy as np
import os
os.chdir('C:\\Users\\chhar_000\\Documents\\etudes\\L2 Cpes\\algorithmiqueinfo\\PROJET S3')


#Matrice statistiques tailles des mots
def longueur(doc_ref):
    stats=27*[0]
    Lmots=doc_ref.read().split('\n')
    for mot in Lmots:
        stats[len(mot)+1]+=1/(len(Lmots))
    return stats

#Matrice de probabilités
def mat_probas(doc_ref, alphabet):
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

#Outils généraux:
lettres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","é","è","ê","ë","à","â","î","ï","ô","ù","û","ü","æ","œ","ç","\n"]
lettres.sort()
tailles=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

#Creation des matrices de probas enchainements et taille:
start_time = time.time()
ref=open('Mots.txt','r')
prob = mat_probas(ref, lettres)
Lstats= longueur(ref)
ref.close()
print(time.time() - start_time)

#Fonction pour la generation d'un mot charabia de taille donnée:
def genere_charabia1(mat_enchainement, alphabet, taille):
    ch = "\n"
    for i in range(taille):
        tab = mat_enchainement[alphabet.index(ch[i])]
        new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
        ch += new_letter
    ch = ch[1:]
    return ch


#Fonction pour la generation de charabia de taille aléatoire, en prenant en compte les probabilités de taille:
def genere_charabia2(mat_enchainement, mat_size, alphabet, tailles):
    size = np.random.choice(tailles, size = None, replace = False, p = mat_size)
    ch = "\n"
    for i in range(size):
        tab = mat_enchainement[alphabet.index(ch[i])]
        new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
        ch += new_letter
    ch = ch[1:]
    return ch

#Fonction pour la generation de charabia à partir de la première lettre et de taille aléatoire
def genere_charabia3(premiere_lettre, mat_enchainement, mat_size, alphabet, tailles):
    size = np.random.choice(tailles, size = None, replace = False, p = mat_size)+1
    ch = premiere_lettre
    for i in range(size):
        tab = mat_enchainement[alphabet.index(ch[i])]
        new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
        ch += new_letter
    return ch

#Fonction pour la generation de charabia à partir des dernieres lettres:


#Remplacer les mots d'un texte par du charabia:
print('Bienvenu au générateur de charabia Chamama (mdr jsp)\n Quel texte voulez-vous charabier?')
nom_fichier=str(input('introduire nom_du_fichier.txt:\n'))
doc=open(nom_fichier, 'r')
Lmots=doc.read().split(' ')
print(Lmots)
doc.close()

print('Choisissez le mode de remplacement des mots:\nPour remplacer aléatoirement, entrez A;\nPour remplacer par taille, entrez T;\nPour remplacer en fonction de la première lettre, entrez P.\n')
mode=input()
f=int(input('\nChoisissez la fréquence de remplacement: tous les ? mots : '))
i=np.random.randint(f)

while i<len(Lmots):
    a_remplacer=Lmots[i]
    if mode=='T':
        Lmots[i]=genere_charabia1(prob,lettres,len(a_remplacer))
    elif mode=='A':
        Lmots[i]=genere_charabia2(prob,Lstats,lettres,tailles)
    elif mode=='P':
        Lmots[i]=genere_charabia3(a_remplacer[0],prob,Lstats,lettres,tailles)
    i+=f

charabia=open('charabia.txt','w')
charabia.write('\n \n')
charabia.write(' '.join(Lmots))
charabia.close()
