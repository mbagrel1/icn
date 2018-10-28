from Tkinter import *
fenetre_principale = Tk()

def impot2017(rimposable, pfiscal):
    rapportrn = rimposable/pfiscal
    if rapportrn < 9807:
        impots = 0
    elif rapportrn < 27086:
        impots = (rimposable * 0.14) - (1372.98 * pfiscal)
    elif rapportrn < 72617:
        impots = (rimposable * 0.30) - (5706.74 * pfiscal)
    elif rapportrn < 153783:
        impots = (rimposable * 0.41) - (13694.61 * pfiscal)
    else:
        impots = (rimposable * 0.45) - (19845.93 * pfiscal)
    return impots

imposable=StringVar()
champ_text= Label(fenetre_principale, text="votre revenu imposable")
champ_text.pack()
champ_imposable=Entry(fenetre_principale,textvariable=imposable, width=30)
champ_imposable.pack()
revenu_imp=champ_imposable.get()

champ_text= Label(fenetre_principale, text="votre nombre de parts de votre foyer fiscal")
champ_text.pack()
fiscal=StringVar()
champ_imposable=Entry(fenetre_principale,textvariable=fiscal, width=30)
part_fiscal=champ_imposable.get()
champ_imposable.pack()

bouton_valider = Button(fenetre_principale, text="Valider", commande=impot2017(revenu_imp,part_fiscal))
bouton_valider.pack()

champ_impot=Label(fenetre_principale, text="votre montant d'impots a payer est de")
champ_impot.pack()



fenetre_principale.mainloop()
