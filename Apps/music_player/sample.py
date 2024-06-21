
from tkinter import filedialog
from tkinter import *
import pygame
import os

# Initialize TK
root = Tk()
root.title('Music Player')
root.geometry("500x300")

# Init the pygame mixer
pygame.mixer.init()


# Globals for songs related
currentSong = ""
paused = False
songs = []

# Helper to load the music from local storage to List box in the 
# Music player App
def loadMusic():
    global currentSong, paused
    root.directory = filedialog.askdirectory()
    try:    
        for song in os.listdir(root.directory):
            name, ext = os.path.splitext(song)
            if ext == '.mp3':
                songs.append(song)
        for song in songs:
            songList.insert('end', song)
        
        songList.selection_set(0)
        currentSong = songs[songList.curselection()[0]]
    except:
        pass

# Helper to play the current song in the list
def playMusic():
    global currentSong, paused
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, currentSong))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

# Helper to pause the current song from the list
def pauseMusic():
    global currentSong, paused
    pygame.mixer.music.pause()
    paused = True
    
# Helper to play the prev song from the list
def prevMusic():
    global currentSong, paused
    try:
        songList.selection_clear(0, END)
        songList.selection_set(songs.index(currentSong) - 1)
        currentSong = songs[songList.curselection()[0]]
        playMusic()
    except:
        pass

# Helper to play the next song from the list
def nextMusic():
    try:
        songList.selection_clear(0, END)
        songList.selection_set(songs.index(currentSong) + 1)
        currentSong = songs[songList.curselection()[0]]
        playMusic()
    except:
        pass

# Create a menu bar to fill in the songList in Listbox region
menuBar = Menu(root)
root.config(menu=menuBar)

organiseMenu = Menu(menuBar, tearoff=False)
organiseMenu.add_command(label='Select Folder', command=loadMusic)
menuBar.add_cascade(label='Organise', menu=organiseMenu)

# Create a song list box
songList = Listbox(root, bg='Black', fg='White', width=100, height=15)
songList.pack()

# Create section and add music buttons
controlFrame = Frame(root)
controlFrame.pack()

# Get the button images fro local
playBtnImage = PhotoImage(file='play.png')
pauseBtnImage = PhotoImage(file='pause.png')
prevBtnImage = PhotoImage(file='previous.png')
nextBtnImage = PhotoImage(file='next.png')

# Create button to add to the section
playBtn = Button(controlFrame, image=playBtnImage, borderwidth=0, command=playMusic)
pauseBtn = Button(controlFrame, image=pauseBtnImage, borderwidth=0, command=pauseMusic)
prevBtn = Button(controlFrame, image=prevBtnImage, borderwidth=0, command=prevMusic)
nextBtn = Button(controlFrame, image=nextBtnImage, borderwidth=0, command=nextMusic)

# Add all these buttons to the control frame in a gri fashion
playBtn.grid(row=0, column=1, padx=7, pady=10)
pauseBtn.grid(row=0, column=2, padx=7, pady=10)
prevBtn.grid(row=0, column=0, padx=7, pady=10)
nextBtn.grid(row=0, column=3, padx=7, pady=10)


# Init the main loop
root.mainloop()