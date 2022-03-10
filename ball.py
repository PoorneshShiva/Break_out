from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.speed(0.1)
        self.shapesize(2)
        self.pu()
        self.setposition(0, -360)

    def bounce(self):
        self.y_move *= -1
        self.x_move *= -1

        # self.setposition(self.xcor() * -1, self.ycor() * -1)

    def bounce_x(self):
        self.y_move *= -1
        self.x_move *= +1

    #
    def bounce_y(self):
        self.y_move *= +1
        self.x_move *= -1

    #     self.move_speed *= 0.9

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setposition(new_x, new_y)
