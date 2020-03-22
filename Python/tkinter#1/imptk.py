import tkinter
from tkinter import *



pencere = tkinter.Tk()


pencere.title("Deneme Programı")

ai = "solo"
ap = "1234"

def girisyapma():
	p = pg.get()
	i = ig.get()
	if (p == ap and i == ai):
		gd.config(text = "Doğru")
	else:
		gd.config(text = "Yanlış")

i = Label(pencere, text = "Adınız")
i.grid(row=0,column=0)
ig = Entry(pencere,width="8")
ig.grid(row=0,column=1)
p = Label(pencere,text="Şifreniz")
pg = Entry(pencere,width="8",show="*")
p.grid(row=1,column=0)
pg.grid(row=1,column=1)

g = Button(pencere,text="Giriş",command=girisyapma)
g.grid(row=3,column=0)

gd = Label(pencere,text="")
gd.grid(row=3,column=1)




pencere.mainloop()