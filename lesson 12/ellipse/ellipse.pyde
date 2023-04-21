a = 0
b = 0
def setup():
    size(600,600)
def draw():
    global a,b
    background(255)
    ellipse(a,b,50,50)
    a += 1
    b += 1
    if a == 600:
        a = 0
        b = 0
