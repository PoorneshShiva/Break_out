import time

from paddle import Paddle
from turtle import Screen
from ball import Ball
from block import Block

dist_list = []

screen = Screen()
paddle = Paddle()
ball = Ball()
block = Block()
all_tur = screen.turtles()[:1:-1]
print(len(all_tur))


def check_blck_col():
    for each in all_tur:
        dist_list.append(ball.distance(each))
        # print(ball.distance(each))
        if ball.distance(each) <= 62:
            # print(each)
            each.reset()

            return True
        else:
            pass


screen.setup(width=1.0, height=1.0)
screen.colormode(255)
screen.bgcolor("black")

screen.listen()
screen.onkeypress(key="Left", fun=paddle.move_left)
screen.onkeypress(key="Right", fun=paddle.move_right)

screen_width = screen.window_width() / 2 - 22
screen_height = screen.window_height()

print(type(all_tur))
print(screen_width)
print(screen_height)
ball.pendown()
ball.goto(-938, -365)
# ball.setposition(0, 1061/2 - 30)
screen.delay(5)
print(len(screen.turtles()[3:]))
count = 0
check_blck_col()

while True:
    ball.move()

    screen.update()
    if check_blck_col():
        ball.bounce_x()
        screen.update()

    if ball.xcor() <= -937:
        check_blck_col()
        ball.bounce()
        print("first_condtion")
    if ball.xcor() >= 929:
        check_blck_col()
        ball.bounce_y()
    if ball.ycor() >= 500:
        print("second_condtion")
        check_blck_col()
        ball.bounce_x()
        count += 1
        if count == 2:
            print("Done")
            break
    if ball.distance(paddle) <= 50:
        ball.bounce_x()
    else:
        pass
    print(ball.heading())
        # print(ball.position())
        # print('no!!!!')

screen.exitonclick()
