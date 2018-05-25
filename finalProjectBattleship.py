#Christo Dragnev
#5/23/18
#battleshipGraphics.py


from ggame import *
from random import randint

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
blackOutline = LineStyle(1,black)

radius = 30

def buildboard():
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    circle = CircleAsset(radius,blackOutline,white)
    for r in range(0,5):
        for c in range(0,5):
            Sprite(circle,(10+r*(2*radius),10+(2*radius)*c))
            
    for r in range(0,5):
        for c in range(0,5):
            Sprite(circle,(500+r*(2*radius),10+(2*radius)*c))
            

def pickComputerShips():
    return

def mouseClick(event):
    blackCircle = CircleAsset(radius,blackOutline,black)
    if (event.x < 70 and event.y < 70) and (event.x>10 and event.y >10):
            Sprite(blackCircle,(10,10))

    


if __name__ == '__main__':
    
    App().listenMouseEvent('click',mouseClick)
    redrawAll()
    App().run()