'''
Classe jeu
'''
import pyxel as px
import Navire


class Jeu:
     
    def __init__(self):

        self.navire1 = Navire()
        self.navire2 = Navire()
     
    def update(self):
        """met à jour le jeu"""
        
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
