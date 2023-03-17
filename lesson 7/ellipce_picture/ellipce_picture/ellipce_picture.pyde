def setup():
    size(600,600)
    background(255)
x=0
csgo=0
cat=0
def draw():
    background(255)
    global x,csgo
    fill(random(0,255),random(0,255),random(0,255))
    csgo=random(10,60)
    ellipse(x,x,csgo,csgo)
    x = x+1
