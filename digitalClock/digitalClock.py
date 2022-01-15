from tkinter import *
import time
root = Tk()
root.title("Digital Clock")
def clock() : 
    tick = time.strftime("%H : %M : %S %p")
    label.config(text = tick) 
    label.after(1000,clock)
label1 = Label(root,text = "Digital Clock",font = ("MADE Evolve Sans EVO",20),bg = "black",fg = "red")
label = Label(root,font = ("DS-Digital",30),background = "black",foreground = "lime")
# label1.pack()
# label.pack()
label1.place(x = 15,y = 30)
label.place(x = 15,y = 100)
clock()
root.geometry("400x250+300+400")
root.configure(bg = "black")
root.mainloop()
