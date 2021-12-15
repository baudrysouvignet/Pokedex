from tkinter import*
import tkinter as tk
from tkinter.ttk import *
import tkinter.font as font
import sqlite3
from tkinter import ttk

class NewWindow(Toplevel): 
    def __init__(self,info, master = None):
        
        #paramétrage de la nouvelle fenetre
        
        super().__init__(master = master) 
        self.info = info
        self.title(self.info) #nom de la fenetre
        self.geometry("400x539")# taille de la fenetre
        
        can = Canvas(self, width = 400, height = 539, bg = 'white') #Canvas pour backg-
        patryck = "backs/back-"+str(self.info)+".gif" # création du lien de l'image
        patryck = PhotoImage(file= patryck) #definie l'image de bg
        item = can.create_image((400/2),(539/2) , image = patryck) #donne la position de l'image
        can.image = patryck
        can.pack()
        
        #crétion specialisé des fenetre
        if self.info == "pokedex":
                
            #hp
            value_label_hp = StringVar()
            champ_label_hp= tk.Label(self,textvariable=value_label_hp, font=("Arial", 13), bg="white")
            champ_label_hp.place(x=40,y=170,width=150, height=30)
            
            #vitesse
            value_label_vitesse= StringVar()
            champ_label_vitesse=tk.Label(self,textvariable=value_label_vitesse, font=("Arial", 13), bg="white")
            champ_label_vitesse.place(x=211,y=170,width=150, height=30)
            
            #attaque
            value_label_attaque = StringVar()
            champ_label_attaque=tk.Label(self,textvariable=value_label_attaque, font=("Arial", 13), bg="white")
            champ_label_attaque.place(x=40,y=220,width=150, height=30)
            
            #defense
            value_label_defense = StringVar()
            champ_label_defense=tk.Label(self,textvariable=value_label_defense, font=("Arial", 13), bg="white")
            champ_label_defense.place(x=211,y=220,width=150, height=30)
            
            #attaque_spe
            value_label_attaque_spe = StringVar()
            champ_label_attaque_spe=tk.Label(self,textvariable=value_label_attaque_spe, font=("Arial", 12), bg="white")
            champ_label_attaque_spe.place(x=40,y=270,width=150, height=30)
            
            #defense_spe
            value_label_defense_spe = StringVar()
            champ_label_defense_spe =tk.Label(self,textvariable=value_label_defense_spe, font=("Arial", 13), bg="white")
            champ_label_defense_spe.place(x=211,y=270,width=150, height=30)
            
            image_pokemon = tk.Label(self, image="",bg="white")
            image_pokemon.place(x=134,y=335,width=200, height=200)
            
            image_pokemon_type = tk.Label(self, image="",bg="white")
            image_pokemon_type.place(x=341,y=342,width=20, height=20)
            
            tabPokemon=RemplirListeDeroulantePokemon()
            listeDeroulantePokemon = Combobox(self, values=tabPokemon)
            listeDeroulantePokemon.current(0)
            listeDeroulantePokemon.place(x=0,y=335,width=130, height=30)
            
            def afficher(): #permet l'affichage des donnes
                AffichezPokemon(listeDeroulantePokemon.get(),value_label_hp,value_label_vitesse,value_label_attaque,value_label_defense,value_label_attaque_spe,value_label_defense_spe,image_pokemon,image_pokemon_type)
            afficher() #initialisation de l'affichege
            #bouton rechercher
            bouton_search= tk.Button(self, text="Rechercher", command=afficher, bg = "white")
            bouton_search.place(x=0,y=510,width=130, height=30)
            
            
            self.resizable(False,False)
            
            
        
        
def connexion(): #permet la conection a la bd
    try:
        #connexion à la bd
        sqliteConnection = sqlite3.connect('pokedex.db')
        return sqliteConnection
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
        

def deconnexion(sqliteConnection):
   if (sqliteConnection): 
       #fermeture de la co
            sqliteConnection.close()
def RemplirListeDeroulantePokemon():
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    
    sqlite_select_Query = "select nom from pokemon ORDER BY nom ASC" # requette sql pour la bd
    cursor.execute(sqlite_select_Query)# execution
    record = cursor.fetchall() # tout les enregistrement de la requette
    
    tabPoke = []
    
    #parcours notre tableau de retour de base de données et ajoute les éléments dans le tableau data
    for row in record:
        tabPoke.append(row[0])

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)

    #retourne le tableau
    return tabPoke

def AffichezPokemon(listeDeroulantePokemon,value_label_hp,value_label_vitesse,value_label_attaque,value_label_defense,value_label_attaque_spe,value_label_defense_spe,image_pokemon,image_pokemon_type):
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = "SELECT idPokemon,nom,HP,attaque,defense,url_image,attaque_spe,defense_spe,vitesse,libelle_type FROM pokemon INNER JOIN type  ON type.idType = pokemon.idType WHERE nom ='" + listeDeroulantePokemon + "';"
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    #la variable record est un tableau à plusieurs dimension, chaque case contient une information

    #on modifie la valeur de la StringVar "value_label_nom" avec une valeur du tableau 
    value_label_hp.set(str(record[0][2])+ " HP")
    value_label_attaque.set("Attaque: " + str(record[0][3]))
    value_label_defense.set("Defense: " + str(record[0][4]))
    value_label_attaque_spe.set("Attaque-spe: " + str(record[0][6]))
    value_label_defense_spe.set("Defense-spe: " + str(record[0][7]))
    value_label_vitesse.set("Vi: " + str(record[0][8]))
    #value_label_type.set(int(record[0][8]))

    #construction du lien de l'image
    lien_image = "images/" + str(record[0][5])
    #affichage de l'iamge
    img2 = PhotoImage(file=lien_image)
    image_pokemon.configure(image=img2)
    image_pokemon.image = img2
    
    lien_image_type = "images/type/" + str(record[0][9]) +".gif"
    #affichage de l'iamge
    img2_type = PhotoImage(file=lien_image_type)
    image_pokemon_type.configure(image=img2_type)
    image_pokemon_type.image = img2_type
    
    axz=0

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)


def lancer():
    patryck = PhotoImage(file="backs/back-intro.gif") #definie l'image de bg
    item = can.create_image((400/2),(539/2) , image = patryck) #donne la position de l'image
    
    can.image = patryck
    can.pack()
  
master = Tk() 
master.geometry("400x530")
master.title("Choix")
can = Canvas(master, width = 400, height = 539, bg = 'white') #Canvas pour backg-
lancer()

photo = PhotoImage(file='images/-btn/Btn-1.gif')
button = Button(master, image=photo)
button.place(x=1, y=1,width=80, height=80)

photo_change = PhotoImage(file = r"images/-btn/Btn-1.gif") #choix de l'image de bg
Button_change = Button(master, image=photo_change) #création du boutton (fonction)
Button_change.place(x=70,y=220,width=100, height=80) #placer et dimension
Button_change.bind("<Button>",lambda e: NewWindow("pokedex", master))


master.resizable(False,False)
mainloop() 