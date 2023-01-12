"""Tron, classic arcade game.

Exercises

1. Make the tron players faster/slower.
2. Stop a tron player from running into itself.
3. Allow the tron player to go around the edge of the screen.
4. How would you create a computer player?
"""

from turtle import *

from random import randint

from freegames import square, vector

BOT = True

timer = randint(10, 60)

p1xy = vector(-80, 0)
p1aim = vector(2, 0)
p1body = set()

p2xy = vector(80, 0)
p2aim = vector(-2, 0)
p2body = set()
count = 0

def return_to_screen(head: vector):
    if head.x > 200:
        head.x = -200
    elif head.x < -200:
        head.x = 200
    elif head.y > 200:
        head.y = -200
    elif head.y < -200:
        head.y = 200


def inside(head):
    """Return True if head inside screen."""
    return -200 < head.x < 200 and -200 < head.y < 200



def draw():
    """Advance players and draw game."""
    p1xy.move(p1aim)
    if not inside(p1xy):
        return_to_screen(p1xy)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    if not inside(p2xy):
        return_to_screen(p2xy)
    p2head = p2xy.copy()

    if p1head in p1body or p1head in p2body:
        penup()
        goto(-30,0)
        pendown()
        write("Player blue wins!")
        print('Player blue wins!')
        return

    if p2head in p1body or p2head in p2body:
        penup()
        goto(-30,0)
        pendown()
        write("Player red wins!")
        print('Player red wins!')
        return

    if BOT:
        p2copy = p2head.copy()
        p2copy.move(p2aim)
        if p2copy in p2body or p2copy in p1body:
            if randint(0, 1) == 1:
                p2aim.rotate(90)
            else:
                p2aim.rotate(-90)
    if len(p2body) % randint(10, 60) == 0:
        if randint(0, 1) == 1:
            p2copy = p2head.copy()
            p2aim_copy = p2aim.copy()
            p2aim_copy.rotate(90)
            p2copy.move(p2aim_copy)
            if p2copy not in p2body and p2copy not in p1body:
                p2aim.rotate(90)
        else:
            p2copy = p2head.copy()
            p2aim_copy = p2aim.copy()
            p2aim_copy.rotate(-90)
            p2copy.move(p2aim_copy)
            if p2copy not in p2body and p2copy not in p1body:
                p2aim.rotate(-90)


    p1body.add(p1head)
    p2body.add(p2head)

    # print(p2body, p2head)
    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    ontimer(draw, 20)



tracer(0,0)
penup()
goto(-200,-200)
pendown()
for i in range(4):
    forward(400)
    left(90)

setup(420, 420, 0, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 'd')
onkey(lambda: p1aim.scale(2), 'w')
onkey(lambda: p1aim.scale(0.5), 's')
if not BOT:
    onkey(lambda: p2aim.rotate(90), 'j')
    onkey(lambda: p2aim.rotate(-90), 'l')
    onkey(lambda: p2aim.scale(2), 'i')
    onkey(lambda: p2aim.scale(0.5), 'k')

draw()
done()
