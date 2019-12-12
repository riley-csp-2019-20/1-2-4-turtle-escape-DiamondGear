# 1.2.4 Turtle Escape Version 2.0
import turtle as trtl
import random as rdn
def reset_button():
    drawmaze = trtl.Turtle()
    Escaper = trtl.Turtle()
    wn = trtl.Screen()
    
    # Reset the Maze
    Escaper.ht()
    Escaper.penup()
    Escaper.speed(0)
    Escaper.goto(10000,10000)
    drawmaze.ht()
    drawmaze.speed(0)
    drawmaze.pensize(1000)
    drawmaze.pencolor("white")
    drawmaze.forward(200)
    drawmaze.back(400)
    drawmaze.penup()
     # Make the Maze
    drawmaze.pencolor("green")
    drawmaze.pensize(5)
    drawmaze.left(90)
    drawmaze.goto(0,0)
    #   Define variables
    repeat_amount = 35
    move_dist = 25
    gap_size = 25


    #   Make the Maze Spiral and Gaps
    for i in range(repeat_amount):

        if i > 4:
            door = rdn.randint(gap_size, (move_dist - gap_size))
            drawmaze.forward(door)
            drawmaze.penup()
            drawmaze.forward(gap_size)
            drawmaze.pendown()
            drawmaze.left(90)
            # Make the Walls and Gaps
            drawmaze.forward(gap_size)
            drawmaze.back(gap_size)
            drawmaze.right(90)
            drawmaze.forward(move_dist - gap_size - door)
            drawmaze.left(90)
        move_dist +=15    
    drawmaze.ht() 



    def move_forward():
        Escaper.forward(15)

    def move_back():
        Escaper.back(15)

    def turn_left():
        Escaper.left(90)


    def turn_right():
        Escaper.right(90)

    #   Make the Player Turtle
    Escaper.st()
    Escaper.shape("turtle")
    Escaper.penup()
    Escaper.goto(-55,40)
    Escaper.speed(5)
    Escaper.pendown()
    Escaper.pencolor("blue")
    Escaper.pensize(5)


    wn.onkeypress(move_forward,"w")
    wn.onkeypress(move_back,"s")
    wn.onkeypress(turn_left,"a")
    wn.onkeypress(turn_right,"d")
    
wn = trtl.Screen()
reset_button()
wn.onkeypress(reset_button,"r")

wn.listen()
wn.mainloop()