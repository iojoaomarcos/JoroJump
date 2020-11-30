class player():
    def __init__(self):
        self.xpos = 135
        self.ypos = 475
        self.xvel = 0
        self.yvel = 0
        self.accel_g = 2
        self.climb = 0
        self.score = 0
        
    def update(self, platforms,s_broke,powerups,s_pwjump,s_jump):
        #movimento do jogador
        if (keyPressed and (keyCode == LEFT)):
            self.xpos -= 10
        elif (keyPressed and (keyCode == RIGHT)):
            self.xpos += 10
        
        #gravidade
        self.yvel += self.accel_g
        
        #colisao do jogador com plataforma
        for platform in platforms:
            if (((self.ypos >= platform.ypos-30) and (self.ypos <= platform.ypos+30) and (self.yvel >= 0)) and ((self.xpos >= platform.xpos-25) and (self.xpos <= platform.xpos+60+25))):
                s_jump.trigger()
                self.ypos = platform.ypos-25
                self.yvel = -28
                
                #fase wood
                if self.score/100 > 300 and self.score/100 <= 500 :
                    if random(6) > 5:
                        platform.destroy(s_broke)
                        
                #fase sky        
                elif self.score/100 > 500 and self.score/100 <= 700:
                    if random(6) > 4:
                        platform.destroy(s_broke)
                    
                #fase space
                elif self.score/100 > 700 and self.score/100 <= 900 :
                    if random(2) > 1:
                        platform.destroy(s_broke)
                    
                #fase infinity
                elif self.score/100 > 1000:
                        platform.destroy(s_broke) 
                        
        #colisao do jogador com powerup                   
        for powerup in powerups:
            if (((self.ypos >= powerup.ypos-60) and (self.ypos <= powerup.ypos+60) and (self.yvel >= 0)) and ((self.xpos >= powerup.xpos-60) and (self.xpos <= powerup.xpos+60))):
                self.ypos = powerup.ypos-25
                self.yvel = -50
                powerup.destroy(s_pwjump)  
                      
        #velocidade do jogador
        self.xpos += self.xvel
        self.ypos += self.yvel
        
        #junta os lados da tela
        if self.xpos <= 0:
            self.xpos = (width+self.xpos)
        if self.xpos >= width:
            self.xpos = (self.xpos-width)
        
        #movimentacao vertical do jogo
        if self.ypos < 300:
            self.climb = (300-self.ypos)
            self.ypos = 300
            for platform in platforms:
                platform.ypos += self.climb
                self.score += self.climb
            for powerup in powerups:
                powerup.ypos += self.climb
                self.score += self.climb     
                       
    #desenha o jogador
    def display(self,joroStylePic,joroSelected):         
        if (keyCode == RIGHT):
            image(joroStylePic[joroSelected],self.xpos, self.ypos, joroStylePic[joroSelected].width * 0.04, joroStylePic[joroSelected].height* 0.04)
        elif (keyCode == LEFT):
            pushMatrix()
            scale(-1, 1)
            image(joroStylePic[joroSelected],- self.xpos - 50, self.ypos, joroStylePic[joroSelected].width * 0.04, joroStylePic[joroSelected].height* 0.04)
            popMatrix()
        else:
            image(joroStylePic[joroSelected],self.xpos, self.ypos, joroStylePic[joroSelected].width * 0.04, joroStylePic[joroSelected].height* 0.04)
            
        fill(255, 255, 255)
        textSize(30)
        text("Pontos: "+str(self.score/100), 20, 40)

 
