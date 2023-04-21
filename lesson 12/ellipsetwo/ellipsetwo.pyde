a = 0
b = 0
def setup():
    size(600,600)
def draw():
    global a,b
    background(255)
    ellipse(300,300,a,b)
    a += 1
    b += 1
    if a == 300:
        a = 0
        b = 0
