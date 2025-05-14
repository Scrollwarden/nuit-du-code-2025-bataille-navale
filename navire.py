'''
Classe navire dirigé par le joueur
'''

import pyxel
from constants import *

class Navire:
    '''
    La classe Navire, objet principal du jeu.

    Les valeurs sont gérées en pourcentages.
    
    ATTRIBUTS
    - direction (int) : 1 UP, 2 UP-RIGHT, 3 RIGHT, 4 DOWN-RIGHT, 5 DOWN, 6 DOWN-LEFT, 7 LEFT, 8 UP-LEFT
    - position (list[int]) : position [x, y]
    '''
    def __init__(self, direction, position):
        # vies
        self.vie = 100
        self.equipage = 100
        self.hitbox = (position[0], position[1], LONGUEUR_NAVIRE, LARGEUR_NAVIRE)

        # mouvement
        self.vitesse = BASE_SPEED
        self.position = position
        self.direction = direction

        # zones d'action de l'équipage
        self.combat = BASE_ACTION_FLECHES           # puissance de feu
        self.voiles = BASE_ACTION_VOILES            # direction du navire
        self.rames = BASE_ACTION_RAMES              # direction du navire
        self.soins_equipage = BASE_ACTION_SOINS     # régénération de équipage
            # zones d'action de réparage
        self.repare_coque = BASE_REPARE_COQUE       # brêches dans la coque
        self.repare_voiles = BASE_REPARE_VOILES     # voiles détruites
        self.repare_rames = BASE_REPARE_RAMES       # rames détruites

        # points endommageables
        self.dommages = {'Rames Babord':100,
                         'Rames Tribord':100,
                         'Coque': 100,
                         'Voiles': 100}

    def change_vitesse(self):
        """change la vitesse du navire"""
        inertie = 10
        if self.vitesse <= MAX_SPEED-inertie:
            self.vitesse += inertie
        if self.vitesse >= inertie:
            self.vitesse -= inertie

    def change_orientation(self, direction):
        """
        change la direction du navire

        direction (int) : 1 UP, 2 UP-RIGHT, 3 RIGHT, 4 DOWN-RIGHT, 5 DOWN, 6 DOWN-LEFT, 7 LEFT, 8 UP-LEFT
        direction doit valoir 1 ou -1
        """
        self.direction += direction
        if self.direction == 0:
            self.direction = 8
        if self.direction == 9:
            self.direction = 1

    def inflige_degats(self, type_projectile):
        """
        fait tirer le navire. Retourne le nombre de dégâts infligés géré dans la classe Jeu
        
        type_projectile (str) : parmi 'flèche', 'feu', 'brise-coque'
        """
        if type_projectile == 'flèche':
            degats = BASE_DAMAGE_ARROW * self.combat
        elif type_projectile == 'feu':
            degats = BASE_DAMAGE_ARROW_FIRE * self.combat
        return (type_projectile, degats)

    def prends_degats(self, type_degats, degats):
        """
        inflige un certain nombre de dégâts au navire. Appelé dans Jeu.

        type_degats (str) : le type de dégâts subit par le navire (flèche, feu ou brise-coque)
        degats (int) : le nombre de dégâts à infliger
        """
        # dégâts purs
        if type_degats in ('feu', 'brise-coque'):
            self.vie -= degats
        else:
            self.equipage -= degats
        
        # composantes endommagées
        pass

    def deplacement(self):
        """déplace le navire"""
        self.position[0] += self.vitesse
        self.position[1] += self.vitesse


    def draw(self):
        """dessine le navire à l'écran"""
        pass

    def update(self):
        """met à jour le navire dans le jeu"""
        pass