from tkinter import *
from tkinter.filedialog import *
from arene import*
from obstacle import*
from robot import*
import math as m
from affichage import *
from demo4 import*

class Fenetre(object):
    def __init__(self):
        self.fin=False
       
    def demarrer(self):
        main(self,self.z,self.p,fenetre)
        #fenetre.after(50,self.demarrer(self))

    def reset(self):
        """Cette fonction permet d'effacer un affichage pour pouvoir en importer un autre
        """
        self.z.zone_dessin.delete(ALL)
        self.z.zone_dessin.destroy()


    def import_file(self):
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
                self.p=Robot(int(L[0]),int(L[1]),m.radians(int(L[2])))
                angle=self.p.calcul_angle()
                t=self.p.calcul_hypo()
                b.inserer_robot(self.p)
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
                self.z=Affichage(b,fenetre,self.p)
                self.z.arene=b
                self.z.zone()
                self.z.afficher()
                self.z.afficher_robot()
            elif ARENE:
                L.append(i.strip())
            elif ROBOT:
                L.append(i.strip())
            elif OBSTACLE:
                L.append(i.strip())
            fichier.close()

    def export_file(self):
        """Cette fonction permet de sauvegarder une configuration : creer un nouveau fichier Scenario.txt
        """
        f=open('Scenario.txt','w')
        f.write('ARENE\n')
        f.write(str(self.z.arene.nb_ligne)+'\n')
        f.write(str(self.z.arene.nb_colonne)+'\n')
        f.write("ROBOT\n")
        for i in self.z.arene.list_rob:
            f.write(str(i.x)+'\n')
            f.write(str(i.y)+'\n')
            f.write(str(int(m.degrees(i.angle)))+'\n')
        f.write("OBSTACLE\n")
        for i in self.z.arene.list_obj:
            f.write(str(i.x)+'\n')
            f.write(str(i.y)+'\n')
            f.write(str(i.forme)+'\n')
            f.write(str(i.para1)+'\n')
            f.write(str(i.para2)+'\n')
        f.write("FIN")
        f.close()

    def arreter(self):
        self.fin=True
        print(self.fin)
        
f=Fenetre
f.fin=False
def importe():
    f.import_file(f)
    
def export():
    f.export_file(f)

def arrete():
    f.arreter(f)
   
def demar():
    if not f.fin: 
        f.demarrer(f)
        fenetre.after(50,demar)
    else:
        f.fin=False
        
def res():
    f.reset(f)
    

"""cree une fenetre"""
fenetre = Tk()#creer une fenetre
fenetre.title('Arene')#donner un nom  la fenetre

fenetre.geometry("1200x600")
"""creation des different bouton"""
f=Fenetre
BoutonExporter = Button(fenetre, text ='Exporter', command = export)
BoutonExporter.pack(side = LEFT, padx = 10, pady = 10)

BoutonArreter = Button(fenetre, text ='Arreter', command = arrete)
BoutonArreter.pack(side = LEFT, padx = 10, pady = 10)

BoutonGo = Button(fenetre, text ='Démarrer', command = demar)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

BoutonQuitter = Button(fenetre, text ='Quitter', command = fenetre.destroy)
BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)

BoutonImporter = Button(fenetre, text ='Importer', command = importe)
BoutonImporter.pack(side = LEFT, padx = 10, pady = 10)

BoutonReset = Button(fenetre, text ='Reset', command = res)
BoutonReset.pack(side = LEFT, padx = 10, pady = 10)

"""creation de case avec des informations a l'interieur"""
label = Label(fenetre, text="x y", bg="yellow")
label.pack()

fenetre.mainloop()
