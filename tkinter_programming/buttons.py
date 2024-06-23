from tkinter import *

# Create the root widget 
root = Tk()

# Action to do when button clicked
def myClick():
    myLabel = Label(root, text='Hi Yupindra!')
    myLabel.pack()

# Create button widget and put it onto the screen
myButton = Button(root, text='Click Me!', padx=50, pady=5, command=myClick, fg='White', bg='Black') # color code hex alos valid
myButton.pack()

# run the main loop of the GUI
root.mainloop()