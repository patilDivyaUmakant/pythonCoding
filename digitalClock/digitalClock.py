from tkinter import *
import time
root = Tk()
root.title("Digital Clock")
def clock() : 
    tick = time.strftime("%H : %M : %S %p")
    label.config(text = tick) 
    label.after(1000,clock)
# label = Label(root,text = "Digital Clock",font = ("arial",20),bg = "yellow",fg = "blue")
label = Label(root,font = ("arial",20),background = "black",foreground = "red")

label.pack()
clock()
# root.geometry("400x250 + 300 + 400")
root.mainloop()