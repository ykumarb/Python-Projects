# Import the requried modules
from tkinter import *
from PIL import ImageTk, Image

# Create a root widget
root = Tk()
root.title('Ironman')
root.iconbitmap('ironman.ico')

# Using images (needs to import - if not gif/pnm or something is supported by tkinter by default)
# For real images like jpg/png etc.., import PIL (Python image library) but it is deprecated
# Pillow is the fork of PIL (referenced as PIL)
# pip install pillow ; pip freeze

myImage = ImageTk.PhotoImage(Image.open("photo.jpg"))
myLabel = Label(image=myImage)
myLabel.pack()

# Create a exit button
quitButton = Button(root, text='Exit Program', command=root.quit)
quitButton.pack()

# Run the main loop
root.mainloop()