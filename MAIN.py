import mysql.connector
import sys
sys.path.append('./classe')
from classe.Categorie import *
from classe.Produit import *
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo



#Ouverture de la base de Données
datab= mysql.connector.connect(
	host="localhost",
	user="root",
	password="root",
	database="boutique"
	)



#Fenêtre principale
win = Tk()
win.title('Gestionnaire de Stock')
win.configure(bg =  "grey")
window_width = 600
window_height = 300
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#ajouter produit
addnom = Entry(win)
addnom.insert(0, "Nom")


adddesc = Entry(win)
adddesc.insert(0, "Description")


addprix = Entry(win)
addprix.insert(0, "Prix")

addqty = Entry(win)
addqty.insert(0, "Quantité")

addid_cat = Entry(win)
addid_cat.insert(0, "Catégorie")

addnom.grid(row=1, column=1, pady=5, padx= 15)
adddesc.grid(row=2,column=1, pady=5, padx= 15)
addprix.grid(row=3,column=1, pady=5, padx= 15)
addqty.grid(row=4,column=1, pady=5, padx= 15)
addid_cat.grid(row=5,column=1, pady=5, padx= 15)


def ajouterProd():
	datab = mysql.connector.connect(
		host="localhost",
		user="root",
		password="root",
		database="boutique"
	)
	nom = addnom.get()
	desc = adddesc.get()
	prix = addprix.get()
	qty = addqty.get()
	cat = addid_cat.get()

	cur = datab.cursor()
	cur.execute(f"INSERT INTO produit (nom, description, prix, quantite, id_categorie) values ('{nom}', '{desc}', {prix}, {qty}, {cat});")
	datab.commit()
	cur.close()

###fin ajouter produit


#enlever produit
delID = Entry(win)
delID.insert(0, "ID à modifier ou supprimer")

delID.grid(row=3, column=2, pady=5, padx=10)


def enleverProd():
	datab = mysql.connector.connect(
		host="localhost",
		user="root",
		password="root",
		database="boutique"
	)


	ID = delID.get()

	cur = datab.cursor()
	cur.execute(f"DELETE FROM produit where id = {ID};")
	datab.commit()
	cur.close()

###fin enlever produit


#Altération de stock
alternom = Entry(win)
alternom.insert(0, "Nom à modifier")
alterdescr = Entry(win)
alterdescr.insert(0, "Description à modifier")
alterprix = Entry(win)
alterprix.insert(0, "Prix à modifier")
alterqty = Entry(win)
alterqty.insert(0, "Quantité à modifier")
alterid_cat = Entry(win)
alterid_cat.insert(0, "Catégorie à modifier")

alternom.grid(row=1, column=3, pady=5, padx= 15)
alterdescr.grid(row=2,column=3, pady=5, padx= 15)
alterprix.grid(row=3,column=3, pady=5, padx= 15)
alterqty.grid(row=4,column=3, pady=5, padx= 15)
alterid_cat.grid(row=5,column=3, pady=5, padx= 15)

def alterProd():
	datab = mysql.connector.connect(
		host="localhost",
		user="root",
		password="root",
		database="boutique"
	)

	nouveaunom = alternom.get()
	nouveldescr = alterdescr.get()
	nouveauprix = alterprix.get()
	nouvelqty = alterqty.get()
	nouvelcat = alterid_cat.get()

	alterID = delID.get()

	cur = datab.cursor()
	cur.execute(f"UPDATE produit set nom = '{nouveaunom}', description = '{nouveldescr}', prix = {nouveauprix}, quantite = {nouvelqty}, id_categorie = {nouvelcat} where id = {alterID};")
	datab.commit()
	cur.close()

###Fin altération

bouton_ajout = Button(win, text = "Ajouter un produit au stock.", command = ajouterProd).grid(row=6,column=1, pady=5, padx= 15)

bouton_supprimer = Button(win, text = "Supprimer un produit du stock.", command = enleverProd).grid(row=6,column=2, pady=5, padx= 15)

bouton_modifier = Button(win, text = "Modifier un produit du stock.", command = alterProd).grid(row=6,column=3, pady=5, padx= 15)




def afficherStock():



	Stock = Toplevel()
	Stock.title('Affichage du Stock')
	Stock.configure(bg =  "grey")
	screen_width = win.winfo_screenwidth()
	screen_height = win.winfo_screenheight()
	center_x = int(screen_width / 2 - window_width / 2)
	center_y = int(screen_height / 2 - window_height / 2)
	Stock.geometry('1300x300')
	curs = datab.cursor()

	colone = ('ID', 'Nom', 'Description', 'Prix', 'Quantite', 'Categorie')

	tableur = ttk.Treeview(Stock, columns=colone, show='headings')

	tableur.heading('ID', text='ID')
	tableur.heading('Nom', text='Nom')
	tableur.heading('Description', text='Description')
	tableur.heading('Prix', text='Prix')
	tableur.heading('Quantite', text='Quantité')
	tableur.heading('Categorie', text='Catégorie')

	curs.execute("SELECT * FROM produit")
	for produit in curs:
		tableur.insert('',END, values=produit)

	tableur.grid(row=0, column=0, sticky='nsew')
	tableur.column(col, anchor=CENTER)

	scrollbar = ttk.Scrollbar(Stock, orient=VERTICAL, command=tableur.yview)
	tableur.configure(yscroll=scrollbar.set)
	scrollbar.grid(row=0, column=1, sticky='ns')

	Stock.mainloop()
	curs.close()

stock_afficher = Button(win, text= "Afficher le stock.", command=afficherStock).grid(row= 8, column=2, pady=50, padx=15)


win.mainloop()
#tk.Label(win, text='CRUD des Produits', bg = 'grey').pack()

# a = Entry(win, width = 15)
# a.pack()