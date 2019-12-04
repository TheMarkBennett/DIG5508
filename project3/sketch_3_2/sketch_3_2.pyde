# Even though there are multiple objects, we still only need one class. 
# No matter how many cookies we make, only one cookie cutter is needed.
class Car(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
            
    def setcolor(self, newcolor):
        self.c = newcolor    
            
 
    
myCar1 = Car(color(255, 0, 0), 0, 100, 2)
myCar2 = Car(color(0, 255, 255), 0, 10, 1)


class Tree(object):
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
            
myTree1 = Tree(color(random(0,255), random(0,255), random(0,255)), random(0,100), random(0,100), random(0,8))
myTree2 = Tree(color(random(0,255), random(0,255), random(0,255)), random(0,100), random(0,100), random(0,8))
myTree3 = Tree(color(random(0,255), random(0,255), random(0,255)), random(0,100), random(0,100), random(0,10))
myTree4 = Tree(color(random(0,255), random(0,255), random(0,255)), random(0,100), random(0,100), random(0,10))

class BgCircle(object):
    
    

    def __init__(self):
        self.c = color(255,0,255)
        self.xpos = 0
        self.ypos = 0
        self.position = [[0,0]]
        
    def mousePosition(self, xpos, ypos):
        self.xpos = mouseX;
        self.ypos = mouseY;
         

        
    def display(self):
        self.position.append([self.xpos,self.ypos])
        stroke(0)
        fill(self.c)
        for i in self.position:            
            ellipse( i[0], i[1], 55, 55)
        
bg = BgCircle();

class ShapeShifter(object):
    def __init__(self, c, xpos, ypos,):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
      
    def changeshape(self, c, xpos, ypos):
        stroke(0)
        fill(self.c)
        ellipse( self.xpos, self.ypos, 55, 55)        



newshape = ShapeShifter()

    
def setup():
    size(200,200)
    

def draw(): 
  background(255)
  myCar1.drive()
  myCar1.display()
  myCar2.drive()
  myCar2.display()
  myTree1.drive()
  myTree1.display()
  myTree2.drive()
  myTree2.display()
  myTree3.drive()
  myTree3.display()
  bg.display()
  
  if (mousePressed == True):
      bg.mousePosition(mouseX,mouseY)

    
     
def keyPressed():
    if( key == ' '):
         myCar1.setcolor( color(random(255), random(255), random(255)) )
         myCar2.setcolor( color(random(255), random(255), random(255)) )



  

  
