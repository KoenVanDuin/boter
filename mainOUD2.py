"""Een code voor het spel boter kaas en eieren."""
from time import sleep
from tkinter import Tk, Label
from functools import partial
from PIL import ImageTk, Image
import tkinter as tk
import numpy as np

# HERV: Ik heb net een klasse gemaakt van spelers.
#       Nu nog de code daarop aanpassen,
#       en verder de klasse groter maken, als daarmee de coder mooier wordt.

class Speler:

    def __init__(self, sym, value):
        self.sym
        self.value
        self.im = ImageTk.PhotoImage(Image.open("{}.bmp".format(sym)))

X = Speler("X", 1)
O = Speler("O", -1)

fenetre = Tk()
fenetre.title("Boter, kaas en eieren.")

X = ImageTk.PhotoImage(Image.open("X.bmp"))  # PIL solution
O = ImageTk.PhotoImage(Image.open("O.bmp"))  # PIL solution

print("Tot nu toe is alles goed gegaan.")
cadre = tk.Frame(fenetre, height=300, width=300)

cadre.pack()

boutons = {}

XaanZet = False

# TODO: van X en O misschien toch objecten maken?

# In dit "woordenboek" wordt de stand van het spel bijgehouden.
toestand = np.zeros((3,3))


# TODO: Een hele voorriedel maken voor het spel, zoiets als:
#       Welkom bij boter kaas en eieren, het beste spel ooit!

# TODO: Deze functie definiëren
def evSums():
    sums = []
    sums += list(toestand * np.ones(3, 1))
    sums += list(np.ones(3, 1) * toestand)
    sums.append(toestand.trace())
    sums.append(np.flipud(toestand).trace())
    return sums
# TODO: Deze functie uitproberen. 


def evToestand():
    if 1==0:
        print("gelijk spel!")
        # TODO: spel beëindigen
    elif 1==0:
        print("X wint!")
        # TODO: spel beëindigen.
    elif 1==0:
        print("O wint!")
        # TODO: spel beëindigen.

def gelijk():
    raise NotImplementedError

# TODO: Misschien van X en O objecten maken, en zodoende de code iets
#       inkorten.

def actie(i, j):
    """
    Verwijdert de betreffende knop en zet er een X of O voor in de plaats,
    afhankelijk van wiens beurt het is.
    """
    # TODO: Het spel onderbreken als het voorbij is.
    boutons[i,j].grid_forget()
    sums = evSums()
    if XaanZet:
        sym = X
        if 3 in sums:
            raise Exception("X heeft gewonnen!")
            # TODO: Hier met hele spel stoppen ofzo?
        print("X is aan zet!")
    else:
        sym = O
        if -3 in sums:
            raise Exception("O heeft gewonnen!")
    print("{} is aan zet!".format(sym))
    global XaanZet
    XaanZet = not XaanZet
    l = tk.Label(cadre, image=sym)
    l.grid(column=i,row=j)
    return

# TODO: Kijken of dit wel echt met een woordenboek moet gebeuren.
#       Misschien kunnen we zonder een woordenboek uitkomen.

grootte = 5
for i in range(3):
    for j in range(3):
        boutons[i,j] = tk.Button(cadre, text='',
                                 command=partial(actie,i,j),
                                 height=grootte, width=2*grootte)
        boutons[i,j].grid(column=i,row=j)

fenetre.resizable(width=False, height=False)
#fenetre.mainloop()

if __name__ == "__main__":

    print("Konijnen hebben oren")

##    mat = np.matrix([[0, -1, -1], [1, 0, -1], [1, 1, -1]])
##    print("hier is te matrix.")
##    print(mat)
##    print("We kijken nu of 1 er in zit.")
##    print(1 in mat)
##    print("We kijken nu of 0 er in zit.")
##    print(0 in mat)
##    print("We kijken nu of -1 er in zit.")
##    print(-1 in mat)
##    print("We kijken nu of 2 er in zit.")
##    print(2 in mat)
##    print("-"*30)
##    print("Nu klugelen met matrixproducten")
##    print("Hier eerst even een enenvector.")
##    rij1 = np.ones((1,3))
##    kol1 = np.ones((3,1))
##    print("rij1 = {}".format(rij1))
##    print("kol1 = {}".format(kol1))
##    print("mat*kol1 = {}".format(mat*kol1))
##    print("rij1*mat = {}".format(rij1*mat))
##    print("-"*30)
##    print("Ik kiep de matrix ondersteboven:")
##    print(np.flipud(mat))

##    print("Oké, tout se passe comme prévu!")
