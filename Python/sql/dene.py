import sqlite3




db = sqlite3.connect("kitaplar.sqlite")
imlec = db.cursor()



# sorgu
imlec.execute("SELECT * FROM 'kitaplik' WHERE yazar = 'Paulo Coelho'")
#fetchall(),fetchone(),fetchmany(*)
ceri = imlec.fetchall()

for i in ceri:
	print(i)




db.close()