import gtk
global compteur
def when_button_valider_lettre_is_clicked(widget) :
	global compteur
	chaine=str(compteur)+".png"
	print chaine
	print str(chaine)
	image_pendu.set_from_file (str(chaine))
 
def when_button_valider_mot_is_clicked(widget) : 
	print "Hello World"
 

interface = gtk.Builder()
interface.add_from_file('interface.glade')

fenetre = interface.get_object('fenetre')
fenetre.connect('delete-event', gtk.main_quit)

label_motaffiche = interface.get_object('label_lettre_a_essayer')

button_valider_lettre = interface.get_object('button_valider_lettre')
button_valider_lettre.connect('clicked', when_button_valider_lettre_is_clicked)

entree_lettre = interface.get_object('entree_lettre')

mot_a_deviner = interface.get_object('mot_a_deviner')
entree_mot = interface.get_object('entree_mot')

button_valider_mot = interface.get_object('button_valider_mot')
button_valider_mot.connect('clicked', when_button_valider_mot_is_clicked)

image_pendu = interface.get_object('image_pendu')




fenetre.show_all()
gtk.main()

	



