img = 0
def setup():
    size(1000,800)
def draw():
    global img
    img = loadImage("background.jpg")
    image(img,0,0,1000,800)
    ellipse(500,400,50,50)
