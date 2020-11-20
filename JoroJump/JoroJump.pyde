from platform_class import *
from player_class import *
from functions import *

gameState = 0
rectSize = 250
overJogar = False
overCreditos = False

def setup():
    #global setup options
    size(500, 800)
    rectMode(CENTER)
    background(255)
    
    global posXbotaoJogar, posYbotaoJogar
    posXbotaoJogar = width/2-150
    posYbotaoJogar = 0.17*height-50
    
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
        
        
def update(x, y):
    global overJogar
    overJogar = overRect(posXbotaoJogar, posYbotaoJogar, 250, 50)
        
        
def overRect(x, y, width, height):
    return x <= mouseX <= x + width and y <= mouseY <= y + height


def mousePressed():
    global gameState
    if gameState == 1:
        global platforms
        platforms = []
        starter_platform = platform([100, 700])
        platforms.append(starter_platform)
        global p1
        p1 = player()
        loop()
    
    if gameState == 0:
        if overJogar:
            gameState = 1 # inicia o jogo


def drawMenu():
    update(mouseX, mouseY)
    menuBackgroud = loadImage("footage/menuBackgroud.jpg")
    image(menuBackgroud, 0, 0);
    
    fill(255)
    #rect(width/2,0.17*height,250,50);
    rect(width/2,0.3*height,250,50);
    
    fill(0)
    textAlign(CENTER, CENTER)
    font = loadFont("fonts/3Dventure-72.vlw")  
    textFont(font)
    
    text("Jogar\n", width/2, 2*height/10)
    text("...", width/2, 3*height/10)
    
    textSize(30)
    text("Creditos", width/2, height/1.5)
    
    textSize(70)
    fill(255); rect(width/2, 700, width, 70)
    esquilo = loadImage("footage/esquilo.png")
    image(esquilo, 370, 600);
    fill(0); text("JoroJump", 200, 700)
    

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
        

    

        
        
