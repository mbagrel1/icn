

def impot2017(rimposable, pfiscal):
    rapportrn = float(rimposable) / pfiscal
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

#programme principal

revenu_imposable = input("Veuillez saisir votre revenu imposable :")
nb_de_part = input("Veuillez saisir votre nombre de parts fiscales :")
print "le montant de l'impot a payer est de", impot2017(revenu_imposable,nb_de_part),"euros"
