# Even though there are multiple objects, we still only need one class. 
# No matter how many cookies we make, only one cookie cutter is needed.
class Tree(object):
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
        rect(random(width), random(height), 20, 10);
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0
                
              
    

    
    
myTree1 = Tree(color(255, 0, 0), 0, 100, 2)
myTree2 = Tree(color(0, 255, 255), 0, 10, 1)
myTree3 = Tree(color(85, 100, 255), 0, 10, 1)
myTree4 = Tree(color(30, 255, 150), 0, 10, 1)
    
def setup():
    size(200,200)

def draw(): 
  background(255)
  ##myCar1.drive()
  myTree1.display()
  ##myCar2.drive()
  myTree2.display()
  myTree3.display()
  myTree4.display()
  
  
