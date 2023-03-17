def setup():
    size(600,600)
    background(255)
    strokeWeight(25)
x=300
y=300
z=0
def draw():
    global x,y,z
    stroke(random(0,255),random(0,255),random(0,255))
    translate(300,300)
    rotate(radians(z))
    line(0,0,100,100)
    z = z + 2
