t = 0
y = 350
u = 200
i = 400
o = 250
p = 450
def setup():
    size(600,400)
    colorMode(HSB,360,100,100)
def draw():
    global t,y,u,i,o,p
    background(255)
    fill(0,100,t)
    ellipse(300,200,t,t)
    t += 0.3
    y += 1
    u += 1
    i += 1
    o += 1
    p += 1
