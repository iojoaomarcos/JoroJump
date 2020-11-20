gameState = 0
PImage menuBackgroud;

from platform_class import *
from player_class import *
from functions import *

def mousePressed():
    global platforms
    platforms = []
    starter_platform = platform([100, 700])
    platforms.append(starter_platform)
    global p1
    p1 = player()
    loop()

def setup():
    #global setup options
    size(500, 800)
    rectMode(CENTER)
    background(255)
    
    #list of platforms
    global platforms
    platforms = []
    starter_platform = platform([100, 700])
    platforms.append(starter_platform)
    global p1
    p1 = player()
    
    
def draw():
    if gameState == 0:
        drawMenu()
    if gameState == 1:
        drawGame()

def drawMenu():
    
    
    

def drawGame():
    frameRate(30)
    background(255)
    for platform in platforms:
        platform.display()
    p1.update(platforms)
    platform_manager(platforms)
    
    #this ends the game if the player falls off the screen
    if p1.ypos > height+25:
        background(0)
        fill(255, 255, 255)
        textAlign(CENTER, CENTER)
        textSize(80)
        text("GAME", width/2, 2*height/10)
        text("OVER", width/2, 3*height/10)
        textSize(40)
        text("Score: "+str(p1.score/100), width/2, 5*height/10)
        text("Retry: [CLICK]", width/2, 7*height/10)
        text("Exit: [ESC]", width/2, 8*height/10)
        textAlign(LEFT)
        noLoop()
        

    

        
        
