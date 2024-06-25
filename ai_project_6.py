import turtle

def draw_screen():
    screen = turtle.Turtle()
    screen.color("purple")
    screen.pensize(3)
    screen.penup()
    screen.goto(-150, 100)
    screen.pendown()
    screen.begin_fill()
    for _ in range(2):
        screen.forward(300)
        screen.right(90)
        screen.forward(200)
        screen.right(90)
    screen.end_fill()

def draw_code_lines():
    code = turtle.Turtle()
    code.color("white")
    code.pensize(2)
    lines = [
        (-140, 80, 100), (-140, 60, 150), (-140, 40, 80),
        (-140, 20, 120), (-140, 0, 140), (-140, -20, 110),
        (-140, -40, 130)
    ]
    for x, y, length in lines:
        code.penup()
        code.goto(x, y)
        code.pendown()
        code.forward(length)

def draw_person():
    person = turtle.Turtle()
    person.color("red")
    person.pensize(3)

    # Body
    person.penup()
    person.goto(-70, -50)
    person.pendown()
    person.right(90)
    person.forward(50)

    # Legs
    person.right(30)
    person.forward(30)
    person.penup()
    person.goto(-70, -100)
    person.pendown()
    person.left(60)
    person.forward(30)

    # Arms
    person.penup()
    person.goto(-70, -75)
    person.pendown()
    person.left(150)
    person.forward(30)
    person.penup()
    person.goto(-70, -75)
    person.pendown()
    person.right(120)
    person.forward(30)

    # Head
    person.penup()
    person.goto(-70, -50)
    person.pendown()
    person.left(30)
    person.circle(10)

def main():
    turtle.speed(0)
    draw_screen()
    draw_code_lines()
    draw_person()
    turtle.hideturtle()
    turtle.done()

main()
