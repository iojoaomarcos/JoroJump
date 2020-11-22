# JOROJUMP

# Carolina Ale
# Joao Marcos Santos
# Renner Souza

# Computacao Grafica
# Engenharia da Computacao @ Universidade Sao Francisco
# Professor Fabio Andrijauskas


add_library('minim')
from platform_class import *
from player_class import *
from functions import *

gameState = 0
rectSize = 250
overJogar = False
overCreditos = False
overBack = False

def setup():
    #global setup options
    size(500, 800)
    rectMode(CENTER)
    background(255)
    
    global posXbotaoJogar, posYbotaoJogar
    global posXbotaoCreditos, posYbotaoCreditos
    posXbotaoJogar = width/2-150
    posYbotaoJogar = 0.17*height-50
    posXbotaoCreditos = width/2
    posYbotaoCreditos = height/1.5
    
    
    #list of platforms
    global platforms
    platforms = []
    starter_platform = platform([100, 700])
    platforms.append(starter_platform)
    global p1
    p1 = player()
    
    #inicia o minim 
    global minim, s_tema, s_menu, s_gameover, s_out, s_jump
    minim = Minim(this)
    
    #musica do menu
    s_menu = minim.loadFile("sounds/hamsterdance.mp3", 2048)
    
    #som do pulo
    s_out = minim.getLineOut();
    s_jump = Sampler( "sounds/jump.mp3", 12, minim);
    s_jump.patch(s_out)
    
    #musica de Game Over
    s_gameover = minim.loadFile("sounds/gameover.mp3", 2048)
    
    #musica principal
    s_tema = minim.loadFile("sounds/tema.mp3", 2048)
    s_tema.shiftGain(s_tema.getGain(),-15,400)
    
    s_menu.loop()
    
    
def draw():
    if gameState == 0:
        drawMenu()
    if gameState == 1:
        textAlign(LEFT) # Ajusta o texto do Score 
        drawGame()
    if gameState == 2:
        drawCreditos()
        
        
def update(x, y):
    global overJogar
    global overCreditos    
    global overBack
    overJogar = overRect(posXbotaoJogar, posYbotaoJogar, 250, 50)
    overCreditos = overRect(posXbotaoCreditos, posYbotaoCreditos, 250, 50)
    overBack = overRect(0, 0, 50, 50)
        
        
def overRect(x, y, width, height):
    return x <= mouseX <= x + width and y <= mouseY <= y + height


def mousePressed():
    global gameState
    if gameState == 1:
        s_gameover.pause()
        s_gameover.rewind()
        s_tema.loop()
        global platforms
        platforms = []
        starter_platform = platform([100, 700])
        platforms.append(starter_platform)
        global p1
        p1 = player()
        loop()
    
    if gameState == 0:
        if overJogar:
            s_tema.loop()
            gameState = 1 # inicia o jogo
        if overCreditos:
            gameState = 2 # inicia a tela do menu
    
    if overBack:
        gameState = 0


def drawMenu():
    update(mouseX, mouseY)
    menuBackgroud = loadImage("footage/menuBackgroud.jpg")
    image(menuBackgroud, 0, 0);
    
    fill(255)
    rect(width/2,height/1.5,250,50);
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
    

def drawCreditos():
    update(mouseX, mouseY)
    background(230);
    back = loadImage("footage/back.png")
    image(back, 0,0)
    textAlign(CENTER, CENTER);
    textSize(30)
    text("Carolina Ale\nJoao Marcos Santos\nRenner Souza", width/2, width/3)
    text("Computacao Grafica\n @ \nUniversidade Sao Francisco", width/2, height/2.5)
    
    textSize(20)
    text("Professor: Fabio Andrijauskas", width/2, height/1.5)
    text("2020\\11", width/2, height/1.25)
    
    joro = loadImage("footage/Joro Original.jpg")
    image(joro, width-129, height-115)


def drawGame():
    s_menu.pause()
    frameRate(60)
    background(255)
    for platform in platforms:
        platform.display()
    p1.update(platforms)
    platform_manager(platforms)
    platform_sounds(p1, platforms)
    #this ends the game if the player falls off the screen
    if p1.ypos > height+25:
        background(0)
        #para a musica de fundo
        s_tema.pause()
        s_tema.rewind()
        s_gameover.loop()
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
        
def platform_sounds(p1, platforms):
    for platform in platforms:
        #quando o jogador colide com uma plataforma, aciona o som do pulo 
        if (((p1.ypos >= platform.ypos-30) and (p1.ypos <= platform.ypos+30) and (p1.yvel >= 0)) and ((p1.xpos >= platform.xpos-25) and (p1.xpos <= platform.xpos+75+25))):
            s_jump.trigger()
        else:
            pass
        
        
