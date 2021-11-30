from tkinter import*
import tkinter as tk


#_____________________________________________________________________#
#______________________________Choix__________________________________#
#_____________________________________________________________________#


def fenetre_choix_creation():
    global photo, boutons_ouvrir
    fenetre_choix = tk.Toplevel()
    fenetre_choix.title('Laisse toi guidée')
    
    can = Canvas(fenetre_choix, width = 300, height = 400, bg = 'white')


    patryck = PhotoImage(file="images/Back_finale/bg_2.gif")
    item = can.create_image((300/2),(400/2) , image = patryck)
    can.image = patryck
    can.pack()
