t = 0
y = 350
u = 200
i = 400
o = 250
p = 450
def setup():
    size(600,400)
    colorMode(HSB)
def draw():
    global t,y,u,i,o,p
    background(255)
    fill(0,0,t)
    triangle(350,u,400,o,450,u)
    t += 1
    y += 1
    u += 1
    i += 1
    o += 1
    p += 1
