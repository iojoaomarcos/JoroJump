# JOROJUMP

# Carolina Ale                 002.2017.01385
# Joao Marcos Santos           002.2017.00153
# Renner Souza                 002.2017.00934

# Computacao Grafica
# Engenharia da Computacao @ Universidade Sao Francisco
# Professor Fabio Andrijauskas

add_library('minim')
from platform_class import *
from player_class import *
from functions import *
from powerup_class import *
from star import*

# gameState representa se está em jogo, menu, créditos, etc
gameState = 0
overJogar = False
overCreditos = False
overBack = False
overRightSkinSelector = False
overLeftSkinSelector = False

#skins
joroStyleID = ["Joro", "Indiana Joro", "Joro Bros", "Lord Joro", "Bruxoro", "Joranjo"]
joroStyleQuantity = len(joroStyleID)
joroStylePic = []




def setup():
    size(500, 800)
    rectMode(CENTER)
    background(255)
    
    #campo de estrelas(ultima fase)
    global stars,speed
    stars = []
    speed = 1.0
    [stars.append(Star(width, height)) for i in range(800)]
    speed = map(10, 0, width, 0, 100)
    
    #skins do personagem
    joroStylePic.append(loadImage("footage/Esquilo/Esquilo_Standard.png"))
    joroStylePic.append(loadImage("footage/Esquilo/Esquilo_Standard_Skin1_Cowboy.png")) 
    joroStylePic.append(loadImage("footage/Esquilo/Esquilo_Standard_Skin2_Mario.png"))
    joroStylePic.append(loadImage("footage/Esquilo/Esquilo_Standard_Skin3_Cartola.png"))
    joroStylePic.append(loadImage("footage/Esquilo/Esquilo_Standard_Skin4_Bruxa.png"))
    joroStylePic.append(loadImage("footage/Esquilo/Esquilo_Standard_Skin5_Celeste.png"))
    
    global joroSelected
    joroSelected = 0
    
    global posXbotaoJogar, posYbotaoJogar
    global posXbotaoCreditos, posYbotaoCreditos
    posXbotaoJogar = width/2-150
    posYbotaoJogar = 0.17*height-50
    posXbotaoCreditos = width/2
    posYbotaoCreditos = height/1.5
    
    
    #backgrounds
    global ground,wood,sky,space
    ground = loadImage("footage/backgrounds/ground.jpg")
    wood = loadImage("footage/backgrounds/wood.jpg")
    sky = loadImage("footage/backgrounds/sky.jpg")
    space = loadImage("footage/backgrounds/star.jpg")
    
    #platskins
    global plat
    plat = []
    plat.append(loadImage("footage/Platforms/plat0.png"))
    plat.append(loadImage("footage/Platforms/plat1.png"))
    plat.append(loadImage("footage/Platforms/plat2.png"))
    plat.append(loadImage("footage/Platforms/plat3.png"))
    
    #powerupskin
    global acorn
    acorn = loadImage("footage/PowerUp/bolota2.png")    
    
    #plataformas
    global platforms
    platforms = []
    starter_platform = platform([100, 700])
    platforms.append(starter_platform)
    global p1
    p1 = player()
    
    #powerup
    global powerups 
    powerups = []
    starter_powerup = powerup([random(425), 85])
    powerups.append(starter_powerup) 
       
    #inicia o minim 
    global minim, s_tema, s_menu, s_gameover, s_out, s_jump,s_out2,s_broke,s_out3,s_pwjump
    minim = Minim(this)
    
    #musica do menu
    s_menu = minim.loadFile("sounds/hamsterdance.mp3", 2048)
    
    #som do pulo
    s_out = minim.getLineOut();
    s_jump = Sampler( "sounds/jump.mp3", 12, minim);
    s_jump.patch(s_out)
    
    #som da plat quebrando
    s_out2 = minim.getLineOut();
    s_broke = Sampler( "sounds/broke.mp3", 12, minim);
    s_broke.patch(s_out2) 
    
    #som do power up
    s_out3 = minim.getLineOut();
    s_pwjump = Sampler( "sounds/powerjump.mp3", 12, minim);
    s_pwjump.patch(s_out3)      
    
    #musica de Game Over
    s_gameover = minim.loadFile("sounds/gameover.mp3", 2048)
    
    #musica principal
    s_tema = minim.loadFile("sounds/tema.mp3", 2048)
    s_tema.shiftGain(s_tema.getGain(),-15,400)
    
    s_menu.loop()
    
# Funcao Principal para desenhar na tela o proprio jogo em si, menu e creditos
def draw(): 
    if gameState == 0:
        drawMenu()
    if gameState == 1:
        textAlign(LEFT) # Ajusta o texto do Score 
        drawGame()
    if gameState == 2:
        drawCreditos()
        
# Verifica e atualiza a posicao do mouse        
def update(x, y):
    global overJogar
    global overCreditos    
    global overBack
    global overRightSkinSelector
    global overLeftSkinSelector
    
    overJogar = overRect(posXbotaoJogar, posYbotaoJogar, 250, 50)
    overCreditos = overRect(posXbotaoCreditos/2, posYbotaoCreditos-25, 250, 50)
    overBack = overRect(0, 0, 50, 50)
    overRightSkinSelector = overRect(width-80, 360, 200, 200)
    overLeftSkinSelector = overRect(0, 360, 80, 80)
        
