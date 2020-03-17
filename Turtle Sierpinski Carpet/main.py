import turtle


def draw_square(section, depth):
    if depth == 0:
        turtle.color('black')
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(section)
            turtle.left(90)
        turtle.end_fill()
    else:
        for _ in range(4):
            draw_square(section/3, depth-1)
            turtle.forward(section/3)
            draw_square(section/3, depth-1)
            turtle.forward(section/3)
            turtle.forward(section/3)
            turtle.left(90)


length = input("Enter the length of the segment: ")
order = input("Enter the level of the iterations: ")

turtle = turtle.Turtle()

turtle.speed(10)

draw_square(int(length), int(order))

input("Press any key to exit.")
