t = 255
y = 0
u = 0
i = 0
o = 0
p = 0
def setup():
    size(600,400)
    colorMode(HSB, 360, 100, 100)
    fill(50,46,95)
    ellipse(300,200,120,120)
def draw():
    global t,y,u,i,o,p
    fill(0,0,t)
    ellipse(250,200,60,60)
    fill(0,0,y)
    ellipse(350,200,60,60)
    t -= 1
    y += 1
