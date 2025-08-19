#CONTROLLER

import tkinter as tk
from canvas import TKpanel
from pen import Pen
from command_parser import Commandparser
from Turtle_engine import Turtle


class App:
    def __init__(self):
        self.root = tk.Tk()     # Main application window where all the widgets appear
        self.root.title("Behroz's Canvas")
        self.canvas = TKpanel(self.root)
        self.canvas.pack()


    def run(self):

        #-- Turtle engine --

        str_comm="+FF-F-F-F+F+F"
        # str_comm="F+F-F" 
        # str_comm="F+F+F+F"
        
        pen = Pen(self.canvas)
        turtle = Turtle(pen)
        Parser=Commandparser(str_comm)
        Parser.execute(turtle)

        print("\nThe App is running sucessfully.")
        self.root.mainloop() # Starts the event loop and keep the app running until the user ends it
        
        
        
        # str_comm="F-F-F-F"
        # pen1= Pen(self.canvas)
        # pen1.move_to()
        # turtle1 = Turtle(pen)
        # Parser=Commandparser(str_comm)
        # # parser = CommandParser(str_comm)
        # Parser.execute(turtle1)


        

       
       
       



