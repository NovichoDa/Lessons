#1.Добавить апгрейд на клик в секунду
#2.Добавить показ кликов в секунду и при нажатии на экран
#3.Выдача денег каждые 10 минут
add_library('sound')
a = 0
b = 0
clicks = 100
img = 0
img2 = 0
buy = 100
xDif = 500
yDif = 100
click = 1
def setup():
    global a,img, b, clicks, img2
    size(600,400)
    a = SoundFile(this,"ll.mp3")
    b = SoundFile(this,"up.mp3")
    img = loadImage("photo.png")
    img2 = loadImage("upgrade.png")
def draw():
    background(255)
    global a,img, b, clicks, img2, buy
    image(img,200,200,220,220)
    image(img2,500,100,50,50)
    fill(0)
    textSize(35)
    textAlign(CENTER,CENTER)
    text(clicks,320,100)
    textSize(25)
    text(buy,525,170)
def mouseClicked():
    global clicks,xDif,yDif,click,buy
    xDif = 500 - mouseX
    yDif = 100 - mouseY
    a.play()
    clicks += click
    if sqrt(xDif*xDif + yDif*yDif) < 50:
        if buy < clicks:
            clicks -= buy
            buy += 200
            click *= 2
