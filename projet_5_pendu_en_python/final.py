#/usr/bin/env python2

import gtk

mot_a_trouver = "chat"
ESSAIS_MAX = 6
compteur = 0
mot_affiche = "*" * len(mot_a_trouver)

fin = False
gagne = False

# interface


def when_button_valider_lettre_is_clicked(widget):
    """verifie si l'essai de lettre est dans le mot"""
    global compteur
    global mot_affiche
    global fin
    global labe_mot_affiche
    global gagne
    n_mot_affiche = ""
    trouve = False
    essai = essai_lettre.get_text()
    for i in range(len(mot_a_trouver)):
        if mot_a_trouver[i] == essai:
            n_mot_affiche = n_mot_affiche + essai
            trouve = True
        else:
            n_mot_affiche = n_mot_affiche + mot_affiche[i]
    if not trouve:
        compteur = compteur + 1
        nom_image = str(compteur) + ".png"
        image_pendu.set_from_file(nom_image)
    mot_affiche = n_mot_affiche
    label_mot_affiche.set_text(mot_affiche)

    if mot_a_trouver == mot_affiche:
        fin = True
        gagne = True
        print "vous avez gagne"
    if compteur == ESSAIS_MAX:
        fin = True
        print "vous avez perdu"


def when_button_valider_mot_is_clicked(widget):
    print "Hello World"


interface = gtk.Builder()
interface.add_from_file('interface.glade')

fenetre = interface.get_object('fenetre')
fenetre.connect('delete-event', gtk.main_quit)

label_mot_affiche = interface.get_object('label_mot_affiche')
print(label_mot_affiche)

button_valider_lettre = interface.get_object('button_valider_lettre')
button_valider_lettre.connect('clicked', when_button_valider_lettre_is_clicked)

essai_lettre = interface.get_object('essai_lettre')

mot_a_deviner = interface.get_object('mot_a_deviner')
entree_mot = interface.get_object('entree_mot')

button_valider_mot = interface.get_object('button_valider_mot')
button_valider_mot.connect('clicked', when_button_valider_mot_is_clicked)

image_pendu = interface.get_object('image_pendu')

# interface

fenetre.show_all()
gtk.main()
