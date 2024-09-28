# Import modules for Pomodoro Timer
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from playsound import playsound
import time


class Pomodoro:
    def __init__(self, root):
        self.root = root

    def work_break(self, timer):
        # Common block to dsiplay min/sec on GUI
        minutes, seconds = divmod(timer, 60)
        self.min.set(f"{minutes:02d}")
        self.sec.set(f"{seconds:02d}")
        self.root.update()
        time.sleep(1)

    def work(self):
        timer = 25 * 60
        while timer >= 0:
            pomo.work_break(timer)
            if timer == 0:
                # Once a work is done play a sound
                # and switch to break
                playsound("sound.ogg")
                messagebox.showinfo(
                    "Good Job", "Take A break, \
                     nClick Break Button"
                )
            timer -= 1

    def break_(self):
        timer = 5 * 60
        while timer >= 0:
            pomo.work_break(timer)
            if timer == 0:
                # Once a break is done
                # Switch back to work
                playsound("sound.ogg")
                messagebox.showinfo(
                    "Time Up", "Get Back To Work, \
                    nclick Work Button"
                )
            timer -= 1

    def main(self):

        # GUI Window configuration
        self.root.title("Pomodoro Timer")
        self.root.geometry("450x455")
        self.root.resizable(False, False)

        # Label
        self.min = tk.StringVar(self.root)
        self.min.set("25")
        self.sec = tk.StringVar(self.root)
        self.sec.set("00")

        self.min_label = tk.Label(self.root, textvariable=self.min, font=(
            "arial", 22, "bold"), bg="red", fg="black")
        self.min_label.pack()

        self.sec_label = tk.Label(self.root, textvariable=self.sec, font=(
            "arial", 22, "bold"), bg="red", fg="black")
        self.sec_label.pack()
        
        # Add backgound image for GUI using canvas widget
        canvas = tk.Canvas(self.root)
        canvas.pack(expand=True, fill="both")
        img = Image.open("pomodoro.jpg")
        bg = ImageTk.PhotoImage(img)
        canvas.create_image(90, 10, image=bg, anchor="nw")

        # Create two buttons with countdown function command
        btn_work = tk.Button(self.root, text="Start", bd=5, command=self.work, 
                            bg="red", font=(
                            "arial", 15, "bold")).place(x=140, y=380)

        btn_break = tk.Button(self.root, text="Break", bd=5, command=self.break_,
                              bg="red", font=(
                                  "arial", 15, "bold")).place(x=240, y=380)
                              
        self.root.mainloop()

# Initialization of main
if __name__ == '__main__':
    pomo = Pomodoro(tk.Tk())
    pomo.main()