import mysql.connector

class CRUDcategorie:
	def __init__(self):
		self.datab = mysql.connector.connect(
			host="localhost",
			user="root",
			password="root",
			database="boutique"
		)

	def Create(self,nom):
		cur= self.datab.cursor()
		cur.execute(f"INSERT INTO categorie (nom) values ('{nom}');")
		self.datab.commit()
		cur.close()

	def Read(self):
		cur = self.datab.cursor()
		cur.execute(f"SELECT * FROM categorie;")
		res = cur.fetchall()
		for line in res:
			print(line)
		cur.close()

	def Update(self, nom, condition, nouveauNom):
		cur = self.datab.cursor()
		cur.execute(f"UPDATE categorie set {nom} = '{nouveauNom}' WHERE id = {condition};")
		self.datab.commit()
		cur.close()

	def Delete(self, condition):
		cur = self.datab.cursor()
		cur.execute(f"DELETE FROM categorie WHERE id = {condition};")
		self.datab.commit()
		cur.close()