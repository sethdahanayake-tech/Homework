import turtle

# Set up the screen and turtle object
screen = turtle.Screen()
my_turtle = turtle.Turtle()

# Loop 4 times to draw the 4 sides of a square
for _ in range(4):
    my_turtle.forward(100)  # Move forward by 100 pixels
    my_turtle.left(90)      # Turn left by 90 degrees

# Keep the window open until you click on it
screen.exitonclick()

