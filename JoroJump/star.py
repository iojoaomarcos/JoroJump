

class Star:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = random(-self.width/2, self.width/2)
        self.y = random(-self.height/2, self.height/2)
        self.z = random(self.width/2)
        self.pz = self.z
    
    def update(self, speed):
        #Update the speed variable with the value from the mouse.
        #Note, the smaller z is the faster the star moves.
        self.z = self.z - speed
        #Resets the star back on the screen after it has moved outside
        #the window.
        if self.z < 1:
            self.z = self.width/2
            self.x = random(-self.width/2, self.width/2)
            self.y = random(-self.height/2, self.height/2)
            self.pz = self.z
         
    def show(self):
        fill(255)
        noStroke()
        #Draws the stars at their updated position. 
        self.sx = map(self.x / self.z, 0, 1, 0, self.width/2)
        self.sy = map(self.y / self.z, 0, 1, 0, self.height/2)
        
        #Increases the size of the stars the closer they get to the edge.
        r = map(self.z, 0, self.width/2, 10, 0)
        ellipse(self.sx, self.sy, r, r)
        
        #Gets the previous position of the star so a line can be drawn that
        #trails behind the star.
        self.px = map(self.x / self.pz, 0, 1, 0, self.width/2)
        self.py = map(self.y / self.pz, 0, 1, 0, self.height/2)
        self.pz = self.z
        
        stroke(255)
        strokeWeight(2)
        line(self.px, self.py, self.sx, self.sy)
