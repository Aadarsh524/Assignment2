"""
    Code to draw a fractal tree using turtle graphics.
    The tree is drawn recursively, with branches splitting at specified angles.
    """

import turtle

def draw_tree(length, depth, left_angle, right_angle, reduction_factor, initial_depth):
    if depth == 0:
        return
    else:
        # Set color: red for trunk (initial depth), green for branches
        if depth == initial_depth:
            turtle.color("red")
        else:
            turtle.color("green")
        turtle.forward(length)
        turtle.left(left_angle)
        draw_tree(length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor, initial_depth)
        turtle.right(left_angle)
        turtle.right(right_angle)
        draw_tree(length * reduction_factor, depth - 1, left_angle, right_angle, reduction_factor, initial_depth)
        turtle.left(right_angle)
        turtle.backward(length)

# Get user inputs
left_angle = float(input("Enter left branch angle (degrees): "))
right_angle = float(input("Enter right branch angle (degrees): "))
start_length = float(input("Enter starting branch length (pixels): "))
depth = int(input("Enter recursion depth: "))
reduction_factor = float(input("Enter branch length reduction factor (e.g., 0.7 for 70%): "))

# Set up turtle graphics with different values
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.setheading(90)

# Draw the tree
draw_tree(start_length, depth, left_angle, right_angle, reduction_factor, depth)

# Keep the window open
turtle.done()