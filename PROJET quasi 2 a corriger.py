from numpy import zeros, array
import time
import numpy as np
import string
import re
import os
os.chdir('C:\\Users\\chhar_000\\Documents\\etudes\\L2 Cpes\\algorithmiqueinfo\\PROJET S3')


#Matrice statistiques tailles des mots
def longueur(doc_ref):
    stats=27*[0]
    docstr=doc_ref.read()
    Lmots=re.split(r'(\W+)', docstr)
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

#Creation des matrices de probas:
start_time = time.time()
#matrice d'enchainement
ref=open('liste2.txt','r',encoding='utf8')
prob = mat_probas(ref, lettres)
ref.close()
#matrice de tailles des mots:
ref=open('liste2.txt','r',encoding='utf8')
Lstats= longueur(ref)
ref.close()

print(time.time() - start_time)
print(prob,'\n',Lstats)


#Fonction pour la generation d'un mot charabia de taille donnée:
def genere_charabia1(mat_enchainement, alphabet, taille):
    ch = "\n\n"
    for i in range(taille):
        tab = mat_enchainement[alphabet.index(ch[-1])]
        new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
        while new_letter=='\n' or (new_letter==ch[-2] and new_letter==ch[-1]):
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
        ch += new_letter
    ch = ch[2:]
    #on ne veut pas de mots qui commencent par deux fois la meme lettre
    while ch[0]==ch[1]:
        tab= mat_enchainement[alphabet.index(ch[0])]
        new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
        ch=ch[0]+new_letter+ch[2:]
    #on ne veut pas d'enchainements de plsu de 3 consonnes
    if len(ch)<=3:
        if len(re.findall('[aeiouy]+',ch))==0:
            i=np.random.randint(0,len(ch))
            voyelle=np.random.choice(['a','e','i','o','u','y'])
            ch=ch[:i]+voyelle+ch[i+1:]
    else:
        l=0
        while l<len(ch):
            if len(re.findall('[aeiouy]+',ch[l:l+4]))==0:
                voyelle=np.random.choice(['a','e','i','o','u','y'])
                ch=ch[:l+3]+voyelle+ch[l+4:]
            l+=3
    return ch


#Fonction pour la generation de charabia de taille aléatoire, en prenant en compte les probabilités de taille:
def genere_charabia2(mat_enchainement, mat_size, alphabet, tailles):
    size = np.random.choice(tailles, size = None, replace = False, p = mat_size)
    ch = "\n\n"
    for i in range(size):
        tab = mat_enchainement[alphabet.index(ch[i])]
        new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
        while new_letter=='\n' or (new_letter==ch[-2] and new_letter==ch[-1]):
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
        ch += new_letter
    if len(re.findall('[aeiouy]+',ch))==0:
        i=np.random.randint(0,len(ch))
        ch=ch[:i]+ np.random.choice(['a','e','i','o','u','y'])+ch[i+1:]
    ch = ch[2:]
    return ch

#Fonction pour la generation de charabia à partir de la première lettre et de taille aléatoire
def genere_charabia3(premiere_lettre, mat_enchainement, mat_size, alphabet, tailles):
    size = np.random.choice(tailles, size = None, replace = False, p = mat_size)+1
    if premiere_lettre in string.ascii_lowercase:
        ch = premiere_lettre
        for i in range(size):
            tab = mat_enchainement[alphabet.index(ch[i])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter=='\n':
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
        return ch
    elif premiere_lettre in string.ascii_uppercase:
        ch=premiere_lettre.lower()
        for i in range(size):
            tab = mat_enchainement[alphabet.index(ch[i])]
            new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            while new_letter=='\n':
                new_letter = np.random.choice(alphabet, size = None, replace = False, p = tab)
            ch += new_letter
        return ch.capitalize()

#Fonction pour la generation de charabia à partir des dernieres lettres: A CORRIGER
def genere_charabia4(dernieres_lettres, mat_enchainement,mat_size, alphabet, tailles):
    size=np.random.choice(tailles, size=None, replace=False, p=mat_size) - len(dernieres_lettres)
    ch=dernieres_lettres
    for i in range(size):
        tab = mat_enchainement[:,alphabet.index(ch[0])]
        new_letter = np.random.choice(alphabet, size = None, replace= False, p= tab)
        ch= new_letter+ch
    return ch

#Remplacer les mots d'un texte par du charabia:
print('\n\nBienvenu au générateur de charabia Chamama \n\nQuel texte voulez-vous charabier?')
nom_fichier=str(input('introduire nom_du_fichier.txt:\n'))
doc=open(nom_fichier, 'r', encoding='utf8')
docstr=doc.read()
Lmots=re.split(r'(\W+)', docstr)
doc.close()
#print(Lmots)

print('\nChoisissez le mode de remplacement des mots:\nPour remplacer aléatoirement, entrez A;\nPour remplacer par taille, entrez T;\nPour remplacer en fonction de la première lettre, entrez P;\n, Pour remplacer en fonction du suffixe, entrez S, \n')
mode=input()
f=int(input('\nChoisissez la fréquence de remplacement: tous les ? mots : '))
i=np.random.randint(f)


while i<len(Lmots):
    #a_remplacer=Lmots[i]
    if len(Lmots[i])<=3:
        i+=1
    else:
        a_remplacer=Lmots[i]
        if mode=='T':
            Lmots[i]=genere_charabia1(prob,lettres,len(a_remplacer))
        elif mode=='A':
            Lmots[i]=genere_charabia2(prob,Lstats,lettres,tailles)
        elif mode=='P':
            Lmots[i]=genere_charabia3(a_remplacer[0],prob,Lstats,lettres,tailles)
        elif mode=='S':
            long_suffixe=int(input('Entrez la longueur du suffixe: '))
            Lmots[i]=genere_charabia4(a_remplacer[-long_suffixe],prob,Lstats,lettres,tailles)
        if a_remplacer[0] in string.ascii_uppercase : #Cas ou le mot a remplacer porte une majuscule
            Lmots[i]=Lmots[i].capitalize()
        i+=2*f

charabia=open('charabia.txt','w')
charabia.write(''.join(Lmots))
charabia.close()
