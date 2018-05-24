#Christo Dragnev
#5/23/18
#battleshipGraphics.py


from ggame import *

red = Color(0xFF0000,1) #this is the color red
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

def buildboard():
    blackOutline = LineStyle(1,black)
    blueCircle = CircleAsset(30,blackOutline,blue) #radius, outline, full
    Sprite(blueCircle,(25,25))
    App().run()

board = [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','y']]

print(buildboard())