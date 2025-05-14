import pyxel

pyxel.init(256, 256, title="Bataille navale")

pyxel.load("theme.pyxres")
fleche_feu_j1 =False
fleche_feu_j2 =True

def update():
    """mise à jour des variables (30 fois par seconde)"""
    pass


def draw():
    """création des objets (30 fois par seconde)"""
    pyxel.cls(0)
    pyxel.blt(84, 104, 0, 0, 0, 88, 48) # bateau
    for ligne in range(2) :
        for elt in range(4):
            pyxel.blt(4 + 25 * elt,2 + 40 * ligne,0,88 +16*elt,0 + 16*ligne,16,16)
    if fleche_feu_j1 == True :
        pyxel.blt(79,2,0,152,0,16,16)

    for ligne in range(2) :
        for elt in range(4):
            pyxel.blt(160+ 25 * elt,170  +40 * ligne,0,88 +16*elt,0 + 16*ligne,16,16)
    if fleche_feu_j2 == True :
        pyxel.blt(235,170,0,152,0,16,16)


pyxel.run(update, draw)