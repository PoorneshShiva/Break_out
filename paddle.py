from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.penup()
        self.speed("fastest")
        self.shape('square')
        self.shapesize(1.5, 14)
        self.color("white")
        self.setposition(0, -433)

    def move_right(self):
        # self.bottom_paddle.setheading(180)
        self.speed("fastest")
        self.forward(100)

    def move_left(self):
        # self.bottom_paddle.setheading(180)
        self.speed("fastest")
        self.backward(100)

 