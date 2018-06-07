#Christo Dragnev
#5/23/18
#battleshipGraphics.py


from ggame import *
from random import randint

#color variables
white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
red = Color(0xFF0000,1)
blue = Color(0x009AFF, 1)
blackOutline = LineStyle(1,black)


#constants
EMPTY = 0
MISS = 1
HIT = 2
radius = 30

def buildboard():  #creates empty board
    return [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]


def redrawAll(): 
    for item in App().spritelist[:]: #deletes are graphics on screen
        item.destroy()
        
    #graphics variables   
    emptyCircle = CircleAsset(radius,blackOutline,white)
    shipCircle = CircleAsset(radius,blackOutline,black)
    hitCircle = CircleAsset(radius,blackOutline,red)
    missCircle = CircleAsset(radius,blackOutline,blue)
    playerBoardText = TextAsset('PlayerBoard',fill=black, style='bold 15pt Times')
    computerBoardText = TextAsset('ComputerBoard',fill=black, style='bold 15pt Times')
    blackCircleText = TextAsset('=PlayerShip',fill=black, style='bold 15pt Times')
    blueCircleText = TextAsset('=Miss',fill=black, style='bold 15pt Times')
    redCircleText = TextAsset('=Hit',fill=black, style='bold 15pt Times')
    computerWinText = TextAsset('Computer Wins!!',fill=black, style='bold 50pt Times')
    playerWinText = TextAsset('Player Wins!!',fill=black, style='bold 50pt Times')

    Sprite(playerBoardText,(120,320))
    Sprite(computerBoardText,(620,320))
    Sprite(blackCircleText,(70,355))
    Sprite(shipCircle, (10,340))
    Sprite(blueCircleText,(70,420))
    Sprite(missCircle, (10,400))
    Sprite(redCircleText,(70,480))
    Sprite(hitCircle, (10,460))
    
    for r in range(0,5): #for user board, places circle where user clicked, and checks if space is empty or not
        for c in range(0,5):
            if data['board'][r][c] == 0:
                Sprite(emptyCircle,(10+r*(2*radius),10+(2*radius)*c)) #if circle is empty, place ship
            elif data['board'][r][c] == 'ship':
                Sprite(shipCircle,(10+r*(2*radius),10+(2*radius)*c))  #if circle is empty, place ship
            elif data['board'][r][c] == MISS:
                Sprite(missCircle,(10+r*(2*radius),10+(2*radius)*c)) #if computer guesses in empty circle, then place missCircle
            elif data['board'][r][c] == HIT:
                Sprite(hitCircle,(10+r*(2*radius),10+(2*radius)*c)) #if computer guesses in ship circle, then place hitCircle
            
    for r in range(0,5): #for computer board, places circle where user clicked, and checks if space is empty or not
        for c in range(0,5):
                if data['compboard'][r][c] == 0:
                    Sprite(emptyCircle,(500+r*(2*radius),10+(2*radius)*c))
                elif data['compboard'][r][c]=='compship':
                    Sprite(emptyCircle,(500+r*(2*radius),10+(2*radius)*c))
                elif data['compboard'][r][c] == MISS:
                    Sprite(missCircle,(500+r*(2*radius),10+(2*radius)*c))
                elif data['compboard'][r][c] == HIT:
                    Sprite(hitCircle,(500+r*(2*radius),10+(2*radius)*c))
    
    if data['computerHits'] == 3: #checks to see if all 3 computer ships have been hit, if so, player wins
        data['end'] = True
        Sprite(playerWinText,(320,200))
    elif data['playerHits'] == 3: #checks to see if all 3 player ships have been hit, if so, player wins
        data['end'] = True
        Sprite(computerWinText,(300,200))
            

def pickComputerShips(): #randomly picks 3 places to put computer ships
    i = 0
    while i <= 2:
        row = randint(0,4)
        col = randint(0,4)
        if data['compboard'][row][col] == 0:
            data['compboard'][row][col]='compship'
            i+=1
    redrawAll()
    
def computerTurn():  #randomly chooses places to guess on the player board
    row = randint(0,4)
    col = randint(0,4)
    
    if data['board'][row][col] == 'ship': #if player hits one ship, then a variable keeping track of the number of player hits is added by one
        data['board'][row][col] = HIT
        data['playerHits'] += 1
        if data['playerHits'] == 3: #if the variable keeping track of number of player hits = 3, then computer wins
            data['end'] = True
        redrawAll()
    elif data['board'][row][col] == 0:
        data['board'][row][col] = MISS
        redrawAll()
    else:
        computerTurn()

def mouseClick(event):  #figures out what row and column the user clicked and places a ship or guess where user clicked
    row = int(event.x//60) 
    col = int(event.y//60)
    if data['end']==False: 
        if  data['playerships']<3: #only 3 ships can be placed
            if data['board'][row][col]==EMPTY: #makes sure you can't place a ship on top of each other
                data['board'][row][col]='ship'
                data['playerships']+=1 
        elif data['playerships']==3: #once ships have been palced, guessing starts
            if data['compboard'][((event.x)-500)//60][col] == 'compship':
                data['compboard'][((event.x)-500)//60][col] = HIT
                data['computerHits'] += 1
                if data['computerHits'] == 3: #if number of ships on computer side equals 3, then player wins
                    data['end'] = True
                else:
                    computerTurn() 
                redrawAll()
            elif data['compboard'][(event.x-500)//60][col] == 0: 
                data['compboard'][(event.x-500)//60][col] = MISS
                computerTurn()
                redrawAll()
            
    redrawAll()
    
if __name__ == '__main__':
    
    #variables
    data = {}
    data['board'] = buildboard()
    data['compboard'] = buildboard()
    data['playerships'] = 0
    data['playerHits'] = 0
    data['computerHits'] = 0
    data['end'] = False
    
    App().listenMouseEvent('click',mouseClick)
    pickComputerShips()
    redrawAll()
    App().run()
