# 🐢 Turtle Drawing with OOP and Tkinter  

This project implements a **command-driven turtle graphics system** using **Object-Oriented Programming (OOP)** principles and the **Tkinter** library in Python.  

It is inspired by **Logo Turtle Graphics** and allows drawing patterns using simple string commands such as:  

- `F+F+F+F` → draws a **square**  
- `F-F+F-F` → draws a **zigzag**  

---

## ✨ Features  

- ✅ **OOP Design** – Classes like `pen`, `point`, `line`, `canvas`, `Turtle_engine`, `Commands`, and `command_parser`  
- ✅ **Command Pattern** – Each action (Forward, Left, Right) is encapsulated as a separate command class  
- ✅ **Separation of Concerns** – Input parsing, command execution, and drawing logic are fully decoupled  
- ✅ **Tkinter Drawing** – Shapes are displayed in a live Tkinter canvas window   

---

## 🏗 Project Structure  

```
📂 turtle-oop-tkinter
│── main.py              # Entry point (launcher)
│── app.py               # controller
│── canvas.py            # Tkinter canvas wrapper(Like paper)
│── pen.py               # Pen class (Draws)
│── Turtle_engine.py     # Turtle class (wraps Pen)
│── point.py             # Represents a 2D coordinate
│── line.py              # Represents a line segment
│── Forward_command.py   # For forward command
│── Right_command.py     # For right command
│── Left_command.py      # For left command
│── command_parser.py    # Parses input strings into command objects

```

---

### Example Input 

```python
command_str = "F+F+F+F"
```
➡ Draws a **square** in a Tkinter window  

---

## 🔧 Example Commands  

- `F+F+F+F` → Square  
- `F-F+F-F` → Zigzag  
- `+FF-F-F-F+F+F` → Custom path  

---

## 🧠 Concepts Applied  

- **Encapsulation** – Pen hides its position/angle logic  
- **Composition** – Turtle uses Pen, Canvas holds Lines  
- **Abstraction** – Command base class enforces consistent interface  
- **Command Pattern** – Each action is a command object  
- **Single Responsibility** – Each class has one job  

---

## 👨‍💻 Author  

Developed by Behroz Musharraf as part of **CS 332: Object-Oriented Programming** (University of Karachi).  

