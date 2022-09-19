from turtle import Turtle, Screen

tim = Turtle()

base_interior_angle = 180

for i in range(1,11):
    for j in range(i):
        tim.right(base_interior_angle * i - base_interior_angle)
        tim.forward(100)

# tim.right(180-60)
# tim.forward(100)
# tim.right(180-60)
# tim.forward(100)
# tim.right(180-60)
# tim.forward(100)





screen = Screen()
screen.exitonclick()