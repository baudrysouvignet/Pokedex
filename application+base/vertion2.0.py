from tkinter import*
import tkinter as tk
from tkinter.ttk import *
import tkinter.font as font
import sqlite3

def connexion():
    try:
        #connexion à la bdd
        sqliteConnection = sqlite3.connect('pokedex.db')
        return sqliteConnection
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

"""<summary>Fonction de connexion à la bdd</summary>
"""
def deconnexion(sqliteConnection):
   if (sqliteConnection):
       #fermeture de la co
            sqliteConnection.close()
            print("The SQLite connection is closed")

def RemplirListeDeroulantePokemon():
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte
    sqlite_select_Query = "select nom from pokemon ORDER BY nom ASC"
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    #declaration du tableau qui va contenir les données a afficher dans la liste déroulante
    tabPoke = []
    #parcours notre tableau de retour de base de données et ajoute les éléments dans le tableau data
    for row in record:
        tabPoke.append(row[0])

    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)

    #retourne le tableau
    return tabPoke

def init():
    fene_info = tk.Toplevel()
    return fene_info

def AffichezPokemon():
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte, on récupére le contenu de la listeDeroulante avec la fonction .get()
    sqlite_select_Query = "SELECT idPokemon,nom,HP,attaque,defense,url_image,attaque_spe,defense_spe,vitesse,libelle_type FROM pokemon INNER JOIN type  ON type.idType = pokemon.idType WHERE nom ='" + listeDeroulantePokemon.get() + "';"
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    #la variable record est un tableau à plusieurs dimension, chaque case contient une information

    #on modifie la valeur de la StringVar "value_label_nom" avec une valeur du tableau
    value_label_nom.set(record[0][1])   
    value_label_hp.set("HP: "+ str(record[0][2]))
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


def ouvrir():
    patryck = PhotoImage(file="images/Back/Framevert.gif")
    item = can.create_image((550/2),(325/2) , image = patryck)
     
    #Rajouter cette ligne
    can.image = patryck
     
    can.pack()
    
    axz=1

def infos(can_info,fene_info ):
    patrycbis_back = PhotoImage(file="images/Back/Framevide.gif")
    itembis_back = can_info.create_image((550/2),(325/2) , image = patrycbis_back)
     
    #Rajouter cette ligne
    can_info.imagebis_back = patrycbis_back
     
    can_info.pack()
    
    patrycbis = PhotoImage(file="images/Back/Frame-stats.gif")
    itembis = can_info.create_image((450/2)+50,(225/2)+50 , image = patrycbis)
     
    #Rajouter cette ligne
    can_info.imagebis = patrycbis
     
    can_info.pack()
    
    

      
#_____________________________PP__________________________________#
fenetre = Tk()

can = Canvas(fenetre, width = 550, height = 325, bg = 'white')
ouvrir()
#bouton rechercher
def info_geo():
    fene_info = init()
    fene_info.geometry('550x325')
    can_info = Canvas(fene_info, width = 550, height = 325, bg = 'white')
    a=0
    
    infos(can_info,fene_info)
    return a, can_info, fene_info

def nombre(v):
    global a
    a=v

print(a)

b=1


#_____________________________PP__________________________________#
print(a)       
photo = PhotoImage(file = r"images/Back/statsbtn.gif") 
btn = tk.Button(fenetre, image=photo, command=lambda *args:nombre(0))
btn.place(x=65,y=72,width=200, height=80)

photot = PhotoImage(file = r"images/Back/rechercher.gif") 
btnt = tk.Button(fenetre, image=photot)
btnt.place(x=285,y=72,width=200, height=80)


if a == 0 and b == 1:
    a, can_info, fene_info = info_geo()
    
    #liste deroulante
    tabPokemon=RemplirListeDeroulantePokemon()
    listeDeroulantePokemon = Combobox(fene_info, values=tabPokemon)
    listeDeroulantePokemon.current(0)
    listeDeroulantePokemon.place(x=77,y=234,width=200, height=30)


    #bouton rechercher
    bouton_search= tk.Button(fene_info, text="Rechercher", command=AffichezPokemon, bg = "black")
    bouton_search.place(x=292,y=234,width=150, height=30)

    #nom
    value_label_nom = StringVar()
    champ_label= tk.Label(fene_info,textvariable=value_label_nom, font=("Arial", 30),justify="right", bg="#D6C52D")
    champ_label.place(x=285,y=50,width=215, height=62)
    
    #hp
    value_label_hp = StringVar()
    champ_label_hp= tk.Label(fene_info,textvariable=value_label_hp, font=("Arial", 15), bg="#A2CD93")
    champ_label_hp.place(x=52,y=55,width=55, height=20)
    
    #vitesse
    value_label_vitesse= StringVar()
    champ_label_vitesse=tk.Label(fene_info,textvariable=value_label_vitesse, font=("Arial", 15), bg="#A2CD93")
    champ_label_vitesse.place(x=107,y=55,width=55, height=20)
    
    #attaque
    value_label_attaque = StringVar()
    champ_label_attaque=tk.Label(fene_info,textvariable=value_label_attaque, font=("Arial", 10), bg="#A2CD93")
    champ_label_attaque.place(x=318,y=120,width=150, height=15)
    
    #defense
    value_label_defense = StringVar()
    champ_label_defense=tk.Label(fene_info,textvariable=value_label_defense, font=("Arial", 10), bg="#A2CD93")
    champ_label_defense.place(x=318,y=145,width=150, height=15)
    
    #attaque_spe
    value_label_attaque_spe = StringVar()
    champ_label_attaque_spe=tk.Label(fene_info,textvariable=value_label_attaque_spe, font=("Arial", 10), bg="#A2CD93")
    champ_label_attaque_spe.place(x=318,y=170,width=150, height=15)
    
    #defense_spe
    value_label_defense_spe = StringVar()
    champ_label_defense_spe =tk.Label(fene_info,textvariable=value_label_defense_spe, font=("Arial", 10), bg="#A2CD93")
    champ_label_defense_spe.place(x=318,y=195,width=150, height=15)
    
    
    
    image_pokemon = Label(fene_info, image="")
    image_pokemon.place(x=50,y=88.19,width=93.62, height=93.62)
    
    
    image_pokemon_type = tk.Label(fene_info, image="",bg="white")
    image_pokemon_type.place(x=206,y=151,width=22, height=22)


  
 
fenetre.mainloop ()