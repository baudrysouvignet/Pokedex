from tkinter import*
import tkinter as tk
from tkinter.ttk import *
import tkinter.font as font
import sqlite3
from tkinter import ttk
import datetime

class tabl:
    def __init__(self, typ, nom):
        self.type=typ
        self.nom=nom
class dresseur:
    def __init__(self, poke):
        self.poke=poke
dresseur_tete = dresseur("teteevo")

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
            
        self.resizable(False,False)
        def photo_des_tetes(photo_tete,lien_image_type):
                img2_type = PhotoImage(file=lien_image_type)
                photo_tete.configure(image=img2_type)
                photo_tete.image = img2_type
        def changer_filtre(event):
                choix_tabl_nom(self)
                
        def changertete(event):
            
                lien_image_type_2 = 'tts/'+dresseur_tete.poke+'-'+self.info+'.gif'
                if dresseur_tete.poke == "tetepika":
                    dresseur_tete.poke = "teteevo"
                else:
                    dresseur_tete.poke = "tetepika"
                tete()
                tete_page()
        def tete_page():
            lien_image_tete_page = 'tts/'+dresseur_tete.poke+'-'+self.info+'.gif'
                #affichage de l'iamge
            img2_tete_page = PhotoImage(file=lien_image_tete_page)
            image_pokemon_tete_page.configure(image=img2_tete_page)
            image_pokemon_tete_page.image = img2_tete_page
                
        image_pokemon_tete_page = tk.Label(self, image="",bg="white")
        image_pokemon_tete_page.place(x=146,y=35,width=110.53, height=100)
        tete_page()
        """bouton_search= tk.Button(self, text="Rechercher", command=changertete, bg = "white")
        bouton_search.place(x=0,y=510,width=130, height=30)"""
        #crétion specialisé des fenetre
        if self.info == "Pokedex":
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
            
        elif self.info == "Stats":
            def tetechange():
                tete_page()
            tabl_type= tabl("xx","pv")

            #création d'une variable StringVar
            var_texte_recherche = StringVar()
            textBoxRecherche = tk.Entry(self, textvariable=var_texte_recherche,bg = "#CF6B67")
            textBoxRecherche.place(x=44,y=265,width=200, height=25)
            def afficher_tabl():
                AffichezPokemon_tabl(var_texte_recherche.get(),tree)
            
            changer_filtre("event")
            #bouton de recherche
            bouton_affichez_pokemon=tk.Button(self, text="Rechercher", command=afficher_tabl,bg = "#CF6B67")
            bouton_affichez_pokemon.place(x=255,y=265,width=100, height=25)
            
            lien_image_change = 'images/btn/Btn-change.gif'
            image_pokemon_change = tk.Label(self, image="",bg="white")
            image_pokemon_change.place(x=268,y=233,width=25, height=25)           
            image_pokemon_change.bind("<Button>",changer_filtre)
            img2_change = PhotoImage(file=lien_image_change)
            image_pokemon_change.configure(image=img2_change)
            image_pokemon_change.image = img2_change

            #choix_tabl_nom()
            
            
            style = ttk.Style(self)
            style.theme_use("alt")
            style.configure("Treeview", 
                bg="#A2CD93",
                fieldbackground="white", foreground="black")
                

            tree = ttk.Treeview(self, columns=('HP', 'PV','Type'))
             
             # Set the heading (Attribute Names)
            tree.heading('#0', text='Pokemon')
            tree.heading('#1', text='HP')
            tree.heading('#2', text='PV')
            tree.heading('#3', text='Type')

            # Specify attributes of the columns (We want to stretch it!)
            tree.column('#0',width=150, stretch=YES)
            tree.column('#1',width=30, stretch=YES)
            tree.column('#2',width=70, stretch=YES)
            tree.column('#3',width=73, stretch=YES)

            #placement du tableau
            tree.place(x=24,y=295,width=353, height=240)
            
            
            AffichezPokemon_tabl(var_texte_recherche.get(),tree)
            #tree.bind('<ButtonRelease-1>', selectItem)
        elif self.info == "Profil":
            sqliteConnection = connexion()
            cursor = sqliteConnection.cursor()
            
            def recupdonnes():
                sqlite_select_Query = "SELECT idDresseur,nom,nbr_comb,nbr_vict,date,compagnon FROM dresseur "
                #execution de la requéte
                cursor.execute(sqlite_select_Query)
                #on place tout les enregistrements dans une variable record
                record = cursor.fetchall()
                
                value_label_combats.set("Combats: " + str(record[0][2]))
                value_label_vict.set("Victoires: " + str(record[0][3]))
                value_label_date.set(str(record[0][4]))
                if record[0][4]== "0":
                    date = datetime.date.today()
                    sqlite_select_Query = "UPDATE dresseur SET date = REPLACE(date, '"+(record[0][4])+"', '"+str(date)+"') WHERE date LIKE '%"+record[0][4]+"%'"
                    cursor.execute(sqlite_select_Query)
                    #on place tout les enregistrements dans une variable record
                    record = cursor.fetchall()
                    sqliteConnection.commit()
                return record
                
            def combat():
                record = recupdonnes()
                a = int(record[0][2])+1
                print(a)
                sqlite_select_Query = "UPDATE dresseur SET nbr_comb = REPLACE(nbr_comb, '"+(record[0][2])+"', '"+str(a)+"') WHERE nbr_comb LIKE '%"+record[0][2]+"%'"
                cursor.execute(sqlite_select_Query)
                #on place tout les enregistrements dans une variable record
                record = cursor.fetchall()
                sqliteConnection.commit()
                recupdonnes()
                
            def vict():
                record = recupdonnes()
                a = int(record[0][3])+1
                print(a)
                sqlite_select_Query = "UPDATE dresseur SET nbr_vict = REPLACE(nbr_vict, '"+(record[0][3])+"', '"+str(a)+"') WHERE nbr_vict LIKE '%"+record[0][3]+"%'"
                cursor.execute(sqlite_select_Query)
                #on place tout les enregistrements dans une variable record
                record = cursor.fetchall()
                sqliteConnection.commit()
                recupdonnes()
            
            def afficher_compa():
                record = recupdonnes()
                value_label_comp.set("Compagnon: " + str(record[0][5]))
                record = record[0][5]
                sqliteConnection = connexion()
                cursor = sqliteConnection.cursor()
                sqlite_select_Query = "SELECT idPokemon,nom,HP,attaque,defense,url_image,attaque_spe,defense_spe,vitesse,libelle_type FROM pokemon INNER JOIN type  ON type.idType = pokemon.idType WHERE nom ='" + record + "';"
                cursor.execute(sqlite_select_Query)
                record = cursor.fetchall()
                record = record[0][5]
                lien_image_compa = "images/" + record 
                img2_compa = PhotoImage(file=lien_image_compa)
                image_pokemon_compa.configure(image=img2_compa)
                image_pokemon_compa.image = img2_compa
                recupdonnes()
            
            def modifier_compa():
                global listeDeroulantePokemon
                record = recupdonnes()
                print(listeDeroulantePokemon_comp.get())
                sqlite_select_Query = "UPDATE dresseur SET compagnon = REPLACE(compagnon, '"+(record[0][5])+"', '"+listeDeroulantePokemon_comp.get()+"') WHERE compagnon LIKE '%"+record[0][5]+"%'"
                cursor.execute(sqlite_select_Query)
                #on place tout les enregistrements dans une variable record
                record = cursor.fetchall()
                sqliteConnection.commit()
                afficher_compa()
                recupdonnes()
            tabPokemon_comp=RemplirListeDeroulantePokemon()
            listeDeroulantePokemon_comp = Combobox(self, values=tabPokemon_comp)
            listeDeroulantePokemon_comp.current(0)
            listeDeroulantePokemon_comp.place(x=0,y=335,width=100, height=30)
            
            value_label_combats= StringVar()
            champ_label_combats=tk.Label(self,textvariable=value_label_combats, font=("Arial", 13), bg="white")
            champ_label_combats.place(x=40,y=169,width=150, height=30)
            
            value_label_vict= StringVar()
            champ_label_vict=tk.Label(self,textvariable=value_label_vict, font=("Arial", 13), bg="white")
            champ_label_vict.place(x=204,y=169,width=150, height=30)
            
            value_label_comp = StringVar()
            champ_label_comp=tk.Label(self,textvariable=value_label_comp, font=("Arial", 13), bg="white")
            champ_label_comp.place(x=40,y=219,width=150, height=30)
            
            champ_label_comp_titre=tk.Label(self,text="Compagnon", font=("Arial", 13), bg="white")
            champ_label_comp_titre.place(x=128,y=305,width=145, height=30)
            
            value_label_date = StringVar()
            champ_label_date=tk.Label(self,textvariable=value_label_date, font=("Arial", 13), bg="white")
            champ_label_date.place(x=204,y=219,width=150, height=30)
            
            bouton_search= tk.Button(self, text="changer", command=modifier_compa, bg = "white")
            bouton_search.place(x=0,y=365,width=100, height=30)
            
            image_pokemon_compa = tk.Label(self, image="",bg="white")
            image_pokemon_compa.place(x=100,y=335,width=200, height=200)
            
            lien_image_change = 'images/btn/changeimg.gif'
            image_pokemon_change = tk.Label(self, image="",bg="white")
            image_pokemon_change.place(x=256,y=135,width=20, height=20)           
            image_pokemon_change.bind("<Button>",changertete)
            img2_change = PhotoImage(file=lien_image_change)
            image_pokemon_change.configure(image=img2_change)
            image_pokemon_change.image = img2_change
            
            
            recupdonnes()
            afficher_compa()
            
