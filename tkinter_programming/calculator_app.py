from tkinter import *

root = Tk()
root.title('Simple Calculator')

entry = Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def clickMe(number):
    prev = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(prev) + str(number))

def clickAdd():
    global fNum, operation
    firstNumber = entry.get()
    fNum = firstNumber
    entry.delete(0, END)
    operation = "add"

def clickSub():
    global fNum, operation
    firstNumber = entry.get()
    fNum = firstNumber
    entry.delete(0, END)
    operation = "Sub"

def clickMul():
    global fNum, operation
    firstNumber = entry.get()
    fNum = firstNumber
    entry.delete(0, END)
    operation = "Mul"

def clickDiv():
    global fNum, operation
    firstNumber = entry.get()
    fNum = firstNumber
    entry.delete(0, END)
    operation = "Div"

def clickEqual():
    global operation
    secondNumber = entry.get()
    entry.delete(0, END)
    try:
        if operation == 'add':
            result = int(fNum) + int(secondNumber)
        elif operation == 'Sub':
            result = int(fNum) - int(secondNumber)
        elif operation == 'Mul':
            result = int(fNum) * int(secondNumber)
        elif operation == 'Div':
            result = int(fNum) / int(secondNumber)
    except:
        print("Something broken. fix it!")

    entry.insert(0, str(result))

def clickClear():
    entry.delete(0, END)

myButton1 = Button(root, text='1', padx=40, pady=20, command=lambda: clickMe(1))
myButton2 = Button(root, text='2', padx=40, pady=20, command=lambda: clickMe(2))
myButton3 = Button(root, text='3', padx=40, pady=20, command=lambda: clickMe(3))
myButton4 = Button(root, text='4', padx=40, pady=20, command=lambda: clickMe(4))
myButton5 = Button(root, text='5', padx=40, pady=20, command=lambda: clickMe(5))
myButton6 = Button(root, text='6', padx=40, pady=20, command=lambda: clickMe(6))
myButton7 = Button(root, text='7', padx=40, pady=20, command=lambda: clickMe(7))
myButton8 = Button(root, text='8', padx=40, pady=20, command=lambda: clickMe(8))
myButton9 = Button(root, text='9', padx=40, pady=20, command=lambda: clickMe(9))
myButton0 = Button(root, text='0', padx=40, pady=20, command=lambda: clickMe(0))
myButtonAdd = Button(root, text='+', padx=39, pady=20, command=clickAdd)
myButtonEqual = Button(root, text='=', padx=91, pady=20, command=clickEqual)
myButtonClear = Button(root, text='Clear', padx=79, pady=20, command=clickClear)

myButtonSub = Button(root, text='-', padx=41, pady=20, command=clickSub)
myButtonMul = Button(root, text='*', padx=40, pady=20, command=clickMul)
myButtonDiv = Button(root, text='/', padx=41, pady=20, command=clickDiv)


myButton1.grid(row=3, column=0)
myButton2.grid(row=3, column=1)
myButton3.grid(row=3, column=2)
myButton4.grid(row=2, column=0)
myButton5.grid(row=2, column=1)
myButton6.grid(row=2, column=2)
myButton7.grid(row=1, column=0)
myButton8.grid(row=1, column=1)
myButton9.grid(row=1, column=2)

myButton0.grid(row=4, column=0)
myButtonAdd.grid(row=5, column=0)
myButtonEqual.grid(row=5, column=1, columnspan=2)  
myButtonClear.grid(row=4, column=1, columnspan=2)

myButtonSub.grid(row=6, column=0)
myButtonMul.grid(row=6, column=1)
myButtonDiv.grid(row=6, column=2)

root.mainloop()