import sqlite3

veriler = [
("Ahmet Ümit","İstanbul hatırası"),
("Yaşar Kemal","İnce Memed"),
("Paulo Coelho","Simyacı"),
("Paulo Coelho","Aldatma")]



db = sqlite3.connect("kitaplar.sqlite")



# İmleç oluşturma
imlec = db.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS kitaplik (yazar,kitap)")



# parametre sorgusu
for veri in veriler:

	# veri oluşturma
	imlec.execute("INSERT INTO kitaplik VALUES (?,?)",veri)
	db.commit()

# seçilen verileri almak
imlec.execute("SELECT * FROM 'kitaplik'")
#fetchall(),fetchone(),fetchmany(*)
ceri = imlec.fetchmany(5)

for i in ceri:
	print(i)




db.close()