import turtle

def zamalujokno():
    turtle.fillcolor('black')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()

ilekolumn = input("Podaj ilość kolumn: ")
ilewierszy = input("Podaj ilośc wierszy: ")

turtle = turtle.Turtle()
turtle.speed(60)
turtle.pensize(1)
#turtle.screen.screensize(1500, 1500)

bialyczarny = 0
przemiennawiersza = 0

for x in range(int(ilewierszy)):
    if przemiennawiersza == 0:
        bialyczarny = 1
    else:
        bialyczarny = 0
    for y in range(int(ilekolumn)):
        turtle.penup()
        turtle.goto(y*50, x*50)
        turtle.pendown()
        if bialyczarny == 0:
            zamalujokno()
            bialyczarny = 1
        else:
            for _ in range(4):
                turtle.forward(50)
                turtle.right(90)
            bialyczarny = 0

    if przemiennawiersza == 0:
        przemiennawiersza = 1
    else:
        przemiennawiersza = 0

input("Wciśnij dowolny klawisz aby wyjść.")

# 1. Proszę pamiętać że programujemy po angielsku :)
# 2. Fajnie że nazwy zmiennych są czytelne. Proszę tylko zastosować język angielski i pewną konwencję, np.
# camelCase: czyliNazwaJestPisanaWTenSposób
# zmienne_oddzielone_dolnymi_spacjami
# sNameOfUser
# iNumberOfColumn
# to już jest idealne nazwenictwo: Po angielsku, czytelne, oraz pokazuje jakiego typu jest zmienna.