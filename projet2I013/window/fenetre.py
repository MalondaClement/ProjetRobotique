from tkinter import *
from tkinter.filedialog import *
#from ..modele.arene import Arene

class Fenetre(object):
    def __init__(self):
        pass


def demarrer():
    global arret
    if arret==True:
        arret=False
    main()


def reset():
    """Cette fonction permet d'effacer un affichage pour pouvoir en importer un autre
    """
    zone_dessin.delete(ALL)
    zone_dessin.destroy()


def import_file():
    filepath = askopenfilename(title="Ouvrir un fichier",filetypes=[('txt files','.txt'),('all files','.*')])
    fichier = open(filepath,'r')
    ARENE=False
    ROBOT=False
    OBSTACLE=False
    L=[]
    for i in fichier.readlines():
        if i.strip()=="ARENE":
            ARENE=True
            ROBOT=False
            OBSTACLE=False
        elif i.strip()=="ROBOT":
            b=Arene(int(L[0]),int(L[1]))
            b.cree_mur()
            L=[]
            ARENE=False
            ROBOT=True
            OBSTACLE=False
        elif i.strip()=="OBSTACLE":
            global p
            p=Robot(int(L[0]),int(L[1]),m.radians(int(L[2])))
            global angle
            angle=p.calcul_angle()
            global t
            t=p.calcul_hypo()
            b.inserer_robot(p)
            L=[]
            ARENE=False
            ROBOT=False
            OBSTACLE=True
        elif i.strip()=="FIN":
            a=0
            while a<len(L):
                o=Obstacle(int(L[a]),int(L[a+1]),int(L[a+2]),int(L[a+3]),int(L[a+4]))
                b.inserer_obs(o)
                a=a+5
            global z
            z=Affichage(b)
            z.arene=b
            z.zone()
            z.afficher()
            z.afficher_robot()
        elif ARENE:
            L.append(i.strip())
        elif ROBOT:
            L.append(i.strip())
        elif OBSTACLE:
            L.append(i.strip())
        fichier.close()

def export_file():
    """Cette fonction permet de sauvegarder une configuration : creer un nouveau fichier Scenario.txt
    """
    f=open('Scenario.txt','w')
    f.write('ARENE\n')
    f.write(str(z.arene.nb_ligne)+'\n')
    f.write(str(z.arene.nb_colonne)+'\n')
    f.write("ROBOT\n")
    for i in z.arene.list_rob:
        f.write(str(i.x)+'\n')
        f.write(str(i.y)+'\n')
        f.write(str(int(m.degrees(i.angle)))+'\n')
    f.write("OBSTACLE\n")
    for i in z.arene.list_obj:
        f.write(str(i.x)+'\n')
        f.write(str(i.y)+'\n')
        f.write(str(i.forme)+'\n')
        f.write(str(i.para1)+'\n')
        f.write(str(i.para2)+'\n')
    f.write("FIN")
    f.close()

def arreter():
    global arret
    arret=True

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
