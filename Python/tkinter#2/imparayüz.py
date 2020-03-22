import tkinter
from tkinter import *


pencere = tkinter.Tk()


pencere.title("Pencere")


pencere.geometry("350x350+0+0")


#pencere.resizable(FALSE,FALSE)
pencere.minsize(200,200)
pencere.maxsize(500,500)
pencere.state("normal")
#normal,iconic,withdrawn


pencere.wm_attributes("-alpha",0.1)
#alpha,topmost,zoomed,fullscreen,type


yazi = Label(text="merhaba dünya", 
	fg = "#766575", 
	font = ("Open Sans", "15", "bold", "italic"),
	width = 15,
	height = 5,
	padx = 15,
	pady = 30,
	#wraplength = 100,
	justify = "left",
	anchor = "center")
yazi.pack()
#bg,fg
#bold,italic,normal,underline,overstrike
#padx,pady,width,height,wraplength,justify
#anchor = "n" (yukarı)
#anchor = "s" (aşağı)
#anchor = "e" (sağ)
#anchor = "w" (sol)
#anchor = "center" (orta)


pencere.mainloop()