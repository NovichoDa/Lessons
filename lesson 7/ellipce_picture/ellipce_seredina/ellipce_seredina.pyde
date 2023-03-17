def setup():
    size(600,600)
    background(255)
x=300
y=300
csgo=0
cat=0
def draw():
    background(255)
    global x,csgo,y
    fill(random(0,255),random(0,255),random(0,255))
    csgo=random(10,60)
    ellipse(x,x,csgo,csgo)
    ellipse(y,y,csgo,csgo)
    ellipse(y,x,csgo,csgo)
    ellipse(x,y,csgo,csgo)
    x = x+1
    y = y-1
