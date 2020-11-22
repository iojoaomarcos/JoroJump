class platform(object):
    def __init__(self, coords):
        self.xpos = coords[0]
        self.ypos = coords[1]
    
        
    def display(self,plat):
        #strokeWeight(10)
        #stroke(self.colour)
        #line(self.xpos, self.ypos, self.xpos+75, self.ypos)
        image(plat[0],self.xpos, self.ypos, plat[0].width * 0.05, plat[0].height* 0.05)
        
    def destroy(self,s_broke):
        s_broke.trigger()
        self.xpos = 600
