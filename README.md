# GENERATEUR DE CHARABIA

Le générateur de Charabia Chamama a pour but de générer des mots nouveaux mais crédibles dans une langue donnée, qui vont remplacer certains mots d’un texte fourni par l’utilisateur. 

Pour cela, un corpus de mots a été analysé pour chaque langue, permettant de générer des matrices de probabilités d’enchainements de lettres dans la langue, en utilisant les chaines de Markov. 
Un automate à états finis se base ensuite sur cette matrice pour générer des enchainements de lettres vraisemblables, en prenant également en compte plusieurs exceptions, notamment pour éviter de trop longues suites de consonnes. 
Les mots ainsi créés vont remplacer certains mots du texte. 

Ce programme contient un système d’interaction avec l’utilisateur qui va lui permettre de sélectionner la langue de son choix, ses préférences de génération des nouveaux mots, la fréquence de modification et d’entrer le texte qu’il veut modifier. 
Notre programme propose plusieurs langues : le français, l’anglais, l’espagnol et le latin. 
La génération des mots peut se faire aléatoirement, en respectant la taille du mot originel, ou en gardant la première lettre. 

Pour faire fonctionner ce programme, l’utilisateur est invité à télécharger les corpus de mots servant à la génération des matrices de probabilités dans chaque langue (ref_langue). 
Il peut aussi, s’il le souhaite, prendre les textes à modifier proposés ici, ou bien les choisir lui-même. 
Le chemin d’accès vers le répertoire où sont stockés tous ces fichiers dans son ordinateur lui sera demandé. 

Et maintenant, à vous de charabier !

