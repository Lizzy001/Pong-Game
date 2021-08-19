from turtle import Screen, Turtle
from paddle import Paddle
from bal import Bal
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
bal = Bal()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "Left")
screen.onkey(l_paddle.go_down, "Right")

game_is_on = True
while game_is_on:
    time.sleep(bal.move_speed)
    screen.update()
    bal.move()

    # Detect collision with wall
    if bal.ycor() > 280 or bal.ycor() < -280:
        bal.bounce_y()

    # Detect collision with r_paddle
    if bal.distance(r_paddle) < 50 and bal.xcor() > 320 or bal.distance(l_paddle) < 50 and bal.xcor() < -320:
        bal.bounce_x()

    # Detect R paddle misses
    if bal.xcor() > 380:
        bal.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if bal.xcor() < -380:
        bal.reset_position()
        scoreboard.r_point()

screen.exitonclick()
