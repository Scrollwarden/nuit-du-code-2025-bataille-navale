import pyxel

pyxel.init(256, 256, title="Bataille navale")

pyxel.load("theme.pyxres")



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

    for ligne in range(2) :
        for elt in range(4):
            pyxel.blt(235 - 25 * elt,235  - 40 * ligne,0,152 -16*elt,32 - 16*ligne,16,16)

pyxel.run(update, draw)