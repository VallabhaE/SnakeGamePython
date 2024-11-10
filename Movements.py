import turtle

Speed_level = 1
WIDTH = 900
HEIGHT = 500
Tails = []


def move(snakeHead):
    snakeHead.forward(Speed_level * 10)


def  initiateListener(snakeWindow, snakeHead):
    # Initial direction
    current_direction = 90  # Starting moving up

    # Define functions to handle key presses
    def move_up():
        nonlocal current_direction
        if current_direction != 270:  # Prevent turning down if moving up
            snakeHead.setheading(90)
            current_direction = 90

    def move_down():
        nonlocal current_direction
        if current_direction != 90:  # Prevent turning up if moving down
            snakeHead.setheading(270)
            current_direction = 270
            print("Moving down!")

    def move_left():
        nonlocal current_direction
        if current_direction != 0:  # Prevent turning right if moving left
            snakeHead.setheading(180)
            current_direction = 180

    def move_right():
        nonlocal current_direction
        if current_direction != 180:  # Prevent turning left if moving right
            snakeHead.setheading(0)
            current_direction = 0

    # Start listening for key events
    snakeWindow.listen()
    snakeWindow.onkey(move_up, "Up")      # Arrow Up key
    snakeWindow.onkey(move_down, "Down")  # Arrow Down key
    snakeWindow.onkey(move_left, "Left")  # Arrow Left key
    snakeWindow.onkey(move_right, "Right")  # Arrow Right key

def ruleCheckForWindow(snakeHead):
    position = snakeHead.pos()
    if position[0] >= WIDTH/2 or position[0]<= -WIDTH/2:
        return False
    if position[1] >= HEIGHT/2 or position[1]<= -HEIGHT/2:
        return False
    return True


def add_tail(head):
    # Create a new tail segment
    new_tail = turtle.Turtle()
    new_tail.hideturtle()
    new_tail.shape("square")
    new_tail.color("white")
    new_tail.penup()  # Don't draw a line
    Tails.append(new_tail)  # Add to the tail list
    new_tail.goto(head.pos())
    new_tail.showturtle()

def move_tails(snakeHead):
    # Move the last segment to the position of the second last, and so on
    for i in range(len(Tails) - 1, 0, -1):
        Tails[i].goto(Tails[i - 1].pos())
    if Tails:
        Tails[0].goto(snakeHead.pos())  # Move the first tail segment to the head position

