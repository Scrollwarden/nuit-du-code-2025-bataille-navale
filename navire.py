'''
Classe navire dirigé par le joueur
'''

import pyxel
from constants import *

class Navire:
    '''
    La classe Navire, objet principal du jeu.

    Les valeurs de vie, equipage et vitesse sont gérés en pourcentages.
    '''
    def __init__(self):
        # params
        self.position = [0, 0]
        self.pv = 100
        self.equipage = 100
        self.vitesse = BASE_SPEED

        # zones d'action de l'équipage
        self.combat = BASE_ACTION_FLECHES           # puissance de feu
        self.voiles = BASE_ACTION_VOILES            # direction du navire
        self.rames = BASE_ACTION_RAMES              # direction du navire
        self.soins_equipage = BASE_ACTION_SOINS     # régénération de équipage
        self.repare_coque = BASE_CALE               # brêches dans la coque

        # points endommageables, passe à False si endommagé
        self.rames = {'babord':True, 'Tribord':True}
        self.voiles = True
        self.coque = True

    def change_vitesse(self):
        """change la vitesse du navire"""
        if pyxel.btn(pyxel.KEY_UP):
            if self.vitesse <= MAX_SPEED-10:
                self.vitesse += 10
        elif pyxel.btn(pyxel.KEY_DOWN):
            if self.vitesse >= 10:
                self.vitesse -= 10

    def tir(self, type_projectile):
        """fait tirer le navire. Retourne le nombre de dégâts infligés géré dans la classe Jeu"""
        pass

    def prends_degats(self, type_degats, degats):
        """
        inflige un certain nombre de dégâts au navire. Appelé dans Jeu.

        type_degats (str) : le type de dégâts subit par le navire (flèche, flèche de feu, brise-coque)
        degats (int) : le nombre de dégâts à infliger
        """
        if type_degats in ('flèche de feu', 'brise-coque'):
            self.pv -= degats
        else:
            self.equipage -= degats
        

    def deplacement(self):
        """déplace le navire"""


    def draw(self):
        """dessine le navire à l'écran"""
        pass

    def update(self):
        """met à jour le navire dans le jeu"""
        pass