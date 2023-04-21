a = 0
b = 0
c = 0
def setup():
    size(600,600)
def draw():
    global a,b,c
    background(255)
    fill(a,b,c)
    ellipse(300,300,50,50)
    a += 1
    b += 1
    c += 1
    if a == 300:
        a = 0
        b = 0
        c = 0
