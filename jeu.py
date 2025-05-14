'''
Classe jeu
'''
import pyxel as px
from navire import Navire
from constants import *


class Jeu:
     
    def __init__(self):
        """crée deux navires"""
        px.load('theme.pyxres')
        self.navire1 = Navire(3,BASE_POS_NAVIRE1,name='Navire 1')
        self.navire2 = Navire(7,BASE_POS_NAVIRE2,name='Navire 2')
        self.cooldown1 = 0
        self.cooldown2 = 0
        self.cooldown_fleche1 = 0
        self.cooldown_fleche2 = 0
        self.menu1 = False
        self.menu2 = False
     
     
    def update(self):
        """met à jour le jeu"""
        
        #=============Controle navire 1==========
        
        if px.btnp(px.KEY_A):
            self.navire1.change_type_fleche()
                
        if px.btnp(px.KEY_E):
            if self.cooldown_fleche1 <= px.frame_count:
                if (self.navire1.position[1] > self.navire2.position[1] or self.navire1.position[1] + LONGUEUR_NAVIRE < self.navire2.position[1] + LONGUEUR_NAVIRE) and ((self.navire2.position[0] - (self.navire1.position[0]+LARGEUR_NAVIRE))**2)<=64:
                    type_degats , degats = self.navire1.inflige_degats(self.navire1.type_fleche)
                    self.navire2.prends_degats(type_degats, degats)
                    self.cooldown_fleche1 = px.frame_count + 60
        
        if px.btnp(px.KEY_Q):
            self.navire1.change_orientation(1)
            
        elif px.btnp(px.KEY_D):
            self.navire1.change_orientation(-1)
        
        if px.btnp(px.KEY_TAB):
            self.menu1 = not(self.menu1)
        
        if self.menu1:
            if px.btn(px.KEY_Z):
                pass
            
            elif px.btn(px.KEY_S):
                pass
        else:
            if px.btn(px.KEY_Z):
                self.navire1.change_vitesse(True)
            
            elif px.btn(px.KEY_S):
                self.navire1.change_vitesse(False)
            
        
            
        #============Controle navire 2===========
            
        if px.btnp(px.KEY_0):
            self.navire2.change_type_fleche()
                
        if px.btnp(px.KEY_1):
            if self.cooldown_fleche2 <= px.frame_count:
                if (self.navire2.position[1] > self.navire1.position[1] or self.navire2.position[1] + LONGUEUR_NAVIRE < self.navire1.position[1] + LONGUEUR_NAVIRE) and ((self.navire1.position[0] - (self.navire2.position[0]+LARGEUR_NAVIRE))**2)<=64:
                    type_degats , degats = self.navire2.inflige_degats(self.navire2.type_fleche)
                    self.navire1.prends_degats(type_degats, degats)
                    self.cooldown_fleche2 = px.frame_count + 60
        
        if px.btnp(px.KEY_LEFT):
            self.navire2.change_orientation(-1)
            
        elif px.btnp(px.KEY_RIGHT):
            self.navire2.change_orientation(1)
        
        if px.btnp(px.KEY_KP_ENTER):
            self.menu2 = not(self.menu2)
        
        if self.menu2:
            if px.btn(px.KEY_UP):
                pass
            
            elif px.btn(px.KEY_DOWN):
                pass
        else:
            if px.btnp(px.KEY_UP):
                self.navire2.change_vitesse(True)
            
            elif px.btnp(px.KEY_DOWN):
                self.navire2.change_vitesse(False)
        
        

        #================================
        
        if self.cooldown1 <= px.frame_count:
            if (self.navire1.position[0] > self.navire2.position[1] or self.navire1.position[0] + LARGEUR_NAVIRE < self.navire2.position[1] + LONGUEUR_NAVIRE) and ((self.navire2.position[1] - (self.navire1.position[1]+LONGUEUR_NAVIRE))**2)<=15:
                type_degats , degats = self.navire1.inflige_degats('brise-coque')
                self.navire2.prends_degats(type_degats, degats)
                self.cooldown1 = px.frame_count + 300
        
        if self.cooldown2 <= px.frame_count:
            if (self.navire2.position[0] > self.navire1.position[1] or self.navire2.position[0] + LARGEUR_NAVIRE < self.navire1.position[1] + LONGUEUR_NAVIRE) and ((self.navire1.position[1] - (self.navire2.position[1]+LONGUEUR_NAVIRE))**2)<=15:
                type_degats , degats = self.navire2.inflige_degats('brise-coque')
                self.navire1.prends_degats(type_degats, degats)
                self.cooldown2 = px.frame_count + 300
                
        self.navire1.update()
        self.navire2.update()
    
    def draw(self):
        """
        Efface l'écran et dessine la mer
        """
        px.cls(5)
        if self.menu1:
            px.rect(2, 2, 25, 50, 7)
            for indice in range(0,8):
                px.text(10,5+indice*16,EQUIPAGE[indice],0)
        if self.menu2:
            px.rect(229, 204, 25, 50, 7)
            for indice in range(0,8):
                px.text(229,209+indice*16,EQUIPAGE[indice],0)
        self.navire1.draw()
        self.navire2.draw()
        

if __name__ == "__main__":
    # Démarre l'application
    px.init(256,256, title="Bataille Navale", fps = 60)
    appli = Jeu()
    px.run(appli.update, appli.draw)
