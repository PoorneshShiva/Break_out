from turtle import Turtle
import random
class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.dist_list = []
        self.COLOR = ["green", "orange", "yellow", "blue", "red", "violet"]
        self.posx = -860
        self.posy = 500
        self.create_block()

    def create_block(self):
        self.shape('square')
        self.shapesize(2, 8, 4)
        self.penup()
        self.speed('fastest')
        self.setposition(self.posx, self.posy)
        self.color(random.choice(self.COLOR))

        for _ in range(6):
            self.setposition(self.posx, self.posy)
            self.clone()
            for each in range(10):
                self.forward(170)
                self.clone()

        # posx -= 100
            self.posy -= 50

    def block_list(self, tur, ball):
        for index, each in enumerate(tur):
            self.dist_list.append(ball.distance(each))

    def block_col(self, tur, ball):
        for index, each in enumerate(tur):
            if ball.distance(each) <= min(self.dist_list):

                return each.reset()
            else:
                return None