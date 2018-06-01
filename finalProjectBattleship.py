#Christo Dragnev
#5/23/18
#battleshipGraphics.py


from ggame import *
from random import randint

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
red = Color(0xFF0000,1)
blackOutline = LineStyle(1,black)

EMPTY = 0
MISS = 1
HIT = 2

radius = 30

def buildboard():
    return [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]


def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    circle = CircleAsset(radius,blackOutline,white)
    blackCircle = CircleAsset(radius,blackOutline,black)
    redCircle = CircleAsset(radius,blackOutline,red)
    for r in range(0,5):
        for c in range(0,5):
            Sprite(circle,(10+r*(2*radius),10+(2*radius)*c))
            if data['board'][r][c]=='ship' and data['playerships']<=3:
                Sprite(blackCircle,(10+r*(2*radius),10+(2*radius)*c))
            
    for r in range(0,5):
        for c in range(0,5):
                Sprite(circle,(500+r*(2*radius),10+(2*radius)*c))
                if data['compboard'][r][c]=='compship':
                    Sprite(blackCircle,(500+r*(2*radius),10+(2*radius)*c))
                if data['compboard'][r][c]=='guess':
                    Sprite(redCircle,(500+r*(2*radius),10+(2*radius)*c))
            
            

def pickComputerShips():
    i = 0
    while i <= 2:
        row = randint(0,4)
        col = randint(0,4)
        data['compboard'][row][col]='compship'
        i+=1
    redrawAll()
    
def computerTurn():
    row = randint(0,4)
    col = randint(0,4)
    if data['turn']==False:
        if data['board'][row][col]==0:
            data['board'][row][col]='ship'
    

def mouseClick(event):
    row = int(event.x//60)
    col = int(event.y//60)
    data['board'][row][col]='ship'
    data['playerships']+=1
    if data['turn']==True and data['playerships']==4:
        data['compboard'][row][col]='guess'
        
        
        
    redrawAll()

            
    


if __name__ == '__main__':
    
    data = {}
    data['board'] = buildboard()
    data['compboard'] = buildboard()
    data['playerships'] = 0
    
    data['turn']=True
    
    App().listenMouseEvent('click',mouseClick)
    pickComputerShips()
    redrawAll()
    App().run()
