import random
import turtle


def setup_canvas():
    """Initializes the window and turtle settings."""
    window = turtle.Screen()
    window.bgcolor("black")  # Black background makes colors pop
    window.title("Python Nested Loop Art Designer")

    artist = turtle.Turtle()
    artist.speed(0)  # 0 is the fastest animation speed
    artist.width(2)
    return artist, window


def draw_loop_art():
    artist, window = setup_canvas()

    # List of vibrant colors for our art generator
    colors = [
        "cyan",
        "magenta",
        "yellow",
        "red",
        "limegreen",
        "deepskyblue",
        "white",
    ]

    # --- THE NESTED LOOP ART LOGIC ---

    # 1. Outer Loop: Controls how many times the overall design repeats/rotates
    for design_layer in range(72):

        # Pick a new color for each layer rotation
        current_color = colors[design_layer % len(colors)]
        artist.color(current_color)

        # 2. Inner Loop: Draws the actual shape (e.g., a 4-sided square)
        for side in range(4):
            artist.forward(200)  # Size of the side
            artist.left(90)  # Corner angle for a square

        # 3. Post-Inner Loop Step: Slightly tilt the artist before drawing the next shape
        # This rotation is what creates the beautiful spiral effect
        artist.left(5)

    # Keep window open until clicked
    window.exitonclick()


if __name__ == "__main__":
    draw_loop_art()

