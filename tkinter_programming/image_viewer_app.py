from tkinter import *
from PIL import ImageTk, Image

root = Tk()

myImage1 = ImageTk.PhotoImage(Image.open('images/photo1.jpg'))
myImage2 = ImageTk.PhotoImage(Image.open('images/photo2.jpg'))
myImage3 = ImageTk.PhotoImage(Image.open('images/photo3.jpg'))
myImage4 = ImageTk.PhotoImage(Image.open('images/photo4.jpg'))
myImage5 = ImageTk.PhotoImage(Image.open('images/photo6.jpg'))

myList = [myImage1, myImage2, myImage3, myImage4, myImage5]

status = Label(root, text='Image 1 of '+ str(len(myList)), bd=1, relief=SUNKEN, anchor=E)
myLabel = Label(image=myImage1)
myLabel.grid(row=0, column=0, columnspan=3)

def clickBck(ImageNumber):
    global myLabel, bckButton, fwdButton
    myLabel.grid_forget()

    myLabel = Label(image=myList[ImageNumber-1])
    myLabel.grid(row=0, column=0, columnspan=3)

    fwdButton = Button(root, text='>>', borderwidth=3, command=lambda: clickFwd(ImageNumber+1))
    bckButton = Button(root, text='<<', borderwidth=3, command=lambda: clickBck(ImageNumber-1))

    if ImageNumber == 1:
        bckButton = Button(root, text='<<', borderwidth=3, state=DISABLED)
    
    bckButton.grid(row=1, column=0) 
    fwdButton.grid(row=1, column=2)

    status = Label(root, text="Image " + str(ImageNumber) + " of" + str(len(myList)), relief=SUNKEN, bd=1, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def clickFwd(ImageNumber):
    
    global myLabel, bckButton, fwdButton
    myLabel.grid_forget()

    myLabel = Label(image=myList[ImageNumber-1])
    myLabel.grid(row=0, column=0, columnspan=3)

    fwdButton = Button(root, text='>>', borderwidth=3, command=lambda: clickFwd(ImageNumber+1))
    bckButton = Button(root, text='<<', borderwidth=3, command=lambda: clickBck(ImageNumber-1))

    if ImageNumber == 5:
        fwdButton = Button(root, text='>>', borderwidth=3, state=DISABLED)
    
    bckButton.grid(row=1, column=0) 
    fwdButton.grid(row=1, column=2)

    status = Label(root, text="Image " + str(ImageNumber) + " of" + str(len(myList)), relief=SUNKEN, bd=1, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

bckButton = Button(root, text='<<', borderwidth=3, command=clickBck, state=DISABLED)
fwdButton = Button(root, text='>>', borderwidth=3, command=lambda:clickFwd(2))
exitButton = Button(root, text='Exit Program', borderwidth=3, command=root.quit)

bckButton.grid(row=1, column=0) 
fwdButton.grid(row=1, column=2)
exitButton.grid(row=1, column=1)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
root.mainloop()