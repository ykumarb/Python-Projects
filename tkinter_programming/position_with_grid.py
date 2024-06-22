# Import all things from the tkinter library 
from tkinter import *

# Create a root widget
root = Tk()

# Create label widgets upon the root widget
myLabel1 = Label(root, text='Hello World')
myLabel2 = Label(root, text='My name is Yupindra!')

# Place all the label widgets in the grid system
# By default, the grid system will not resize the contents unlike pack system
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

# Run the mainloop
root.mainloop()