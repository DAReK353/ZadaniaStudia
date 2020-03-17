import turtle


def black_square():
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()


number_of_columns = input("Enter the number of columns: ")
number_of_lines = input("Enter the number of lines: ")

turtle = turtle.Turtle()
turtle.speed(60)
turtle.pensize(1)

black_or_white = 0
next_line = 0

for x in range(int(number_of_lines)):
    if next_line == 0:
        black_or_white = 1
    else:
        black_or_white = 0
    for y in range(int(number_of_columns)):
        turtle.penup()
        turtle.goto(y*50, x*50)
        turtle.pendown()
        if black_or_white == 0:
            black_square()
            black_or_white = 1
        else:
            for i in range(4):
                turtle.forward(50)
                turtle.right(90)
            black_or_white = 0

    if next_line == 0:
        next_line = 1
    else:
        next_line = 0

input("Press any key to exit.")
