import turtle

import Movements
import random


class Points:
    def __init__(self):
        self.point_turtle = turtle.Turtle()  # Create a turtle for the point
        self.point_turtle.shape("circle")
        self.point_turtle.color("red")
        self.point_turtle.penup()  # Prevent drawing a line
        self.pos = None
        self.point_turtle.hideturtle()  # Hide initially

        self.GeneratePoint()  # Generate a point immediately upon creation

    def GeneratePoint(self):
        # Generate a random position within the window bounds
        self.pos = (random.randint(-Movements.WIDTH//2 + 10, Movements.WIDTH//2 - 10),
                    random.randint(-Movements.HEIGHT//2 + 10, Movements.HEIGHT//2 - 10))
        self.point_turtle.goto(self.pos)  # Move the point turtle to the new position
        self.point_turtle.showturtle()  # Show the point when it is placed


    def GetPos(self):
        return self.pos

    def reset_point(self):
        self.point_turtle.hideturtle()  # Hide the point before repositioning
        self.GeneratePoint()  # Method to regenerate the point when eaten
