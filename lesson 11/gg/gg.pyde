img = 0
def setup():
    global img
    size(600,600)
    img = loadImage('quen.jpg')
def draw():
    global img
    image(img,0,0,150,150)
