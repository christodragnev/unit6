#Christo Dragnev
#5/23/18
#battleshipGraphics.py


from ggame import *

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
blackOutline = LineStyle(1,black)

def buildboard():
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def redrawAll():
    circle = CircleAsset(30,blackOutline,white)
    for r in range(0,5):
        for c in range(0,5):
            Sprite(circle,(10+r*(2*25+10),10+(2*25+10)*c))

if __name__ == '__main__':
    redrawAll()
    App().run()