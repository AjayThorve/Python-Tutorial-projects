import turtle
def draw_square(pen):
    pen.shape("turtle")
    pen.color("red")
    pen.speed(100)
    for i in range(0,4):
        pen.forward(100)
        pen.right(90)

def draw_circle(pen):
    #angie=turtle.Turtle()
    pen.color("red")
    pen.speed(200)
    pen.circle(100)

def draw_triangle(an):
    for i in range(0,3):
        an.forward(50)
        an.left(120)
def draw_squared_circle():
    mark=turtle.Turtle()
    n=0
    while(n<=360):
        draw_square(mark)
        mark.right(5)
        n=n+5

def draw_flower():
    mark=turtle.Turtle()
    n=0
    while(n<=360):
        draw_circle(mark)
        mark.right(5)
        n=n+5
    mark.right(85)
    mark.forward(400)

def draw_name():
    ajay=turtle.Turtle()
    ajay.color("green")
    draw_triangle(ajay)
    ajay.right(120)
    ajay.forward(100)
    ajay.backward(100)
    ajay.left(120)
    ajay.forward(100)
    ajay.right(60)
    ajay.forward(100)

def recursive_triangle(n,r):
    draw_triangle(r)
    if(n<=10):
        n=n+1
        r.right(120)
        recursive_triangle(n,r)
        r.left(120)
        

window = turtle.Screen()
window.bgcolor("blue")
#draw_squared_circle()
#draw_flower()
#draw_name()
#draw_circle()
#draw_triangle()
r=turtle.Turtle()
recursive_triangle(1,r)
window.exitonclick()
