import turtle

# opens a window to draw on
window = turtle.Screen()
# makes the window white
window.bgcolor("white")


def draw_square(new_turtle):
    for x in range(0, 4):
        new_turtle.pendown()
        new_turtle.right(90)
        new_turtle.forward(100)


def draw_star(turtle_star):
    for x in range(0,7):
        turtle_star.pendown()
        turtle_star.right(144)
        turtle_star.forward(100)

def main():
    # create an instance of Turtle
    jane = turtle.Turtle()

    # set values on attributes in the Turtle module
    jane.shape("turtle")
    jane.color("green", "yellow")  # outline color, fill color
    jane.penup()
    jane.setx(150)

    # create another instance of Turtle and set its values
    ginger = turtle.Turtle()
    ginger.shape("circle")
    ginger.color("blue", "red")
    ginger.penup()
    ginger.setx(-150)

    # draw one square filled with color with the jane instance
    #jane.begin_fill()
    draw_square(jane)
    #jane.end_fill()
    color_count = 1
    for x in range(0, 36):
        if color_count == 1:
            ginger.color("red", "purple")
        else:
            ginger.color("blue", "yellow")
    # draw offset squares in a loop with the ginger instance
        ginger.begin_fill()
        draw_square(ginger)
        ginger.right(10)
        ginger.end_fill
        
        if color_count == 1:
            color_count -= 1
        else:
            color_count += 1


    spud = turtle.Turtle()

    spud.shape("arrow")
    spud.color("black")
    spud.penup()
    spud.setx(200)

   
    for x in range(0,7):
        draw_star(spud)
        spud.left(10)


    window.exitonclick()

# The following code will only call the `main` function if we are running *this*
# file from the command line. The main function won't be called if we import
# this file.
# Want to learn more about if __name__ == '__main__':?
# Check out:
# http://stackoverflow.com/a/20158605 and/or
# https://www.youtube.com/watch?v=sugvnHA7ElY
if __name__ == '__main__':
    main()
