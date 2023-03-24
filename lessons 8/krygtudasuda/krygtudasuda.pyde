x = 600
y = 0
r = 5
def setup():
    size(600,600)
    strokeWeight(5)
def draw():
    background(255)
    strokeWeight(r)
    global x,y,r
    point(x,y)
    x -= 1
    y += 1
    r += 3
