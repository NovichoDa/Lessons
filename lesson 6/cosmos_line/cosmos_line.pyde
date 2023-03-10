def setup():
    size(600,400)
    background(0)
    stroke(255)
    ellipse(300,200,80,80)
    frameRate(2)
def draw():
    stroke(0)
    background(0)
    ellipse(300,200,80,80)
    stroke(random(0,150))
    strokeWeight(random(5,16))
    line(300,200,random(600),random(600))
    point(random(600),random(400))
