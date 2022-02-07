"""Een code voor het spel boter kaas en eieren."""
from time import sleep
from tkinter import Tk, Label
from functools import partial
from PIL import ImageTk, Image
import tkinter as tk
import numpy as np

def matLijst(mat):
    """Slikt een np.array in, spuugt een lijst van diens componenten uit."""
    return np.array(mat).reshape(-1,).tolist()

##class Speler:
##
##    def __init__(self, sym, value):
##        self.sym
##        self.value
##        self.im = ImageTk.PhotoImage(Image.open("{}.bmp".format(sym)))
##
##X = Speler("X", 1)
##O = Speler("O", -1)

fenetre = Tk()
fenetre.title("Boter, kaas en eieren.")
cadre = tk.Frame(fenetre, height=300, width=300)
cadre.pack()

boutons = {}

XaanZet = False

# In dit "woordenboek" wordt de stand van het spel bijgehouden.
toestand = np.zeros((3,3))


# TODO: Een hele voorriedel maken voor het spel, zoiets als:
#       Welkom bij boter kaas en eieren, het beste spel ooit!

# TODO: Deze functie documenteren.
def evSums():
    sums = []
    prodR = np.dot(toestand, np.ones((3, 1)))
    prodL = np.dot(np.ones((1, 3)), toestand)
    print("\ntoestand:\n{}".format(toestand))
    print("prodR:\n{}".format(prodR))
    print("prodL:\n{}".format(prodL))
    sums += matLijst(prodR) + matLijst(prodL)
    sums.append(toestand.trace())
    sums.append(np.flipud(toestand).trace())
    print("sums: {}\n".format(sums))
    return sums
# TODO: Deze functie uitproberen. 


# TODO: Deze functie afmaken
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

# TODO: Misschien van X en O objecten maken, en zodoende de code iets
#       inkorten.

X = ImageTk.PhotoImage(Image.open("X.bmp"))
O = ImageTk.PhotoImage(Image.open("O.bmp"))

def actie(i, j):
    """
    Verwijdert de betreffende knop en zet er een X of O voor in de plaats,
    afhankelijk van wiens beurt het is.
    """
    global XaanZet

    if XaanZet:
        plaatje = X
        kenmerk = 1
        print("\tNu is de beurt aan O!")
    else:
        plaatje = O
        kenmerk = -1
        print("\tNu is de beurt aan X!")

    # TODO: Het spel netjes onderbreken als het voorbij is.

    # Hier wordt het speelbord "grafisch" bijgewerkt.
    boutons[i,j].grid_forget()
    l = tk.Label(cadre, image=plaatje)
    l.grid(column=i,row=j)

    toestand[j,i] = kenmerk
    sums = evSums()
    
    if 3 in sums:
        raise EOFError("\tX heeft gewonnen!")
    if -3 in sums:
        raise EOFError("\tO heeft gewonnen!")

    XaanZet = not XaanZet

    if 0 not in toestand:
        raise EOFError("\tGelijk spel!")
    
    return

grootte = 5
for i in range(3):
    for j in range(3):
        boutons[i,j] = tk.Button(cadre, text='',
                                 command=partial(actie,i,j),
                                 height=grootte, width=2*grootte)
        boutons[i,j].grid(column=i,row=j)

fenetre.resizable(width=False, height=False)
# TODO: Uitzoeken waarom hiervoor niet eens een mainloop nodig is.
#       Best wel vreemd eigenlijk.

if __name__ == "__main__":

    try:
        fenetre.mainloop()
    except EOFError as e:
        print(e)
        # TODO: Hier ook de knoppen onbruikbaar maken.
    

    # Hier deed ik normaalgesproken testjes.
    pass
