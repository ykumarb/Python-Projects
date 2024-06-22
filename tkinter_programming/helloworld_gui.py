from tkinter import *

# Tkinter is all full of widgets - label, text, frame, buton etc..,

# Create a root widegt
root = Tk()

# Create a label widget
myLabel = Label(root, text='Hello World')

# Pack a Label widget i.e shoving it on the screen
myLabel.pack()

# Run a main loop on the root widget
root.mainloop()