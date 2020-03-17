import turtle


def draw_triangle(section, depth):
    if depth == 0:
        for _ in range(0, 3):
            turtle.forward(section)
            turtle.left(120)
    else:
        draw_triangle(section/2, depth-1)
        turtle.forward(section/2)
        draw_triangle(section/2, depth-1)
        turtle.back(section/2)
        turtle.left(60)
        turtle.forward(section/2)
        turtle.right(60)
        draw_triangle(section/2, depth-1)
        turtle.left(60)
        turtle.back(section/2)
        turtle.right(60)


length = input("Enter the length of the segment: ")
order = input("Enter the level of the iterations: ")

turtle = turtle.Turtle()

turtle.speed(10)

draw_triangle(int(length), int(order))

input("Press any key to exit.")
