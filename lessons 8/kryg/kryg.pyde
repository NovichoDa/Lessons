g = 1200
def setup():
    size(600,600)
def draw():
    global g
    fill(random(15,255),random(15,255),random(15,255),)
    stroke(random(15,255),random(15,255),random(15,255),)
    ellipse(300,300,g,g)
    g -= 5
    
