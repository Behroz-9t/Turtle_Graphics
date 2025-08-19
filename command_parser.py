#PARSES COMMANDS

from Forward_command import forwardcmd
from Right_command import rightcmd
from Left_command import leftcmd

class Commandparser:
    def __init__(self,str_comm:str):
        self.str_comm=str_comm # str_comm for storing the F+F+F+Fmlike stirng command

    def parser(self):

        commands = [] # list in which commands calling will be added for respective commands

        for ch in self.str_comm:
            if "F" in ch:
                commands.append(forwardcmd())
            elif "+" in ch:
                commands.append(rightcmd())
            elif "-" in ch:
                commands.append(leftcmd())
        

        return commands #returns the list of commands sent to str_comm like if "F+F-"  it will be like: [forwardcmd,rightcmd,forw..,leftcmd]
    
    def execute(self,turtle):
        for cmd in self.parser(): # here it access the list returned by the parser and cmd becomes (forwardcmd) then (right) then (forw..) then (left)
            cmd.execute(turtle) # here the command passes like " forwardcmd.execute(turtle) "
            





            