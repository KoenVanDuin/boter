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

# Hier wordt het (lege) venster gemaakt
window = Tk()
window.title("Boter, kaas en eieren.")
frame = tk.Frame(window, height=300, width=300)
frame.pack()

buttons = {}

XaanZet = False

# Een 3x3 matrix waarin de stand van het spel wordt bijgehouden:
# 0 staat voor een leeg vakje, -1 staat voor O, en 1 voor X.
toestand = np.zeros((3,3))

def evSums():
    """
    Hiermee schatten we in met matrixmanipulaties een lijst van indices
    gemaakt die aangeeft of X of O gewonnen heeft.
    De lijst van indices wordt teruggestuurd.
    """
    sums = []
    prodR = np.dot(toestand, np.ones((3, 1)))
    prodL = np.dot(np.ones((1, 3)), toestand)
##    print("\ntoestand:\n{}".format(toestand))
##    print("prodR:\n{}".format(prodR))
##    print("prodL:\n{}".format(prodL))
    sums += matLijst(prodR) + matLijst(prodL)
    sums.append(toestand.trace())
    sums.append(np.flipud(toestand).trace())
##    print("sums: {}\n".format(sums))
    return sums

X = ImageTk.PhotoImage(Image.open("X.bmp"))
O = ImageTk.PhotoImage(Image.open("O.bmp"))
leeg = ImageTk.PhotoImage(Image.open("leeg.bmp"))

def actie(i, j):
    """
    Verwijdert de betreffende knop en zet er een X of O voor in de plaats,
    afhankelijk van wiens beurt het is.
    Werkt verder de toestand van het spel bij
    """
    global XaanZet

    if XaanZet:
        plaatje = X
        kenmerk = 1
    else:
        plaatje = O
        kenmerk = -1

    # Hier wordt het speelbord "grafisch" bijgewerkt.
    buttons[i,j].grid_forget()
    del buttons[i,j]
    l = tk.Label(frame, image=plaatje)
    l.grid(column=i,row=j)

    # Het bijwerken van de toestand.
    toestand[j,i] = kenmerk
    sums = evSums()

    # Nakijken of het spel niet ten einde is.
    try:    
        if 3 in sums:
            raise EOFError("X heeft gewonnen!")
        elif -3 in sums:
            raise EOFError("O heeft gewonnen!")

        XaanZet = not XaanZet

        if 0 not in toestand:
            raise EOFError("Gelijk spel!")

    # Het einde van het spel afhandelen,
    # als het geval is voordoet.
    except EOFError as e:
        print("-"*50)
        sleep(0.5)
        print(e)
        for key in buttons.keys():
            buttons[key].grid_forget()
            l = tk.Label(frame, image=leeg)
            l.grid(column=key[0],row=key[1])
    else:
        if XaanZet:
            print("Nu is X aan zet!")
        else:
            print("Nu is O aan zet!")
            
    return

#   Hier wordt het hele venster in elkaar gezet,
#   inclusief knoppen en hun werking.

size = 5
for i in range(3):
    for j in range(3):
        buttons[i,j] = tk.Button(frame, text='',
                                 command=partial(actie,i,j),
                                 height=size, width=2*size)
        buttons[i,j].grid(column=i,row=j)

window.resizable(width=False, height=False)

if __name__ == "__main__":

    print("Welkom bij Boter kaas en Eieren, het beste spel ooit!")
    print("-"*50)
    sleep(0.5)
    print("O begint.")
    window.mainloop()
   
