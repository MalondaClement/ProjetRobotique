from bouton import *
from tkinter import *

class Fenetre(object):
    def __init__(self, ):
        pass

arret=False ## A VIRER
"""cree une fenetre"""
fenetre = Tk()#creer une fenetre
fenetre.title('Arene')#donner un nom  la fenetre

fenetre.geometry("1200x600")
"""creation des different bouton"""
BoutonExporter = Button(fenetre, text ='Exporter', command = export_file)
BoutonExporter.pack(side = LEFT, padx = 10, pady = 10)

BoutonArreter = Button(fenetre, text ='Arreter', command = arreter)
BoutonArreter.pack(side = LEFT, padx = 10, pady = 10)

BoutonGo = Button(fenetre, text ='Démarrer', command = demarrer)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

BoutonQuitter = Button(fenetre, text ='Quitter', command = fenetre.destroy)
BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)

BoutonImporter = Button(fenetre, text ='Importer', command = import_file)
BoutonImporter.pack(side = LEFT, padx = 10, pady = 10)

BoutonReset = Button(fenetre, text ='Reset', command = reset)
BoutonReset.pack(side = LEFT, padx = 10, pady = 10)

"""creation de case avec des informations a l'interieur"""
label = Label(fenetre, text="x y", bg="yellow")
label.pack()

fenetre.mainloop()
