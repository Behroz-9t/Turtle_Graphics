# INSTRUCTIONS FOR FORWARD

from Turtle_engine import Turtle
# called by the command parser for forward operation

class forwardcmd:
    def __init__(self,cd=100):
        self.cd=cd
        
    def execute(self,Turtle:Turtle):
        Turtle.forward() # which then calls the forward function in Turtle class

