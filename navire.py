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
    - direction (int) : 0 UP, 1 UP-RIGHT, 2 RIGHT, 3 DOWN-RIGHT, 4 DOWN, 5 DOWN-LEFT, 6 LEFT, 7 UP-LEFT
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
        self.equipage_libre = BASE_ACTION_LIBRE     # équipage réassignable
        self.combat = BASE_ACTION_FLECHES           # puissance de feu
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

    def __str__(self):
        return 'Navire'
    
    def assigne_equipage(self, poste):
        """
        assigne 1% de l'équipage à un poste. Cet équipage doit être libre avant

        poste (str) : le poste auquel le pourcentage d'équipage est assigné,
        parmi libre, combat, rames, soins, repare coque, repare voiles, repare rames
        """
        equipage_max = self.equipage
        equipage_libre = self.equipage_libre
        equipage_combat = self.combat
        equipage_rames = self.rames
        equipage_soins = self.soins_equipage
        equipage_reparation_coque = self.repare_coque
        equipage_reparation_voiles = self.repare_voiles
        equipage_reparation_rames = self.repare_rames

    def reorganiser_equipage(self):
        """réorganise l'équipage en fonction des pertes"""
        equipage_max = self.equipage
        equipage_libre = self.equipage_libre
        equipage_combat = self.combat
        equipage_rames = self.rames
        equipage_soins = self.soins_equipage
        equipage_reparation_coque = self.repare_coque
        equipage_reparation_voiles = self.repare_voiles
        equipage_reparation_rames = self.repare_rames

        equipage_employe = equipage_libre + equipage_rames + equipage_combat + equipage_soins + equipage_reparation_coque + equipage_reparation_rames + equipage_reparation_voiles
        if equipage_max < equipage_employe:
            equipage_libre -= (equipage_employe - equipage_max)
            if equipage_libre < 0:
                equipage_combat -= equipage_libre
                equipage_libre = 0
                if equipage_combat < 0:
                    equipage_reparation_voiles -= equipage_combat
                    equipage_combat = 0
                    if equipage_reparation_voiles < 0:
                        equipage_reparation_voiles = 0 # aucun autre homme sur le pont ne peut être touché

        equipage_libre += equipage_soins//2 # deux hommes pour en soigner un

        self.equipage_libre = equipage_libre
        self.combat = equipage_combat
        self.repare_voiles = equipage_reparation_voiles
        
    def defini_vitesse_max(self, vitesse_max):
        """définie la vitesse maximale en fonction des dommages subits"""
        if self.dommages['Rames Babord'] <= 50 and ['Rames Tribord'] <= 50:
            vitesse_max -= 10
        elif self.dommages['Rames Babord'] <= 33 and ['Rames Tribord'] <= 33:
            vitesse_max -= 20
        elif self.dommages['Rames Babord'] <= 20 and ['Rames Tribord'] <= 20:
            vitesse_max -= 30

        if self.dommages['Voiles'] <= 66:
            vitesse_max -= 40
        elif self.dommages['Voiles'] <= 33:
            vitesse_max -= 60
        elif self.dommages['Voiles'] <= 10:
            vitesse_max -= 80

        if vitesse_max < 0:
            vitesse_max = 0

        return vitesse_max

    def change_vitesse(self, augmente):
        """
        change la vitesse du navire
        
        augmente (bool) : si la vitesse augmente ou diminue
        """
        vitesse_max = self.defini_vitesse_max(100)

        if augmente:
            if self.vitesse <= vitesse_max-INERTIE:
                self.vitesse += INERTIE
        else:
            if self.vitesse >= INERTIE:
                self.vitesse -= INERTIE

    def change_orientation(self, direction):
        """
        change la direction du navire

        direction (int) : 0 UP, 1 UP-RIGHT, 2 RIGHT, 3 DOWN-RIGHT, 4 DOWN, 5 DOWN-LEFT, 6 LEFT, 7 UP-LEFT
        direction doit valoir 1 ou -1 selon droite ou gauche
        """
        if self.dommages['Rames Babord'] <= 33:
            self.direction -= 1
        if self.dommages['Rames Tribord'] <= 33:
            self.direction += 1

        self.direction += direction
        if self.direction == -1:
            self.direction = 7
        if self.direction == 8:
            self.direction = 0

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
            self.vitesse = 20
            if random.randint(0, 10) <= 4:
                self.dommages['Coque'] -= degats
            if random.randint(0, 10) <= 6:
                if random.randint(0, 1) == 0:
                    self.dommages['Rames Babord'] -= degats*2
                else:
                    self.dommages['Rames Tribord'] -= degats*2
        elif type_degats == 'flèche':
            if random.randint(0, 10) <= 1:
                self.dommages['Voiles'] -= degats//4

    def deplacement(self):
        """déplace le navire"""
        if pyxel.frame_count % 30 == 0:
            direction = self.direction
            mouvement = self.vitesse/50
            if direction == 0:
                self.position[0] -= mouvement
            elif direction == 1:
                self.position[0] -= mouvement
                self.position[1] += mouvement
            elif direction == 2:
                self.position[1] += mouvement
            elif direction == 3:
                self.position[0] += mouvement
                self.position[1] += mouvement
            elif direction == 4:
                self.position[0] += mouvement
            elif direction == 5:
                self.position[0] += mouvement
                self.position[1] -= mouvement
            elif direction == 6:
                self.position[1] -= mouvement
            else:
                self.position[0] -= mouvement
                self.position[1] -= mouvement

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
        orientation = self.direction * 45
        pyxel.blt(x, y, 0, 0, 0, 88, 48, colkey=0, rotate=orientation)

    def update(self):
        """met à jour le navire dans le jeu"""
        self.deplacement()
        self.reorganiser_equipage()
        self.dommage_coque_cassee()