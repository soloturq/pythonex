import random
from random import * #randint
from os import system as komut

komut("clear")


# Rastgele Sayı

rast = randint(10,50)
print("Tutulan sayı", rast)
print("10 ile 50 arasında bir sayı tuttum bil bakalım kaç?")

tahmin = int(input("TAHMİN: "))

if tahmin == rast:
	print("Tebrikler")

else:
	print("Maalesef")