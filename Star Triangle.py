import turtle

def draw():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(10)
    turtle.bgcolor("white")  
    pen.pensize(2)

    initial_size = 100

    for i in range(300):
        pen.color(colors[i % 6])
        pen.forward(initial_size + i)
        pen.left(150)

    pen.hideturtle()


draw()

turtle.done()
