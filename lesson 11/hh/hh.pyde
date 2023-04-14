img = 0
img1 = 0
img2 = 0
background = 0
def setup():
    global img,img1,img2,background
    size(600,600)
    background = loadImage('background.jpg')
    img = loadImage('home.jpg')
    img1 = loadImage('home1.jpg')
    img2 = loadImage('home2.jpg')
def draw():
    global img,img1,img2,background
    image(background,0,0,650,650)
    fill(144,104,3)
    rect(200,200,200,200)
    image(img,220,250,50,50)
    image(img1,300,250,50,50)
    image(img2,220,320,50,50)
