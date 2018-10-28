#/usr/bin/env python2

import gtk
import random


with open("liste_mots.txt", "r") as fichier:
    liste_mots = [
        ligne.strip()
        for ligne in fichier.readlines()
        if ligne.strip()
    ]


mot_a_trouver = random.choice(liste_mots)
ESSAIS_MAX = 10
compteur = 0
mot_affiche = "*" * len(mot_a_trouver)
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
liste_lettres = []


fin = False
gagne = False


def mon_str(chaine):
    result = ""
    for lettre in chaine:
        result += lettre + " "
    return result


def gerer_fin_du_jeu(p_gagne):
    if p_gagne:
        label_lettres.set_text("c'etait bien : " + mot_a_trouver)
        image_pendu.set_from_file("feux.gif")
        label_mot_affiche.set_text("Bravo ! Vous avez gagne !")
    else:
        label_lettres.set_text("c'etait : " + mot_a_trouver)
        image_pendu.set_from_file("pik.gif")
        label_mot_affiche.set_text("vous avez perdu")


def when_button_valider_lettre_is_clicked(widget):

    global compteur
    global mot_affiche
    global fin
    global labe_mot_affiche
    global gagne
    global liste_lettres

    essai = essai_lettre.get_text()
    essai_lettre.grab_focus()
    essai_lettre.set_text("")

    if not essai:
        return

    if essai not in ALPHABET:
        return

    essai = essai.upper()

    if fin:
        return

    if essai in liste_lettres:
        return

    if essai not in mot_a_trouver:
        liste_lettres.append(essai)
        label_lettres.set_text(mon_str(liste_lettres))
        compteur += 1
        if compteur == ESSAIS_MAX:
            fin = True
            gagne = False
            gerer_fin_du_jeu(gagne)
        else:
            image_pendu.set_from_file(str(compteur) + ".png")
        return
    # Tout le monde est gentil

    liste_lettres.append(essai)
    label_lettres.set_text(mon_str(liste_lettres))

    n_mot_affiche = ""
    for i in range(len(mot_a_trouver)):
        if mot_a_trouver[i] == essai:
            n_mot_affiche = n_mot_affiche + essai
        else:
            n_mot_affiche = n_mot_affiche + mot_affiche[i]
    mot_affiche = n_mot_affiche
    label_mot_affiche.set_text(mot_affiche)

    if mot_a_trouver == mot_affiche:
        fin = True
        gagne = True
        gerer_fin_du_jeu(gagne)


def key_pressed(widget, event):
    keyval = event.keyval
    keyval_name = gtk.gdk.keyval_name(keyval)
    if keyval_name == "Return":
        when_button_valider_lettre_is_clicked(widget)


def when_button_valider_mot_is_clicked(widget):

    global compteur
    global mot_affiche
    global fin
    global labe_mot_affiche
    global gagne
    global liste_lettres

    mot = entree_mot.get_text()
    essai_lettre.grab_focus()
    entree_mot.set_text("")

    if not mot:
        return

    for lettre in mot:
        if lettre not in ALPHABET:
            return
    mot = mot.upper()

    if fin:
        return

    if mot != mot_a_trouver:
        compteur += 1
        if compteur == ESSAIS_MAX:
            fin = True
            gagne = False
            gerer_fin_du_jeu(gagne)
        else:
            image_pendu.set_from_file(str(compteur) + ".png")
        return
    # Tout le monde est gentil

    fin = True
    gagne = True
    gerer_fin_du_jeu(gagne)


# interface

interface = gtk.Builder()
interface.add_from_file('interface.glade')

fenetre = interface.get_object('fenetre')
fenetre.connect('delete-event', gtk.main_quit)
fenetre.connect("key-press-event", key_pressed)

label_lettres = interface.get_object('label_lettres')
label_lettres.set_text("Ici les lettres precedentes.")

label_mot_affiche = interface.get_object('label_mot_affiche')
label_mot_affiche.set_text(mot_affiche)


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
