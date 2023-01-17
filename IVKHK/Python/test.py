import turtle

def draw_cat():
    # create a turtle object
    t = turtle.Turtle()

    # draw the cat's head
    t.circle(50)

    # move the turtle to draw the cat's ears
    t.penup()
    t.goto(-35, 55)
    t.pendown()
    t.circle(10)

    t.penup()
    t.goto(35, 55)
    t.pendown()
    t.circle(10)

    # move the turtle to draw the cat's eyes
    t.penup()
    t.goto(-25, 70)
    t.pendown()
    t.circle(5)

    t.penup()
    t.goto(25, 70)
    t.pendown()
    t.circle(5)

    # move the turtle to draw the cat's nose
    t.penup()
    t.goto(0, 60)
    t.pendown()
    t.dot(10)

    # move the turtle to draw the cat's mouth
    t.penup()
    t.goto(-10, 40)
    t.pendown()
    t.goto(10, 40)

    turtle.done()

draw_cat()
