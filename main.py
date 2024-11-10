#imports to be here
import turtle
import Movements
from Points import Points

#initilizing values here
snakeWindow = turtle.Screen()
snakeWindow.setup(Movements.WIDTH,Movements.HEIGHT)
snakeHead = turtle.Turtle()
snakeHead.speed('normal')
snakeHead.penup()

snakeHead.shape("square")
snakeHead.color("white")
snakeWindow.bgcolor("black")
Movements.initiateListener(snakeWindow,snakeHead)
point = Points()


textTurtle = turtle.Turtle()
textTurtle.penup()
textTurtle.hideturtle()  # Hide the turtle cursor
textTurtle.color("white")
textTurtle.goto(Movements.WIDTH // 2 - 50, Movements.HEIGHT // 2 - 20)  # Position at top right

snakeHead.shape("square")
snakeHead.color("white")
snakeWindow.bgcolor("black")
score = 0
# Update the text
def update_text(score):
    textTurtle.clear()  # Clear previous text
    textTurtle.write(f"Score: {score}", align="right", font=("Arial", 16, "normal"))

while Movements.ruleCheckForWindow(snakeHead):
    turtle.speed('fastest')
    Movements.move(snakeHead)
    HeadPosition = snakeHead.pos()
    pointPos = point.GetPos()
    if snakeHead.distance(point.GetPos()) < 15:  # Adjust this threshold based on size
        score+=1
        Movements.add_tail(snakeHead)
        point.reset_point()
        update_text(score)

    Movements.move_tails(snakeHead)  # Move the tails after moving the head

snakeWindow.exitonclick()