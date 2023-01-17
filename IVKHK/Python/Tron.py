"""Tron, classic arcade game.

Exercises

1. Make the tron players faster/slower.
2. + Stop a tron player from running into itself. 
3. + Allow the tron player to go around the edge of the screen.
4. How would you create a computer player?
"""

from turtle import *

from freegames import square, vector

p1xy = vector(-150, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(150, 0)
p2aim = vector(-4, 0)
p2body = set()


def inside(head):
    # """Return True if head inside screen."""
    
    if head.x > 200:
        head.x = -200
    elif head.x < -200:
        head.x = 200
    elif head.y > 200:
        head.y = -200
    elif head.y < -200:
        head.y = 200

    return True
    # return -200 < head.x < 200 and -200 < head.y < 200
    
    

def draw():
    """Advance players and draw game."""
    p1xy.move(p1aim)
    inside(p1xy)
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    inside(p2xy)
    p2head = p2xy.copy()


    if not inside(p1head) or p1head in p2body :
        print('Player blue wins!')
        return

    if not inside(p2head) or p2head in p1body :
        print('Player red wins!')
        return

    if p1head in p1body:
        print('Player blue wins!')
        return

    p1body.add(p1head)

    if p2head in p2body:
        print('Player red wins!')
        return

    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, 'red')
    square(p2xy.x, p2xy.y, 3, 'blue')
    update()
    ontimer(draw, 80)



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: p1aim.rotate(90), 'a')
onkey(lambda: p1aim.rotate(-90), 'd')
onkey(lambda: p2aim.rotate(90), 'j')
onkey(lambda: p2aim.rotate(-90), 'l')

penup()
goto(-200,-200)
pendown()
for i in range(4):
    forward(400)
    left(90)

draw()
done()