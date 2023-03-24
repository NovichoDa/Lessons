e = 1
def setup():
    size(600,600)
def draw():
    background(255)
    global e
    strokeWeight(e)
    line(150,150,300,300)
    line(150,150,300,150)
    line(150,300,300,150)
    line(220,50,150,300)
    line(220,50,300,300)
    e += 1
