import turtle
import time

wn = turtle.Screen()
wn.title("Animation")
wn.bgcolor("white")

player = turtle.Turtle()
player.shape("circle")
player.shape("square")
player.shape("triangle")

def playerAnimation() :
    player.shape("square")
    time.sleep(0.5)
    player.shape("circle")
    time.sleep(0.5)
    player.shape("triangle")
    time.sleep(0.5)


while True:
    print("Main Loop")
    playerAnimation()

wn.mainloop()    