tabl_type= tabl("xx","pv")         

def choix_tabl_nom(fenetre):
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
    champ_label= tk.Label(fenetre,text=("Recherche par "+ tabl_type.nom), bg="#CF6B67", justify=tk.LEFT)
    champ_label.place(x=108,y=233,width=150, height=25)
        
        
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

def AffichezPokemon_tabl(var_texte_recherche,tree):
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    #ecriture de la requéte
    sqlite_select_Query = "SELECT idPokemon,nom,HP,pv,libelle_type FROM pokemon INNER JOIN type  ON type.idType = pokemon.idType WHERE "+tabl_type.type+" LIKE '%" + var_texte_recherche + "%' ORDER BY "+tabl_type.type+" ASC"
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

photo_change = PhotoImage(file = r"images/btn/Btn-1.gif") #choix de l'image de bg
Button_change = tk.Label(master, image=photo_change ,bg="white")
Button_change.place(x=70,y=220,width=80, height=80)
Button_change.bind("<Button>",lambda e: NewWindow("Pokedex", master))



photo_change_1 = PhotoImage(file = "images/btn/Btn-2.gif") #choix de l'image de bg
Button_change_1 = tk.Label(master, image=photo_change_1 ,bg="white")
Button_change_1.place(x=250,y=220,width=80, height=80)
Button_change_1.bind("<Button>",lambda e: NewWindow("Stats", master))

photo_change_2 = PhotoImage(file = "images/btn/Btn-4.gif") #choix de l'image de bg
Button_change_2 = tk.Label(master, image=photo_change_2 ,bg="white")
Button_change_2.place(x=250,y=365,width=80, height=80)
Button_change_2.bind("<Button>",lambda e: NewWindow("Profil", master))

def tete():
    lien_image_tete = 'tts/'+dresseur_tete.poke+'-Intro.gif'
    #affichage de l'iamge
    img2_tete = PhotoImage(file=lien_image_tete)
    image_pokemon_tete.configure(image=img2_tete)
    image_pokemon_tete.image = img2_tete
image_pokemon_tete = tk.Label(master, image="",bg="white")
image_pokemon_tete.place(x=146,y=35,width=110.53, height=100)

tete()

master.resizable(False,False)
mainloop() 