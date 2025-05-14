'''
Classe jeu
'''
import pyxel as px
from navire import Navire
from constants import *


class Jeu:
     
    def __init__(self):
        """crée deux navires"""
        self.navire1 = Navire(3,[2,2])
        self.navire2 = Navire(7,[1,1])
     
    def update(self):
        """met à jour le jeu"""
        
        #=============Controle navire 1==========
        
        if px.btnp(px.KEY_A):
            self.navire1.change_type_fleche()
                
        if px.btnp(px.KEY_E):
            if (self.navire1.position[1] > self.navire2.position[1] or self.navire1.position[1] + LONGUEUR_NAVIRE < self.navire2.position[1] + LONGUEUR_NAVIRE) and ((self.navire2.position[0] - (self.navire1.position[0]+LARGEUR_NAVIRE))**2)<=64:
                type_degats , degats = self.navire1.inflige_degats(self.navire1.type_fleche)
                self.navire2.prends_degats(type_degats, degats)
        
        if px.btnp(px.KEY_Q):
            self.navire1.change_orientation(1)
            
        elif px.btnp(px.KEY_D):
            self.navire1.change_orientation(-1)
            
        if px.btn(px.KEY_SHIFT):
            self.navire1.change_vitesse(True)
            
        elif px.btn(px.KEY_CTRL):
            self.navire1.change_vitesse(False)
            
        #============Controle navire 2===========
            
        if px.btnp(px.KEY_0):
            self.navire2.change_type_fleche()
                
        if px.btnp(px.KEY_1):
            if (self.navire2.position[1] > self.navire1.position[1] or self.navire2.position[1] + LONGUEUR_NAVIRE < self.navire1.position[1] + LONGUEUR_NAVIRE) and ((self.navire1.position[0] - (self.navire2.position[0]+LARGEUR_NAVIRE))**2)<=64:
                type_degats , degats = self.navire2.inflige_degats(self.navire2.type_fleche)
                self.navire1.prends_degats(type_degats, degats)
        
        if px.btnp(px.KEY_LEFT):
            self.navire2.change_orientation(-1)
            
        elif px.btnp(px.KEY_RIGHT):
            self.navire2.change_orientation(1)
        
        if px.btnp(px.KEY_PLUS):
            self.navire2.change_vitesse(True)
            
        elif px.btnp(px.KEY_MINUS):
            self.navire2.change_vitesse(False)

        #================================
        
        if False:#a completer
            type_degats , degats = self.navire1.inflige_degats('brise-coque')
            self.navire2.prends_degats(type_degats, degats)
        
        elif False:#a completer
            type_degats , degats = self.navire2.inflige_degats('brise-coque')
            self.navire1.prends_degats(type_degats, degats)
                
        self.navire1.update()
        self.navire2.update()
    
    def draw(self):
        """
        Efface l'écran et dessine la mer
        """
        px.cls(5)
        self.navire1.draw()
        self.navire2.draw()
        

if __name__ == "__main__":
    # Démarre l'application
    px.init(256,256, title="Bataille Navale", fps = 60)
    appli = Jeu()
    px.run(appli.update, appli.draw)
