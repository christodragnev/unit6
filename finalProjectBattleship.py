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
            i = 0
            while i<=3:
                if data['board'][r][c]=='ship':
                    Sprite(blackCircle,(10+r*(2*radius),10+(2*radius)*c))
                i+=1
            
    for r in range(0,5):
        for c in range(0,5):
                Sprite(circle,(500+r*(2*radius),10+(2*radius)*c))
                if data['compboard'][r][c]=='compship':
                    Sprite(blackCircle,(10+r*(2*radius),10+(2*radius)*c))
            
            

def pickComputerShips():
    i = 0
    while i <= 3:
        row = randint(0,5)
        col = randint(0,5)
        data['compboard'][row][col]='compship'
        i+=1
    redrawAll()

def mouseClick(event):
    row = int(event.x//60)
    col = int(event.y//60)
    data['board'][row][col]='ship'
    redrawAll()

            
    


if __name__ == '__main__':
    
    data = {}
    data['board'] = buildboard()
    
    data['compboard'] = buildboard()
    
    App().listenMouseEvent('click',mouseClick)
    pickComputerShips()
    redrawAll()
    App().run()
