#Christo Dragnev
#5/23/18
#battleshipGraphics.py


from ggame import *

white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
blackOutline = LineStyle(1,black)

circleRadius = 20

def buildboard():
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def redrawAll():
    circle = CircleAsset(circleRadius,blackOutline,white)
    for r in range(0,5):
        for c in range(0,5):
            Sprite(circle,(10+r*(2*circleRadius+10),10+(2*circleRadius+10)*c))
    for item in App().spritelist[:]:
        item.destroy()

if __name__ == '__main__':
    redrawAll()
    App().run()