from tkinter import *
# tk = Tk()
# tk.title("Button")
def onClick() :
    print ("hello, there!") 

btn = Button(Tk(), text = "Click Here", command = onClick() )
btn.pack()