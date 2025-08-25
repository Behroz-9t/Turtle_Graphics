# INSTRUCTIONS FOR LEFT

from Turtle_engine import Turtle
# called by the command parser for left operation

class leftcmd:
    def __init__(self,angle=90):
        self.angle=angle

    def execute(self,Turtle:Turtle):
        Turtle.left()  # which then calls the left function in Turtle class 