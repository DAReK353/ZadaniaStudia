import turtle


def snowflake(section, depth):
    if depth > 0:
        for angle in [60, -120, 60, 0]:
            snowflake(section, depth-1)
            turtle.left(angle)
    else:
        turtle.forward(section)


length = input("Enter the length of the segment: ")
order = input("Enter the level of the iterations: ")

turtle = turtle.Turtle()
turtle.speed(10)

for i in range(3):
    snowflake(int(length), int(order))
    turtle.right(120)

input("Press any key to exit.")
