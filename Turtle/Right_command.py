# INSTRUCTIONS FOR RIGHT

from Turtle_engine import Turtle
# called by the command parser for right operation

class rightcmd:
    def __init__(self,angle=90):
        self.angle=angle
        
    def execute(self,Turtle:Turtle):
        Turtle.right()  # which then calls the right function in Turtle class