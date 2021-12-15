from tkinter import*
import tkinter as tk
from tkinter.ttk import *
import tkinter.font as font
import sqlite3
from tkinter import ttk

class NewWindow(Toplevel): 
      
    def __init__(self, page_intro_f = None): 
          
        super().__init__(page_intro_f = page_intro_f) 
        self.title("New Window") 
        self.geometry("600x600")
        
        bouton_affichez_pokemon= Button(self, text="Rechercher", command=m)
        bouton_affichez_pokemon.place(x=100,y=100,width=150, height=30)
        
        label = Label(self, text ="This is the main window") 
        label = Label(self, text ="This is a new Window") 
        label.pack()

#---------------------------------------#
#---------------Fonctions---------------#
#---------------------------------------#
def lancer():
    patryck = PhotoImage(file="backs/back-intro.gif") #definie l'image de bg
    item = can.create_image((400/2),(539/2) , image = patryck) #donne la position de l'image
    
    can.image = patryck
    can.pack()

def pokedex_page():
    import pik
#---------------------------------------#
#----------Programe Principale----------#
#---------------------------------------#

page_intro_f = Tk()#cr&ation de l afenetre

can = Canvas(page_intro_f, width = 400, height = 530, bg = 'white') #Canvas pour backg-
lancer() #permet affichage du backg- et dim la fenetre


#création du premier boutton
photo_change = PhotoImage(file = r"images/-btn/Btn-1.gif") #choix de l'image de bg
Button_change = tk.Button(page_intro_f, image=photo_change) #création du boutton (fonction)
Button_change.place(x=70,y=220,width=80, height=80) #placer et dimension
Button_change.bind("<Button>",lambda e: NewWindow(page_intro_f))


page_intro_f.mainloop()