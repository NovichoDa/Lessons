img = 0
img1 = 0
img2 = 0
img3 = 0
img4 = 0
img5 = 0
img6 = 0
img7 = 0
img8 = 0
a = 0
s =0
d = 0
f = 0
g = 0
h = 0
j = 0
k = 0
l = 0
def setup():
    global img,img1,img2,background,a,s,d,f,g,h,j,k,l,img3,img4,img5,img6,img7,img8
    size(600,600)
    img = loadImage('bipbip.png')
    img1 = loadImage('bipbip2.png')
    img2 = loadImage('bipbip3.png')
    img3 = loadImage('pipi.png')
    img4 = loadImage('pipi2.png')
    img5 = loadImage('pipi3.png')
    img6 = loadImage('aa.png')
    img7 = loadImage('aa2.png')
    img8 = loadImage('aa3.png')
def draw():
    global img,img1,img2,background,img3,img4,img5,img6,img7,img8,a,s,d,f,g,h,j,k,l
    background(255)
    image(img,a,0,100,50)
    image(img1,s,50,100,50)
    image(img2,d,100,100,50)
    image(img3,f,150,100,50)
    image(img4,g,200,100,50)
    image(img5,h,250,100,50)
    image(img6,j,300,100,50)
    image(img6,j,300,100,50)
    image(img7,k,350,100,50)
    image(img8,l,400,100,50)
    a += 1
    s += 2
    d += 6
    f += 3
    g += 8
    h += 4
    j += 5
    k += 7
    l += 9
    if frameCount > 150:
        noLoop()
