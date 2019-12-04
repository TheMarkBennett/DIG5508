## Spot the difference game

class spotItem(object):
    def __init__(self,level,answers):
        self.level = level
        self.answers = answers
        self.numobjects = len(answers)
        self.found = 9
        
    def instructions(self):
        ## instructions
        textAlign(CENTER)
        fill(50)
        t = "Spot the Difference"
                
        if(self.found == 0):
            fill(255,0,0)
            s = "Congratulations You Found the Differences"
        else: 
             s = "Find the " + str(self.found) + " Differences"
             
        
        textSize(48)
        text(t, 0, 550, width, 200)
        textSize(24)
        text(s, 0, 610, width, 200) 
        
        
    def drawAnswer(self):
        
        ## loop through all the answers and show correct answers
        for item in self.answers:         
            
            if(item[4] == True):
                fill(207, 0, 15, 0)
                strokeWeight(5) 
                stroke(0)
                rect(item[0],item[1],item[2],item[3])
                

    
    def clicked(self):
        # loop through all the answers to is if it has been clicked and if it has show it
        for n,i in enumerate(self.answers):
            #I trield using elipse but it was to hard to get the radius for click
            x = i[0]
            y = i[1]
            w = i[2]
            h = i[3]
            
            if (mouseX > x and mouseX < (x + w) and mouseY > y and mouseY < (y + h)):
                #if click on the object set it to true
                if(self.answers[n][4] == False):
                    self.answers[n][4] = True
                    
  
                
    #calculate the found answers                                         
    def answerCounter(self):
       num = self.numobjects
       t = 0
       
       for n,i in enumerate(self.answers):
           if(self.answers[n][4] == True):
               #print(self.answers[n][4])
               t += 1
       
       self.found = (num - t)

      
        
             

               

         
         
         
         
##level 1 answers
level1answers = [
                 [1220,20,55,55,False], ##spider web
                 [1510,95,60,70,False], #picture frame
                 [1485,250,65,20,False], #lampshade
                 [1125,230,40,60,False], #cup on desk
                 [1180,335,35,100,False], #leg of chair
                 [950,485,60,30,False], #spill
                 [1440,315,105,35,False], #Book
                 [850,365,90,100,False], #side table
                 [1270,420,75,30,False] #pencils
                 ]                      



def setup():
    global orginalImg, editedImg
    size(1610,650)
    orginalImg = loadImage("image_01_1.png")
    editedImg = loadImage("image_02_1.png")


myDifference1 = spotItem(1,level1answers)
    
def draw():
  background(255)
  image(orginalImg,0,0,800,534)
  image(editedImg,810,0,800,534)
  ##Canvas.menu()
  myDifference1.instructions()
  myDifference1.drawAnswer()

  
  
def mousePressed():  
    myDifference1.clicked()
    myDifference1.answerCounter()
    

    
