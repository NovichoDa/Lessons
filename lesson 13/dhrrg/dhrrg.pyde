def setup():
    size(600,400)
def moused():
    if mousePressed and (mouseButton == LEFT):
        fill(255,0,0)
        rect(50,50,50,50)
    if mousePressed and (mouseButton == RIGHT):
        fill(0,255,0)
        rect(50,50,50,50)
    elif mousePressed and (mouseButton == CENTER):
        fill(0,0,255)
        rect(50,50,50,50)
