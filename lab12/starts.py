import turtle
import math

wn = turtle.Screen()
tri = turtle.Turtle()
tri.hideturtle()
tri.speed(0)
tri.penup()

col1 = "#ff0000"
col2 = "#EFF906"

def triangleL(tri, col, scale):
    tri.fillcolor(col)
    tri.begin_fill()
    tri.pendown()
    tri.left(90)
    tri.forward(200 * scale)
    tri.right(162)
    tri.forward(145 * scale)
    tri.right(54)
    tri.forward(76 * scale)
    tri.end_fill()
    tri.penup()

def triangleR(tri, col, scale):
    tri.fillcolor(col)
    tri.begin_fill()
    tri.pendown()
    tri.left(90)
    tri.forward(200 * scale)
    tri.right(198)
    tri.forward(145 * scale)
    tri.right(306)
    tri.forward(76 * scale)
    tri.end_fill()
    tri.penup()

def star(x, y, scale, tilt=0):

    tri.goto(x, y)

    for i in range(5):
        tri.setheading(72 * i + tilt)
        triangleL(tri, col1, scale)

    for i in range(5):
        tri.setheading(72 * i + tilt)
        triangleR(tri, col2, scale)

scales   = [0.3, 0.2, 0.15, 0.05]
radius_x = 250
radius_y = 110
steps    = math.pi / 9
max_tilt = 40

θ = 0
for _ in range(10):
    x = math.cos(θ) * radius_x
    y = math.sin(θ) * radius_y
    tilt = (x / radius_x) * max_tilt
    star(x, y, scales[-1], tilt)
    θ += steps

fixed_positions = [
    (-190, -25, scales[2]), 
    (-105, -15, scales[1]),  
    (   0,    0, scales[0]),  
    ( 105, -15, scales[1]), 
    ( 190, -25, scales[2]), 
]

for x, y, scale in fixed_positions:
    star(x, y, scale)

wn.mainloop()