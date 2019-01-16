import turtle

import random


 

def draw_box(t,x,y,sizeX,sizeY,fill_color):

    t.penup() 

    t.goto(x,y) 

    t.pendown() 

    t.speed(0)

 

    t.fillcolor(fill_color)

    t.begin_fill()  

 

    for i in range(0,2):

        t.forward(sizeX) 
        t.left(90) 
        t.forward(sizeY)
        t.left(90)

 

    t.end_fill() 


def draw_line(t,x,y,sizeX,sizeY):
    
    t.penup() 

    t.goto(x,y) 

    t.pendown() 

    t.speed(0)

    for i in range(0,2):
    
        t.forward(sizeX) 
        t.left(90) 
        t.forward(sizeY)
        t.left(90)

 

 

def draw_chess_board(beginX,beginY,sizeX,sizeY):

    square_color = "green" 

    start_x = beginX 

    start_y = beginY 

    box_width = sizeX 
    box_height = sizeY

    for i in range(0,8): 

        for j in range(0,1):

            box_start_pointX = start_x+j*box_width
            box_start_pointY = start_y+i*box_height
            

            draw_box(board, box_start_pointX, box_start_pointY, box_width, box_height, square_color)

def hlines(beginX,beginY,sizeX,sizeY):
    
   
    
    start_x = beginX 

    start_y = beginY 

    box_width = sizeX 
    box_height = sizeY

    for i in range(0,1): 

        for j in range(0,8):

            box_start_pointX = start_x+j*box_width
            box_start_pointY = start_y+i*box_height
            

            draw_line(board, box_start_pointX, box_start_pointY, box_width, box_height)

def circlepartsplayer(x,y):

    turtle.penup()

    turtle.goto(x,y)

    turtle.pendown()

    turtle.fillcolor("white")

    turtle.speed(0)

    turtle.begin_fill()  

    turtle.circle(10)

    turtle.end_fill()


def circlepartscomputer(x,y):

    turtle.penup()

    turtle.goto(x,y)

    turtle.pendown()

    turtle.fillcolor("black")

    turtle.speed(0)

    turtle.begin_fill()  

    turtle.circle(10)

    turtle.end_fill()


def whoisfirst():
    
    if random.randomint(0,1) == 0:
       
        return 'computer'
   
    else:
       
        return 'player'  

def tileinputplayer(xC,xY, color):
    (x,y) = input ('Where would you like to place your tile')






         

  


board = turtle.Turtle()



draw_chess_board(0,0,240,30)

hlines(0,0,30,240)

Valuegrid = [15,5]

#Note. Each circle should go by 30.

circlepartscomputer(105,95)

circlepartsplayer(135,95)

circlepartscomputer(135,125)

circlepartsplayer(105,125)

#Start of the bottom left grid

circlepartsplayer(15,5)

#start of the top right grid

circlepartscomputer(225,215)




turtle.done()