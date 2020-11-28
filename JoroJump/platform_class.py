class platform(object):
    def __init__(self, coords):
        self.xpos = coords[0]
        self.ypos = coords[1]
    
        
    def display(self,plat,player):
        if player.score/100 <= 300:
            image(plat[0],self.xpos, self.ypos, plat[0].width * 0.05, plat[0].height* 0.05)
        if player.score/100 > 300 and player.score/100 <= 500:
            image(plat[1],self.xpos, self.ypos, plat[1].width * 0.05, plat[1].height* 0.05)
        if player.score/100 > 500 and player.score/100 <= 700: 
            image(plat[2],self.xpos, self.ypos, plat[2].width * 0.05, plat[2].height* 0.05)
        if player.score/100 > 700:
            image(plat[3],self.xpos, self.ypos, plat[3].width * 0.05, plat[3].height* 0.05)
            
    def destroy(self,s_broke):
        s_broke.trigger()
        self.xpos = 600
