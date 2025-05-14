'''
Classe jeu
'''
import pyxel as px
import Navire


class Jeu:
     
    def __init__(self):
        """crée deux navires"""
        self.navire1 = Navire(3)
        self.navire2 = Navire(7)
     
    def update(self):
        """met à jour le jeu"""
        
        if px.btnp(px.KEY_A):
            if :
                type_degats , degats = self.navire1.inflige_degats('flèche')
                self.navire2.prends_degats(type_degats, degats)
                
        elif px.btnp(px.KEY_E):
            if :
                type_degats , degats = self.navire1.inflige_degats('feu')
                self.navire2.prends_degats(type_degats, degats)
                
        if px.btnp(px.KEY_0):
            if :
                type_degats , degats = self.navire2.inflige_degats('flèche')
                self.navire1.prends_degats(type_degats, degats)
                
        elif px.btnp(px.KEY_1):
            if :
                type_degats , degats = self.navire2.inflige_degats('feu')
                self.navire1.prends_degats(type_degats, degats)
        
        if px.btnp(px.KEY_Z):
            if px.btnp(px.KEY_Q):
                self.navire1.change_orientation(8)
            elif px.btnp(px.KEY_D):
                self.navire1.change_orientation(2)
            else:
                self.navire1.change_orientation(1)
                
        elif px.btnp(px.KEY_S):
            if px.btnp(px.KEY_Q):
                self.navire1.change_orientation(6)
            elif px.btnp(px.KEY_D):
                self.navire1.change_orientation(4)
            else:
                self.navire1.change_orientation(5)
                
        elif px.btnp(px.KEY_Q):
            self.navire1.change_orientation(7)
            
        elif px.btnp(px.KEY_D):
            self.navire1.change_orientation(3)
            
        if px.btn(px.KEY_SHIFT):
            self.navire1.change_vitesse(True)
            
        elif px.btn(px.KEY_CTRL):
            self.navire1.change_vitesse(False)
            
            
        if px.btnp(px.KEY_UP):
            if px.btnp(px.KEY_LEFT):
                self.navire2.change_orientation(8)
            elif px.btnp(px.KEY_RIGHT):
                self.navire2.change_orientation(2)
            else:
                self.navire2.change_orientation(1)
                
        elif px.btnp(px.KEY_DOWN):
            if px.btnp(px.KEY_LEFT):
                self.navire2.change_orientation(6)
            elif px.btnp(px.KEY_RIGHT):
                self.navire2.change_orientation(4)
            else:
                self.navire2.change_orientation(5)
                
        elif px.btnp(px.KEY_LEFT):
            self.navire2.change_orientation(7)
            
        elif px.btnp(px.KEY_RIGHT):
            self.navire2.change_orientation(3)
        
        if px.btn(px.KEY_PLUS):
            self.navire2.change_vitesse(True)
            
        elif px.btn(px.KEY_MINUS):
            self.navire2.change_vitesse(False)

        
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
    px.init(80,80, title="Bataille Navale", fps = 60)
    appli = Jeu()
    px.run(appli.update, appli.draw)
