class Point:
    def __init__(self,x=0,y=0):
        self._x =x
        self._y =y

# More Pythonic version of getter and setter

    @property #--> getter of x
    def get_x(self):
        return self._x
    
    @get_x.setter #--> setter of x
    def set_x(self,value):
        self._x=value
    
    @property#--> getter of y
    def get_y(self):
        return self._y
    
    @get_y.setter#--> setter of y
    def set_y(self,value):
        self._y=value


    # This function is to basically check the point type of the addition operands

    def __add__(self,other): # --> dunder func/method to add two point type objects
        if isinstance(other,Point): #--> isinstance returns boolean value and checks "other" input of type "point"
            return (self._x+other._x,self._y+other._y)
        else:
            raise TypeError("Can only add point to point type!")
        
   

    def __str__(self):
        return (f"(x:{self._x} , y:{self._y})")
    
    def __eq__(self, other): # Dunder method for the equality check. Without this the complier always compairs the (memory address) and even though the answer will be true it will return false.
        return isinstance(other,Point) and self._x==other._x and self._y==other._y
    
    def distance(self, p): # Distance Formula for dist between self.x and self.y and anpther point p
        return ((self._x - p._x)**2 + (self._y - p._y)**2)**0.5


#---Testing point class-----

# P=Point(2,3) # object p with value of x = 2 and y = 3
# Q=Point(5,9)# object Q with value of x = 5 and y = 9
# S=Point(2,3)
# R=P+Q        # R object to hold the addition of P and Q
# print(R)     # prints R --> Output: (7,12)
# print(P==S)  # returns true
# print(P.distance(Q))  # calcs dist b/w (p._x ,p._y)and (Q._x and Q._y)

# print(P.get_x)
# print(P.get_y)




          

          