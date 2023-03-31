# Projet de Forensic 2023

## A. Objectifs

1. Réaliser un outil fonctionnel en Python utile pour une analyse Forensique
2. Travailler en équipe organisée
3. Produire un outil lisible, évolutif et maintenable, pas uniquement pour vos pires ennemis
4. Savoir rédiger de la documentation
5. Réaliser une démonstration des capacités de l'outil
6. Et bien sûr, mettre en oeuvre les connaissances du cours

## B. Sujet

### B.1. Extraction des fichiers d'intêret

Il faut réaliser un outil en Python pour extraire les fichiers intéressants pour le forensic, d'une image disque au format EWF, celle utilisée en cours par exemple.

Vous devez extraire au minimum :

- les fichiers du registre système et les ruches utilisateur,
- Les navigateurs Internet Edge, Internet Explorer, Firefox et Chrome,
- les journaux Windows Security et System au minimum,
- et la MFT

La liste des fichiers à extraire devra être au format yaml, notamment pour indiquer les outils / commandes à utiliser par la suite (B.2).
Il ne s'agit pas d'être exhaustif, mais de prendre en compte les données sources étudiées en cours.
Il est conseillé d'utiliser des expressions régulières, mais seuls les fichiers prévus doivent être extraits.

Il est également conseillé d'utiliser, en back end, les commandes The Sleuth Kit suivantes: mmls, fls et icat

On restreindra l'outil aux fichiers à extraire venant dune image Windows 7 à Windows 11.

L'outil devra fonctionner sous Windows ou Linux, avec Python 3.

### B.2. En bonus, extraction des informations

- Utiliser les outils d'Eric Zimmerman ou RegRipper pour extraire les données

## C. Critères d'évaluation

### Code

Le code devra être fonctionnel, lisible, modulaire et fourni sur github (ou une archive .zip), avec un readme pour le faire fonctionner.

### Rapport

Il est au format PDF (même si initialement en Word ou Markdown), sur le github (ou dans l'archive).

Le rapport devra contenir:
- un argumentaire sur l'architecture du code
- qui a travaillé sur quelle partie
- une série de tests implémentés ou possibles, prouvant la robustesse de l'outil et les cas de figure envisagés ou testés
- les cas non supportés
- les bugs connus et si on saurait les résoudre

### Soutenance

Le groupe effectuera une démonstration et répondra aux éventuelles questions sur le code, le rapport et le travail d'équipe.
Si le rapport est complet, il n'est pas nécessaire de montrer des slides.

Pensez à vous organiser très tôt pour vous répartir le travail au maximum, et se garder du temps pour assembler le tout.

## Références

- https://github.com/EricZimmerman/KapeFiles/tree/master/Targets/Browser
- https://github.com/EricZimmerman/KapeFiles/blob/master/Targets/Windows/RegistryHivesSystem.tkape
- https://github.com/EricZimmerman/KapeFiles/blob/master/Targets/Windows/RegistryHivesUser.tkape 