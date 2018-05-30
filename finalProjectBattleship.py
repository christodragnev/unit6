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
    return [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]


def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    circle = CircleAsset(radius,blackOutline,white)
    blackCircle = CircleAsset(radius,blackOutline,black)
    for r in range(0,5):
        for c in range(0,5):
            Sprite(circle,(10+r*(2*radius),10+(2*radius)*c))
            if data['board'][r][c]=='ship':
                Sprite(blackCircle,(10+r*(2*radius),10+(2*radius)*c))
            
    for r in range(0,5):
        for c in range(0,5):
            Sprite(circle,(500+r*(2*radius),10+(2*radius)*c))
            
            

def pickComputerShips():
    return

def mouseClick(event):
    row = int(event.x//60)
    col = int(event.y//60)
    i=0
    while i<4:
        data['board'][row][col]='ship'
        i+=1
    redrawAll()

            
    


if __name__ == '__main__':
    
    data = {}
    data['board'] = buildboard()
    
    data['compboard'] = buildboard()
    
    App().listenMouseEvent('click',mouseClick)
    redrawAll()
    App().run()
