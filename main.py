from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.listen()

# TODO 1: Create functions for the directions for the turtle
def go_up():
    timmy.fd(10)

def go_down():
    timmy.bk(10)

def go_left():
    new_heading = timmy.heading() + 10
    timmy.seth(new_heading)

def go_right():
    new_heading = timmy.heading() - 10
    timmy.seth(new_heading)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

# TODO 2: Bind the functions to keys: W, A, S, D

screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")
screen.onkeypress(clear_screen, "space")

screen.exitonclick()

