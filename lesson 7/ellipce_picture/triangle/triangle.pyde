def setup():
    size(600,600)
    background(255)
x=100
y=100
x2=150
y2=150
x3=200
y3=100
def draw():
    background(255)
    global x,y,x2,y2,x3,y3
    fill(255,0,0)
    triangle(x,y,x2,y2,x3,y3)
    x = x + 1
    y = y + 1
    x2 = x2 - 1
    y2 = y2 - 1
    x3 = x3 + 1
    y3 = y3 - 1
