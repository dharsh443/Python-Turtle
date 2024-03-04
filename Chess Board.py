import turtle  
scr = turtle.Screen()  
ttl = turtle.Turtle()   
def draw():  
    for i in range(4):  
        ttl.forward(35)  
        ttl.left(90)  
  
    ttl.forward(35)  
if __name__ == "__main__":   
    scr.setup(500, 700)   
    ttl.speed(90)    
    for j in range(8):    
        ttl.up()    
        ttl.setpos(-110, 35 * j)    
        ttl.down()    
        for k in range(8):    
            if (j + k) % 2 == 0:  
                clr = 'black'  
  
            else:  
                clr = 'white'  
    
            ttl.fillcolor(clr)  
  
             
            ttl.begin_fill()  
  
           
            draw()  
           
            ttl.end_fill()   
    ttl.hideturtle()  
    turtle.done()  
