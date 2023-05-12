a = 0
b = 0
def setup():
    size(600,400)
    a = loadImage("hh.png")
def draw():
    global a,b
    image(a,50,50,50,50)
    rect(300,200,50,50)
    textSize(26)
    textAlign(CENTER,CENTER)
    text(b,400,100)
def mouseClicked():
    global a,b
    if mouseX > 300 and mouseX < 350 and mouseY > 200 and mouseY < 250:
        b += 1
