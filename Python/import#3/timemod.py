import time

for i in dir(time):
	if "_" not in i:
		print(i)



# Uyutma / bekletme
print("1.satır.................")
time.sleep(2)
print("2.satır.................")

# zaman aralığı
zaman1 = time.time()
time.sleep(2)
zaman2 = time.time()
print("fark: {}".format(zaman2-zaman1))