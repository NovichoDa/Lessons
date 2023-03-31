t = 0
y = 0
u = 0
i = 0
o = 0
p = 0
def setup():
    size(600,400)
def draw():
    global t,y,u,i,o,p
#красный
    fill(t,0,0)
    ellipse(200,200,40,40)
#зелёный
    fill(0,y,0)
    ellipse(250,250,40,40)
#синий
    fill(0,0,u)
    ellipse(300,300,40,40)
#жёлтый
    fill(i,i,0)
    ellipse(300,200,40,40)
#голубой
    fill(0,o,o)
    ellipse(350,250,40,40)
#фиолетовый
    fill(p,0,p)
    ellipse(400,300,40,40)
    t += 0.1
    y += 1
    u += 2
    i += 0.5
    o += 3
    p += 2.1
    if frameCound > 255*60:
        noLoop
