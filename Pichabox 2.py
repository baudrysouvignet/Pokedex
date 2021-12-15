from tkinter import*
from tkinter.ttk import *
import sqlite3



#--------------------------------------------#
#------------Programme Principale------------#
#--------------------------------------------#


#création de la fenetre Tkinter
fenetre=Tk()

#Canvas utiliser pour le backg-
can = Canvas(fenetre, width = 1100, height = 600, bg = 'white')
lancer() #lance la fenetre