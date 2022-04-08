from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.listen()


# TODO 1: Create functions for the directions for the turtle
def move_up():
    timmy.seth(90)
    timmy.fd(1)


def move_down():
    timmy.seth(270)
    timmy.fd(1)


def move_left():
    timmy.seth(180)
    timmy.fd(1)


def move_right():
    timmy.seth(0)
    timmy.fd(1)


def clear_screen():
    timmy.clear()


# TODO 2: Bind the functions to keys: W, A, S, D
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(clear_screen, "space")

screen.exitonclick()
