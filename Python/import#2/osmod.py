import os


# Bulunduğum dizin
loc = os.getcwd()
print(loc)

# Dizin değiştir
os.chdir("/home/soloturq/Masaüstü")
loc = os.getcwd()
print(loc)


######################

# Temizleme
# os.system("clear")

######################


# Ev dizini
ev = os.path.expanduser("~")
print(ev)

# Dosya ve klasörler
print("#####################")
for i in os.listdir("."):
	print(i)