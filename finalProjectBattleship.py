#Christo Dragnev
#5/23/18
#battleshipGraphics.py


from ggame import *
from random import randint

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
red = Color(0xFF0000,1)
blue = Color(0x009AFF, 1)
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
        
    emptyCircle = CircleAsset(radius,blackOutline,white)
    shipCircle = CircleAsset(radius,blackOutline,black)
    hitCircle = CircleAsset(radius,blackOutline,red)
    missCircle = CircleAsset(radius,blackOutline,blue)
    
    for r in range(0,5):
        for c in range(0,5):
            if data['board'][r][c] == 0:
                Sprite(emptyCircle,(10+r*(2*radius),10+(2*radius)*c))
            elif data['board'][r][c] == 'ship':
                Sprite(shipCircle,(10+r*(2*radius),10+(2*radius)*c))
            elif data['board'][r][c] == MISS:
                Sprite(missCircle,(10+r*(2*radius),10+(2*radius)*c))
            elif data['board'][r][c] == HIT:
                Sprite(hitCircle,(10+r*(2*radius),10+(2*radius)*c))
            
    for r in range(0,5):
        for c in range(0,5):
                if data['compboard'][r][c] == 0:
                    Sprite(emptyCircle,(500+r*(2*radius),10+(2*radius)*c))
                elif data['compboard'][r][c]=='compship':
                    Sprite(emptyCircle,(500+r*(2*radius),10+(2*radius)*c))
                elif data['compboard'][r][c] == MISS:
                    Sprite(missCircle,(500+r*(2*radius),10+(2*radius)*c))
                elif data['compboard'][r][c] == HIT:
                    Sprite(hitCircle,(500+r*(2*radius),10+(2*radius)*c))
                
            

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
    if data['board'][row][col] == 'ship':
        data['board'][row][col] = HIT
        data['playerHits'] += 1
        if data['playerHits'] == 3:
            data['endGame'] = True
            print('Computer wins!')
        redrawAll()
    elif data['board'][row][col] == 0:
        data['board'][row][col] = MISS
        redrawAll()
    else:
        computerTurn()

def mouseClick(event):
    row = int(event.x//60)
    col = int(event.y//60)
    if data['end']==False:
        if  data['playerships']<3:
            data['board'][row][col]='ship'
            data['playerships']+=1
        elif data['playerships']==3:
            if data['compboard'][((event.x)-500)//60][col] == 'compship':
                data['compboard'][((event.x)-500)//60][col] = HIT
                data['computerHits'] += 1
                if data['computerHits'] == 3:
                    data['end'] = True
                    print('Player wins!')
                else:
                    computerTurn()
                redrawAll()
            elif data['compboard'][(event.x-500)//60][col] == 0:
                data['compboard'][(event.x-500)//60][col] = MISS
                computerTurn()
                redrawAll()
            
    redrawAll()
    
if __name__ == '__main__':
    
    data = {}
    data['board'] = buildboard()
    data['compboard'] = buildboard()
    data['playerships'] = 0
    data['playerHits'] = 0
    data['computerHits'] = 0
    data['end'] = False
    
    
    data['turn']=True
    
    App().listenMouseEvent('click',mouseClick)
    pickComputerShips()
    redrawAll()
    App().run()
