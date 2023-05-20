#1.Добавить апгрейд на клик в секунду
#2.Добавить показ кликов в секунду и при нажатии на экран
#3.Выдача денег каждые 10 минут
a = 0
b = 0
clicks = 1000
img = 0
img2 = 0
buy = 100
xDif = 500
yDif = 100
xDif2 = 500
yDif2 = 200
click = 1
buy2 = 100
last_time = 0
interval = 2
cps = 0
def setup():
    global a,img, b, clicks, img2, buy2, xDif2, yDif2, last_time,interval,cps
    size(600,400)
    img = loadImage("photo.png")
    img2 = loadImage("upgrade.png")
def draw():
    background(255)
    global a,img, b, clicks, img2, buy, buy2, xDif2, yDif2, last_time,interval,cps
    last_time = second()
    image(img,200,200,220,220)
    image(img2,500,100,50,50)
    image(img2,500,200,50,50)
    fill(0)
    textSize(35)
    textAlign(CENTER,CENTER)
    text(clicks,320,100)
    text()
    textSize(25)
    text(buy,525,170)
    text(buy2,525,270)
    if second() - last_time >= interval:
        if cps > 0:
            clicks+=cps
            last_time = second()
def mouseClicked():
    global clicks,xDif,yDif,click,buy, buy2, xDif2, yDif2, last_time,interval,cps
    xDif = 500 - mouseX
    yDif = 100 - mouseY
    xDif2 = 500 - mouseX
    yDif2 = 200 - mouseY
    clicks += click
    if sqrt(xDif*xDif + yDif*yDif) < 50:
        if buy < clicks:
            clicks -= buy
            if buy > 499:
                buy += 400
                click *= 2
            else:
                buy += 200
                click *= 2
    if sqrt(xDif2*xDif2 + yDif2*yDif2) < 50:
        if buy2 < clicks:
            clicks -= buy2
            if buy2 > 499:
                buy2 += 400
            else:
                buy2 += 200
