from tkinter import*
import tkinter as tk


#importations des autres fichiers du projets
from page_choix import *
#/importations des autres fichiers du projets

#_____________________________________________________________________#
#______________________________Open___________________________________#
#_____________________________________________________________________#

# def photo de fond de la page
def background():
    patryck = PhotoImage(file="images/Back_finale/bg_1.gif")
    item = can.create_image((300/2),(400/2) , image = patryck)
    can.image = patryck
    can.pack()
    
def bouttons_open():
    fenetre_choix_creation()
    #fenetre_open.destroy()
    

      
#_____________________________PP__________________________________#
fenetre_open = tk.Tk()
fenetre_open.title('Votre Pokedex')

can = Canvas(fenetre_open, width = 300, height = 400, bg = 'white')
background()


photo = PhotoImage(file = r"images/divers_finale/boutons_ouvrir.gif") 
boutons_ouvrir = Button(fenetre_open, image=photo, command=bouttons_open)
boutons_ouvrir.place(x=80,y=328,width=140, height=40)