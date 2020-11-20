class player():
    def __init__(self):
        self.xpos = 135
        self.ypos = 475
        self.xvel = 0
        self.yvel = 0
        self.accel_g = 2
        self.colour = color(random(256), random(256), random(256))
        self.climb = 0
        self.score = 0
        
    def update(self, platforms):
        #this changes the horizontal velocities based on arrow keys
        if (keyPressed and (keyCode == LEFT)):
            self.xpos -= 10
        elif (keyPressed and (keyCode == RIGHT)):
            self.xpos += 10
        
        #this changes the vertical velocity based on acceleration due to gravity
        self.yvel += self.accel_g
        
        #this updates the player position and velocity on collision
        for platform in platforms:
            if (((self.ypos >= platform.ypos-30) and (self.ypos <= platform.ypos+30) and (self.yvel >= 0)) and ((self.xpos >= platform.xpos-25) and (self.xpos <= platform.xpos+75+25))):
                self.ypos = platform.ypos-25
                self.yvel = -28
                #print(self.score/100)
                if self.score/100 > 200:
                    if random(5) > 3:
                        platform.destroy()
                elif self.score/100 > 500:
                    platform.destroy()
        
        #this updates the player position each frame based on its velocity
        self.xpos += self.xvel
        self.ypos += self.yvel
        
        #this wraps left and right
        if self.xpos <= 0:
            self.xpos = (width+self.xpos)
        if self.xpos >= width:
            self.xpos = (self.xpos-width)
        
        #this "moves" the view frame if the player moves too far up
        if self.ypos < 300:
            self.climb = (300-self.ypos)
            self.ypos = 300
            for platform in platforms:
                platform.ypos += self.climb
                self.score += self.climb
            
        #this re-draws the player and score each frame
        noStroke()
        fill(self.colour)
        rect(self.xpos, self.ypos, 50, 50)
        fill(0, 0, 0)
        textSize(30)
        text("Score: "+str(self.score/100), 20, 40)