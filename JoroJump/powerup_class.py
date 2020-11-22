class powerup(object):
    def __init__(self, coords):
        self.xpos = coords[0]
        self.ypos = coords[1]
        
    def display(self,acorn):

        image(acorn,self.xpos, self.ypos,50, 50)
    
    def destroy(self,s_pwjump):
        s_pwjump.trigger()
        self.xpos = 600
