'''
Classe navire dirigé par le joueur
'''

import pyxel
import random
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
        self.hitbox = (LONGUEUR_NAVIRE, LARGEUR_NAVIRE)

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
        
        # autres
        self.type_fleche = 'flèche'

    def change_vitesse(self, augmente):
        """
        change la vitesse du navire
        
        augmente (bool) : si la vitesse augmente ou diminue
        """
        if self.dommages['Rames Babord'] <= 50 and ['Rames Tribord'] <= 50:
            vitesse_max = 80
        elif self.dommages['Rames Babord'] <= 33 and ['Rames Tribord'] <= 33:
            vitesse_max = 70
        elif self.dommages['Rames Babord'] <= 20 and ['Rames Tribord'] <= 20:
            vitesse_max = 60

        if self.dommages['Voiles'] <= 66:
            vitesse_max -= 50
        elif self.dommages['Voiles'] <= 33:
            vitesse_max -= 80

        inertie = 10
        if augmente:
            if self.vitesse <= vitesse_max-inertie:
                self.vitesse += inertie
        else:
            if self.vitesse >= inertie:
                self.vitesse -= inertie


    def change_orientation(self, direction):
        """
        change la direction du navire

        direction (int) : 1 UP, 2 UP-RIGHT, 3 RIGHT, 4 DOWN-RIGHT, 5 DOWN, 6 DOWN-LEFT, 7 LEFT, 8 UP-LEFT
        direction doit valoir 1 ou -1 selon droite ou gauche
        """
        if self.dommages['Rames Babord'] <= 33:
            self.direction -= 1
        if self.dommages['Rames Tribord'] <= 33:
            self.direction += 1

        self.direction += direction
        if self.direction == 0:
            self.direction = 8
        if self.direction == 9:
            self.direction = 1

    def change_type_fleche(self):
        """Change le type de flèche à celui qui n'est pas actif"""
        self.type_fleche = 'feu' if self.type_fleche == 'flèche' else 'flèche'

    def inflige_degats(self, type_degats):
        """
        fait tirer le navire. Retourne le nombre de dégâts infligés géré dans la classe Jeu
        
        type_degats (str) : parmi 'flèche' ou 'brise-coque'
        """
        if type_degats == 'flèche':
            type_degats = self.type_fleche
            if type_degats == 'feu':
                degats = BASE_DAMAGE_ARROW_FIRE * self.combat//100
            else:
                degats = BASE_DAMAGE_ARROW * self.combat//100
        elif type_degats == 'brise-coque':
            degats = BASE_DAMAGE_BRISE_COQUE
        return (type_degats, degats)

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
        if type_degats == 'feu':
            if random.randint(0, 10) <= 2:
                self.dommages['Voiles'] -= degats*2
        elif type_degats == 'brise-coque':
            if random.randint(0, 10) <= 4:
                self.dommages['Coque'] -= degats
            if random.randint(0, 10) <= 6:
                if random.randint(0, 1) == 0:
                    self.dommages['Rames Babord'] -= degats*2
                else:
                    self.dommages['Rames Tribord'] -= degats*2

    def deplacement(self):
        """déplace le navire"""
        self.position[0] += self.vitesse
        self.position[1] += self.vitesse

    def dommage_coque_cassee(self):
        """Dommages progressifs si la coque est trouée"""
        if pyxel.frame_count % 30 == 0:
            if self.dommages['Coque'] <= 50:
                self.vie -= 1
            if self.dommages['Coque'] <= 20:
                self.vie -= 2

    def repare_navire(self):
        """gère la réparation des différentes composantes du navire"""
        if pyxel.frame_count % 30 == 0:
            self.dommages['Coque'] += self.repare_coque
            self.dommages['Voiles'] += self.repare_voiles
            self.dommages['Rames Babord'] += self.repare_rames
            self.dommages['Rames Tribord'] += self.repare_rames

    def draw(self):
        """dessine le navire à l'écran"""
        x, y = self.position
        longueur, largeur = self.hitbox
        pyxel.rect(x, y, longueur, largeur)

    def update(self):
        """met à jour le navire dans le jeu"""
        self.deplacement()
        self.dommage_coque_cassee()