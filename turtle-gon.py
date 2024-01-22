import turtle
sidenum = int(input("Enter the first base of the trapezoid"))
for i in range(sidenum):
    turtle.forward(100)
    turtle.right(360/sidenum)
turtle.exitonclick()
