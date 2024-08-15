import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Heart Animation")
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.speed(1)

# Define the heart shape
def draw_heart():
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

# Animation: Draw the heart and make it pulse
def animate_heart():
    for _ in range(1):  # Pulse 1 times
        t.clear()
        t.penup()
        t.goto(0, -100)
        t.pendown()
        draw_heart()
        t.penup()
        t.goto(0, 0)
        t.color("black")
        t.write("I Love You", align="center", font=("Arial", 11, "normal"))
        t.color("red")
        time.sleep(0.4)
        t.clear()
        time.sleep(0.7)

# Start the animation
animate_heart()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()