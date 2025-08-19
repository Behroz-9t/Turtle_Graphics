# DRAWS

from point import Point
import math

class Pen:

    def __init__(self,canvas,angle=0):

        self._canvas=canvas # stores canvas in _canvas 
        self._cp=Point(150,150) # obj created and gave value to Point where x and y are initially centered to x=150 , y=150
        self._angle=angle


    def forward(self, cd): #here the command is comming from the Turtle class forward

        """Move forward in current direction, drawing a line."""
        rad = math.radians(self._angle)
        new_x = self._cp.get_x + cd * math.cos(rad)
        new_y = self._cp.get_y + cd * math.sin(rad)
        new_point = Point(new_x, new_y)
        self._canvas.add_line(self._cp, new_point)
        # self.move_to(new_x,new_y)
        self._cp = new_point

    def turn_left(self,angle=90): #-----------QQ: but why is there formula for forward and not for left or right ??--------
        self._angle-=angle

    def turn_right(self,angle=90):
        self._angle+=angle


    def get_position(self):
       
        return self._cp # returns the value of new _cp

