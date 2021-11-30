from tkinter import*
import tkinter as tk
from tkinter.ttk import *
import tkinter.font as font
import sqlite3

class tabl:
    def __init__(self, typ, nom):
        self.type=typ
        self.nom=nom

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

def choix_tabl_nom():
    if tabl_type.nom == "Pokemon":
        tabl_type.type = "libelle_type"
        tabl_type.nom = "type"
    elif tabl_type.nom == "type":
        tabl_type.type = "pv"
        tabl_type.nom = "pv"
    elif tabl_type.nom == "pv":
        tabl_type.type = "nom"
        tabl_type.nom = "Pokemon"
    
    value_label_nom = StringVar()
    champ_label= tk.Label(fenetre,text=("Recherche par "+ tabl_type.nom), bg="#A2CD93")
    champ_label.place(x=730,y=58,width=150, height=30)

    
def AffichezPokemon_tabl():
    print(tabl_type.type)
    
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte
    sqlite_select_Query = "SELECT idPokemon,nom,HP,pv,libelle_type FROM pokemon INNER JOIN type  ON type.idType = pokemon.idType WHERE "+ tabl_type.type +" LIKE '%" + var_texte_recherche.get() + "%';"
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    #vidange du tableau
    tree.delete(*tree.get_children())
    #on parcours le tableau record pour afficher et on insert une nouvelle ligne à chaque row. 
    for row in record:
        tree.insert('', 'end', iid=str(row[0]), text=str(row[1]),values=(str(row[2]),str(row[3]),str(row[4])))
        
    #on ferme le curseur
    cursor.close()
    #deconnexion de la bdd
    deconnexion(sqliteConnection)
    
    
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
    item = can.create_image((1100/2),(600/2) , image = patryck)
     
    #Rajouter cette ligne
    can.image = patryck
     
    can.pack()
    
    
    

      
#_____________________________PP__________________________________#
fenetre = Tk()

can = Canvas(fenetre, width = 1100, height = 600, bg = 'white')
ouvrir()

b=1


#_____________________________PP__________________________________#

a=0
if a == 0 and b == 1:
    
    #liste deroulante
    tabPokemon=RemplirListeDeroulantePokemon()
    listeDeroulantePokemon = Combobox(fenetre, values=tabPokemon)
    listeDeroulantePokemon.current(0)
    listeDeroulantePokemon.place(x=77,y=234,width=200, height=30)


    #bouton rechercher
    bouton_search= tk.Button(fenetre, text="Rechercher", command=AffichezPokemon, bg = "#626DCB")
    bouton_search.place(x=292,y=234,width=150, height=30)

    #nom
    value_label_nom = StringVar()
    champ_label= tk.Label(fenetre,textvariable=value_label_nom, font=("Arial", 25),justify="right", bg="#D6C52D")
    champ_label.place(x=285,y=50,width=167, height=62)
    
    #hp
    value_label_hp = StringVar()
    champ_label_hp= tk.Label(fenetre,textvariable=value_label_hp, font=("Arial", 13), bg="#A2CD93")
    champ_label_hp.place(x=52,y=55,width=55, height=20)
    
    #vitesse
    value_label_vitesse= StringVar()
    champ_label_vitesse=tk.Label(fenetre,textvariable=value_label_vitesse, font=("Arial", 13), bg="#A2CD93")
    champ_label_vitesse.place(x=107,y=55,width=55, height=20)
    
    #attaque
    value_label_attaque = StringVar()
    champ_label_attaque=tk.Label(fenetre,textvariable=value_label_attaque, font=("Arial", 10), bg="#A2CD93")
    champ_label_attaque.place(x=318,y=120,width=150, height=15)
    
    #defense
    value_label_defense = StringVar()
    champ_label_defense=tk.Label(fenetre,textvariable=value_label_defense, font=("Arial", 10), bg="#A2CD93")
    champ_label_defense.place(x=318,y=145,width=150, height=15)
    
    #attaque_spe
    value_label_attaque_spe = StringVar()
    champ_label_attaque_spe=tk.Label(fenetre,textvariable=value_label_attaque_spe, font=("Arial", 10), bg="#A2CD93")
    champ_label_attaque_spe.place(x=318,y=170,width=150, height=15)
    
    #defense_spe
    value_label_defense_spe = StringVar()
    champ_label_defense_spe =tk.Label(fenetre,textvariable=value_label_defense_spe, font=("Arial", 10), bg="#A2CD93")
    champ_label_defense_spe.place(x=318,y=195,width=150, height=15)
    
    
    
    image_pokemon = tk.Label(fenetre, image="",bg="white")
    image_pokemon.place(x=50,y=88.19,width=93.62, height=93.62)
    
    
    image_pokemon_type = tk.Label(fenetre, image="",bg="white")
    image_pokemon_type.place(x=206,y=152,width=22, height=22)



 
"""
Partie recherche et affichage du tableau`
"""

tabl_type= tabl("xx","pv")

#création d'une variable StringVar
var_texte_recherche = StringVar()
textBoxRecherche = tk.Entry(fenetre, textvariable=var_texte_recherche,bg = "#626DCB")
textBoxRecherche.place(x=654,y=234,width=200, height=30)
#bouton de recherche
bouton_affichez_pokemon=tk.Button(fenetre, text="Rechercher", command=AffichezPokemon_tabl,bg = "#626DCB")
bouton_affichez_pokemon.place(x=864,y=234,width=150, height=30)

choix_tabl_nom()
print(tabl_type.type)

bb= "type"

photo_change = PhotoImage(file = r"images/Back/Change.gif") 
Button_change = tk.Button(fenetre, image=photo_change, command=choix_tabl_nom)
Button_change.place(x=890,y=58,width=30, height=30)

#création de la grille d'affichage (tableau)
tree = Treeview(fenetre, columns=('HP', 'PV','Type'))
 
 # Set the heading (Attribute Names)
tree.heading('#0', text='Pokemon')
tree.heading('#1', text='HP')
tree.heading('#2', text='PV')
tree.heading('#3', text='Type')

# Specify attributes of the columns (We want to stretch it!)
tree.column('#0',width=150, stretch=YES)
tree.column('#1',width=30, stretch=YES)
tree.column('#2',width=70, stretch=YES)
tree.column('#3',width=70, stretch=YES)

#placement du tableau
tree.place(x=649,y=92,width=351, height=120)


fenetre.mainloop ()