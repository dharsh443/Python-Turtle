import turtle  
from turtle import *  

scr = turtle.Screen()  
 
ttl = turtle.Turtle()  
speed(20)  
  
  
ttl.penup()  
ttl.goto(-150, 125)  
ttl.pendown(  
  )  
  
ttl.color("orange")  
ttl.begin_fill()  
ttl.forward(400)  
ttl.right(90)  
ttl.forward(84)  
ttl.right(90)  
ttl.forward(400)  
ttl.end_fill()  
ttl.left(90)  
ttl.forward(84)  
   
ttl.color("green")  
ttl.begin_fill()  
ttl.forward(84)  
ttl.left(90)  
ttl.forward(400)  
ttl.left(90)  
ttl.forward(84)  
ttl.end_fill()  
    
ttl.penup()  
ttl.goto(35, 0)  
ttl.pendown()  
ttl.color("navy")  
ttl.begin_fill()  
ttl.circle(35)  
ttl.end_fill()  
  
# Drawing the in-circle Big White Circle  
ttl.penup()  
ttl.goto(30, 0)  
ttl.pendown()  
ttl.color("white")  
ttl.begin_fill()  
ttl.circle(30)  
ttl.end_fill()  
   
ttl.penup()  
ttl.goto(-27, -4)  
ttl.pendown()  
ttl.color("navy")  
for j in range(24):  
    ttl.begin_fill()  
    ttl.circle(2)  
    ttl.end_fill()  
    ttl.penup()  
    ttl.forward(7)  
    ttl.right(15)  
    ttl.pendown()  
    
ttl.color("navy")  
ttl.penup()  
ttl.goto(10, 0)  
ttl.pendown()  
ttl.begin_fill()  
ttl.circle(10)  
ttl.end_fill()  
 
ttl.penup()  
ttl.goto(0, 0)  
ttl.pendown()  
ttl.pensize(1)  
for j in range(24):  
    ttl.forward(30)  
    ttl.backward(30)  
    ttl.left(15)  
   
ttl.color("Brown")  
ttl.pensize(10)  
ttl.penup()  
ttl.goto(-150,125)  
ttl.right(180)  
ttl.pendown()  
ttl.forward(500)  
   
ttl.hideturtle()  
  
turtle.done() 
