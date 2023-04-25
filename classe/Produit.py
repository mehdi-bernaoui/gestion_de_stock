import mysql.connector

class CRUDproduit:
	def __init__(self):
		self.datab = mysql.connector.connect(
			host="localhost",
			user="root",
			password="root",
			database="boutique"
		)

	def Create(self, nom, desc, prix, qty, cat):
		cur = self.datab.cursor()
		cur.execute(f"INSERT INTO produit (nom, description, prix, quantite, id_categorie) values ('{nom}', '{desc}', {prix}, {qty}, {cat});")
		self.datab.commit()
		cur.close()

	def Read(self):
		cur = self.datab.cursor()
		cur.execute(f"SELECT * FROM produit;")
		res = cur.fetchall()
		for line in res:
			print(line)
		cur.close()

	def Update(self, nom, condition, nouveauNom):
		cur = self.datab.cursor()
		cur.execute(f"UPDATE produit set {nom} = '{nouveauNom}' WHERE id = {condition};")
		self.datab.commit()
		cur.close()

	def Delete(self, condition):
		cur = self.datab.cursor()
		cur.execute(f"DELETE FROM produit WHERE id = {condition};")
		self.datab.commit()
		cur.close()


#test des méthodes
ar15 = CRUDproduit()

#ar15.Create('AR-15', 'Replique longue', 350, 15, 2)

#ar15.Update('description',  1, 'Replique longue type AR-15' )

#ar15.Read()

#ar15.Delete(1)