# Calcula a distancia entre a posicao do mouse e posicao do botao        
def overRect(x, y, width, height):
    return x <= mouseX <= x + width and y <= mouseY <= y + height

def drawMenu():
    global joroSelected
    global joroStylePic
    update(mouseX, mouseY)
    menuBackgroud = loadImage("footage/menuBackgroud.jpg")
    image(menuBackgroud, 0, 0);
   
    fill(255)
    rect(width/2,height/1.5,250,50);
    rect(width/2,0.5*height,350,50);
    rect(width/2,height*0.166,250,55);
    
    fill(0)
    textAlign(CENTER, CENTER)
    font = loadFont("fonts/3Dventure-72.vlw")  
    textFont(font)
    
    text("Jogar\n", width/2, 2*height/10)
    
    image(joroStylePic[joroSelected],150,200, joroStylePic[joroSelected].width * 0.1, joroStylePic[joroSelected].height* 0.1)
    
    textSize(42)
    text(joroStyleID[joroSelected], width/2, 0.5*height)
    arrow = loadImage("footage/arrow.png")
    leftArrow = loadImage("footage/2arrow.png")
    arrow.resize(80, 80)
    leftArrow.resize(80, 80)
    image(leftArrow, 0, 360) 
    image(arrow, width-80, 360)
      
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
    text("Computacao Grafica\n @ \nUniversidade \nSao \nFrancisco", width/2, height/2.5)
    
    textSize(20)
    text("Professor: Fabio Andrijauskas", width/2, height/1.5)
    text("2020\\11", width/2, height/1.25)
    
    joro = loadImage("footage/Joro Original.jpg")
    image(joro, width-129, height-115)


def drawGame():
    s_menu.pause()
    frameRate(60)
    
    if p1.score/100 <= 1000:
        setBackground(p1)
    
    if p1.score/100 > 1000:
        background(0)
        for i in range(len(stars)):
            stars[i].update(speed)
            stars[i].show()
    
    for platform in platforms:
        platform.display(plat,p1)
        
    for powerup in powerups:
        powerup.display(acorn)  
          
    p1.display(joroStylePic,joroSelected) 
    p1.update(platforms,s_broke,powerups,s_pwjump,s_jump)
    platform_manager(platforms)
    powerup_manager(powerups)

    #Quando o jogador cai para fora da tela: Game Over
    if p1.ypos > height+25:
        background(0)
        #para a musica de fundo
        s_tema.pause()
        s_tema.rewind()
        s_gameover.play()
        fill(255, 255, 255)
        textAlign(CENTER, CENTER)
        textSize(80)
        text("GAME", width/2, 2*height/10)
        text("OVER", width/2, 3*height/10)
        textSize(40)
        text("Pontos: "+str(p1.score/100), width/2, 5*height/10)
        text("Main Menu: [UP]", width/2, 0.6*height)
        text("Retry: [CLICK]", width/2, 7*height/10)
        text("Exit: [ESC]", width/2, 8*height/10)
        textAlign(LEFT)
        
def mousePressed():
    global gameState
    global joroSelected
    
    if gameState == 1:
        s_gameover.pause()
        s_gameover.rewind()
        s_tema.loop()
        global platforms
        platforms = []
        starter_platform = platform([100, 700])
        platforms.append(starter_platform)
        global powerups 
        powerups = []
        starter_powerup = powerup([random(425), 85])
        powerups.append(starter_powerup) 
        global p1
        p1 = player()
        loop()
    
    if gameState == 0:
        if overJogar:
            s_tema.loop()
            global platforms
            platforms = []
            starter_platform = platform([100, 700])
            platforms.append(starter_platform)
            global powerups 
            powerups = []
            starter_powerup = powerup([random(425), 85])
            powerups.append(starter_powerup) 
            global p1
            p1 = player()
            gameState = 1 # inicia o jogo
        if overCreditos:
            gameState = 2 # inicia a tela do menu
    
    if overBack: #volta para o menu
        gameState = 0
        
    if overRightSkinSelector:
        if joroSelected == (joroStyleQuantity - 1):
            joroSelected = 0
        else:
            joroSelected += 1
    
    if overLeftSkinSelector:
        print(joroSelected)
        if joroSelected == 0:
            joroSelected = joroStyleQuantity - 1
        else:
            joroSelected -= 1

def keyPressed():
    global gameState
    global p1
    if keyCode == UP:
        s_tema.pause()
        s_tema.rewind()
        s_gameover.pause()
        s_gameover.rewind()
        s_menu.rewind()
        s_menu.loop()
        gameState = 0
        drawMenu()                    

def setBackground(p1):
        if p1.score/100 <= 300:
            background(ground)
        if p1.score/100 > 300 and p1.score/100 <= 500:
            background(wood)
        if p1.score/100 > 500 and p1.score/100 <= 700: 
            background(sky)
        if p1.score/100 > 700 and p1.score/100 <= 1000:
            background(space)
    
            
# Joяoзззззззззззззpa
