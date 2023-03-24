r = 350
t = 350
g = 1
l = 1
def setup():
    size(600,600)
def draw():
    background(255)
    global r,g,t,l
    fill(255,0,0)
    rect(100,200,r,r)
    rect(400,200,t,t)
    fill(0,255,0)
    rect(200,400,g,g)
    rect(400,400,l,l)
    r -= 1
    g += 2
    t -= 3
    l += 4
    
