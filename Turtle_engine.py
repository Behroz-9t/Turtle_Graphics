#DRAWER USING PEN

from pen import Pen

class Turtle:
    def __init__(self,pen:Pen):
        self.pen = pen
    

    def forward(self,cd=100):
        self.pen.forward(cd) # here from the forwardcmd it reaches the point's forward function which uses formula to draw the line
                             # taking cd as input argument
    
    def left(self,angle=90):
        self.pen.turn_left(angle)  # here from the leftcmd it reaches the point's left function which changes the direction                   
                                   # taking angle as input argument
    
    def right(self,angle=90):
        self.pen.turn_right(angle) # here from the rightcmd it reaches the point's right function which changes the direction                   
                                   # taking angle as input argument

