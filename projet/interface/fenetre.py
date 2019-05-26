from tkinter import *
from tkinter.filedialog import *
from math import degrees, radians
from modele.arene import *
from modele.obstacle import *
from modele.robotreel import *
from .affichage import *
from modele.controleur_robotreel_carre import ControleurRobotReelCarre
from modele.controleur_robotreel_mur import ControleurRobotReelMur
from modele.controleur_robotreel_contourner_porte import ControleurRobotReelContournerPorte
from modele.controleur_robotreel_cercle import ControleurRobotReelCercle
from threading import Thread
import time

class Fenetre(Thread):
    """La classe Fenetre permet de créer une fenetre tkinter avec différent bouton.
    """
    def __init__(self, i):
        self.fin=False
        self.i=i
        super(Fenetre,self).__init__()

    def creer(self):
        """cree une fenetre"""
        self.fenetre = Tk()
        self.fenetre.title('Arene')
        self.fenetre.geometry("1200x600")
        """creation des different bouton"""
        BoutonExporter = Button(self.fenetre, text ='Exporter', command = self.export_file)
        BoutonExporter.pack(side = LEFT, padx = 10, pady = 10)

        BoutonArreter = Button(self.fenetre, text ='Arreter', command = self.arreter)
        BoutonArreter.pack(side = LEFT, padx = 10, pady = 10)

        BoutonGo = Button(self.fenetre, text ='Démarrer', command = self.demarrer)
        BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

        BoutonQuitter = Button(self.fenetre, text ='Quitter', command = self.fenetre.destroy)
        BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)

        BoutonImporter = Button(self.fenetre, text ='Importer', command = self.import_file)
        BoutonImporter.pack(side = LEFT, padx = 10, pady = 10)

        BoutonReset = Button(self.fenetre, text ='Reset', command = self.reset)
        BoutonReset.pack(side = LEFT, padx = 10, pady = 10)
        """creation de case avec des informations a l'interieur"""
        label = Label(self.fenetre, text="x y", bg="yellow")
        label.pack()

        self.fenetre.mainloop()

    """Demarre la demo selon le controleur choisi.
    """
    def demarrer(self):
        #self.b.start()
        #ctrl=ControleurRobotReel(self.p)
        #self.start()
        if not self.controleur.stop() and not self.fin:
            self.controleur.update()
            self.update() ## a griser si pas d'affichage
            self.b.update()
            self.fenetre.after(50,self.demarrer)
        else:
            print ("fin")
            self.fin=False
    """Efface le canvas present sur la fenetre. Cela permet de changer d'arène sans avoir a relancer le programme.
    """
    def reset(self):
        """Cette fonction permet d'effacer un affichage pour pouvoir en importer un autre
        """
        self.z.zone_dessin.destroy()

    """L'importation s'effectue en lisant un fichier au format strict.
    On lit la ligne arène, puis les ligne sont enregistrés dans une liste.
    Lorsque l'on lit l'element suivant ROBOT, on sait que les informations relatives a l'arène sont dans la liste donc on peut créer notre arène.
    Et ainsi de suite pour tous les autres éléments liés a l'arène.
    """
    def import_file(self):
        #filepath = askopenfilename(title="Ouvrir un fichier",filetypes=[('txt files','.txt'),('all files','.*')])
        #if filepath==() or  filepath=="":
            #return
        #if hasattr(self, 'z'):
            #self.reset()
        #fichier = open(filepath,'r')
        a=os.getcwd()
        a=a.replace('projet','')
        fichier=open(a+"/Scenario/test.txt",'r')
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
                self.b=Arene(int(L[0]),int(L[1]))
                self.b.cree_mur()
                L=[]
                ARENE=False
                ROBOT=True
                OBSTACLE=False
            elif i.strip()=="OBSTACLE":
                self.p=RobotReel(int(L[0]),int(L[1]),radians(int(L[2])),self.b)
                if self.i=="0" :
                    self.controleur= ControleurRobotReelCarre(self.p)
                elif self.i=="1" :
                    self.controleur=ControleurRobotReelMur(self.p)
                elif self.i=="2" :
                    self.controleur=ControleurRobotReelCercle(self.p, 400, 10, "droite", 50)
                elif self.i=="3" :
                    self.controleur=ControleurRobotReelContournerPorte(self.p)
                #ajouter nouveaux controleurs ici
                else:
                    print("Erreur la demo demandee n'existe pas")
                    exit(1)
                angle=self.p.calcul_angle()
                t=self.p.calcul_hypo()
                self.b.inserer_robot(self.p)
                L=[]
                ARENE=False
                ROBOT=False
                OBSTACLE=True
            elif i.strip()=="FIN":
                a=0
                while a<len(L):
                    if int(L[a+2]) == 1:
                        o=ObstacleRectangle(int(L[a]),int(L[a+1]),int(L[a+3]),int(L[a+4]))#modif
                    elif int(L[a+2]) == 2:
                        o=ObstacleEllipse(int(L[a]),int(L[a+1]),int(L[a+3]),int(L[a+4]))#modif
                    else :
                        o=ObstacleTriangle(int(L[a]),int(L[a+1]),int(L[a+3]),int(L[a+4]))#modif
                    self.b.inserer_obs(o)
                    a=a+5
                self.z=Affichage(self.b,self.fenetre,self.p)
                self.z.arene=self.b
                self.z.zone()
                self.z.afficher()
                self.z.afficher_robot()
                #self.start()
                #self.b.start()
            elif ARENE:
                L.append(i.strip())
            elif ROBOT:
                L.append(i.strip())
            elif OBSTACLE:
                L.append(i.strip())
            fichier.close()
 
    def export_file(self):
        """Cette fonction permet de sauvegarder une configuration : creer un nouveau fichier Scenario.txt
           On recupère les informations dont nous avons besoin pour construire une arène et ses composants puis on les écrit dans fichier texte.
        """
        if not hasattr(self, 'z'):
            return
        f=open('Scenario.txt','w')
        f.write('ARENE\n')
        f.write(str(self.z.arene.nb_ligne)+'\n')
        f.write(str(self.z.arene.nb_colonne)+'\n')
        f.write("ROBOT\n")
        for i in self.z.arene.list_rob:
            f.write(str(i.x)+'\n')
            f.write(str(i.y)+'\n')
            f.write(str(int(degrees(i.angle)))+'\n')
        f.write("OBSTACLE\n")
        for i in self.z.arene.list_obj:
            f.write(str(i.x)+'\n')
            f.write(str(i.y)+'\n')
            f.write(str(i.forme)+'\n')
            f.write(str(i.para1)+'\n')
            f.write(str(i.para2)+'\n')
        f.write("FIN")
        f.close()

    """Fonction arreter permet d'arreter une simulation pour exporter une situation voulue par exemple ou pour debugger.
    """
    def arreter(self):
        self.fin=True

    """Meme chose que update dans affichage.
    """
    def update(self):
        self.z.zone_dessin.create_rectangle(self.p.x,self.p.y,self.p.x+1,self.p.y+1,fill='green')
        self.z.dessiner()

    """Meme chose que dans affichage.
    """
    def run(self):
        self.fenetre.mainloop()
        while True:
            self.update()
            time.sleep(1./20)







