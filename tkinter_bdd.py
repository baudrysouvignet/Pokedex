from tkinter import*
import sqlite3


def connexion():
    try:
        #connexion à la bdd
        sqliteConnection = sqlite3.connect('pays.db')
        return sqliteConnection
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def deconnexion(sqliteConnection):
   if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

            
def testRequete():
    connexion()
    sqliteConnection = connexion()
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")
    #ecriture de la requéte
    sqlite_select_Query = "select * from city where name ='Paris';"
    #execution de la requéte
    cursor.execute(sqlite_select_Query)
    #on place tout les enregistrements dans une variable record
    record = cursor.fetchall()
    value_label.set(record[0][1])
    print("SQLite Database Version is: ", record)
    #on ferme le curseur
    cursor.close()
    deconnexion(sqliteConnection)


fenetre=Tk()
#permet de modifier la taille de la fenétre
fenetre.geometry("400x400")

#On crée un label(lignedetexte) souhaitant labienvenue
#Note:lepremier paramètre passé au constructeur de Label est notre fenétre
bouton_quitter=Button(fenetre, text="Quitter", command=testRequete)
bouton_quitter.pack()
value_label = StringVar()
champ_label=Label(fenetre,textvariable=value_label)
#On affiche le label dans la fenêtre
champ_label.place(x=20,y=200,width=200, height=85)
#On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()





