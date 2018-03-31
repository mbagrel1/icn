#/usr/bin/env python2

mot_a_trouver = "chat"
#mot_a_trouver= raw_input("Choississez le mot a trouver : ")

compteur = 0

motAffiche = ""
for i in range(len(mot_a_trouver)):
    motAffiche = motAffiche + "*"
print motAffiche

fin = False
gagne = False

while fin == False:
    naffiche = ""
    trouve = False
    essai = raw_input("essayez une lettre :")
    for i in range(len(mot_a_trouver)):
        if mot_a_trouver[i] == essai:
            naffiche = naffiche + essai
            trouve = True
        else:
            naffiche = naffiche + motAffiche[i]
    if trouve == False:
        compteur = compteur + 1
    motAffiche = naffiche
    print motAffiche
    print compteur
    if mot_a_trouver == motAffiche:
        fin = True
        gagne = True
    if compteur == 6:
        fin = True
if gagne == True:
    print"Vous avez gagne, champagne!!!"
else:
    print"vous avez perdu,vous etes nul, le mot etait :" + mot_a_trouver
