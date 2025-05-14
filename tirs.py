import pyxel

pyxel.init(256, 256, title="Tirs")
touche = pyxel.KEY_SPACE
liste_des_tirs = []

x1 =128
y1 =128

x2 = 15
y2= 200

def gestion_tirs(x1, y1, x2, y2, liste_des_tirs):
    """création et déplacement des tirs"""
    if pyxel.btnr(touche) :
        liste_des_tirs.append([x1, y1]) #il faut ajuster x et y
    for tir in liste_des_tirs :
        if tir[0] > x2:
            tir[0] -= 1
        if tir[0] < x2:
            tir[0] += 1
        if tir[1] > y2:
            tir[1] -= 1
        if tir[1] < y2:
            tir[1] += 1
        if tir[0] == x2 and tir[1] == y2:
            liste_des_tirs.remove(tir)
    return liste_des_tirs



def update():
    """mise à jour des variables (30 fois par seconde)"""
    global liste_des_tirs
    liste_des_tirs = gestion_tirs(x1, y1 , x2, y2,liste_des_tirs)


def draw():
    """onnnnnnn desssssssssssine"""
    pyxel.cls(0)
    for tir in liste_des_tirs :
        pyxel.rect(tir[0], tir[1], 1, 8,13)

pyxel.run(update,draw )
