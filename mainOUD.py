"""Een code voor het spel boter kaas en eieren."""

from tkinter import Tk, Label
from functools import partial
from PIL import ImageTk, Image
import tkinter as tk

fenetre = Tk()
fenetre.title("Boter, kaas en eieren.")

X = ImageTk.PhotoImage(Image.open("X.bmp"))  # PIL solution
O = ImageTk.PhotoImage(Image.open("O.bmp"))  # PIL solution

print("Tot nu toe is alles goed gegaan.")
frame = tk.Frame(fenetre, height=300, width=300)

cadre.pack()

 = {}

XaanZet = False

def actie(i, j):
    """
    Verwijdert de betreffende knop en zet er een X of O voor in de plaats,
    afhankelijk van wiens beurt het is.
    """
    boutons[i,j].grid_forget()
    if XaanZet:
        sym = X 
    else:
        sym = O
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

fenetre.resizable(width=False,height=False)
fenetre.mainloop() # Lancement de la boucle principale

if __name__ == "__main__":

    print("Hier testen we ons spel.")
    
