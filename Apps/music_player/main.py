from tkinter import filedialog
from tkinter import *
import pygame
import os

root = Tk()
root.title('Music Player')
root.geometry("500x300")

pygame.mixer.init()

songs = []
current_song = ""
paused = False

def load_music():
    global current_song
    root.directory = filedialog.askdirectory()
    try:
        for song in os.listdir(root.directory):
            name, ext = os.path.splitext(song)
            if ext == '.mp3':
                songs.append(song)

        for song in songs:
            songList.insert("end", song)
        songList.selection_set(0)

        current_song = songs[songList.curselection()[0]]
    except:
        print("No Directory selected to load music!!!")
        pass

def play_music():
    global current_song, paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global current_song, paused

    try:
        songList.selection_clear(0, END)
        songList.selection_set(songs.index(current_song) + 1)
        current_song = songs[songList.curselection()[0]]
        play_music()
    except:
        pass

def prev_music():
    global current_song, paused

    try:
        songList.selection_clear(0, END)
        songList.selection_set(songs.index(current_song) - 1)
        current_song = songs[songList.curselection()[0]]
        play_music()
    except:
        pass

menuBar = Menu(root)
root.config(menu=menuBar)

organiseMenu = Menu(menuBar, tearoff=False)
organiseMenu.add_command(label='Select Folder', command=load_music)
menuBar.add_cascade(label='Organise', menu=organiseMenu) 

songList = Listbox(root, bg="Black", fg="White", width=100, height=15)
songList.pack()

playBtnImage = PhotoImage(file='play.png')
pauseBtnImage = PhotoImage(file='pause.png')
nextBtnImage = PhotoImage(file='next.png')
prevBtnImage = PhotoImage(file='previous.png')

control_frame = Frame(root)
control_frame.pack()

playBtn = Button(control_frame, image=playBtnImage, borderwidth=0, command=play_music)
pauseBtn = Button(control_frame, image=pauseBtnImage, borderwidth=0, command=pause_music)
nextBtn = Button(control_frame, image=nextBtnImage, borderwidth=0, command=next_music)
prevBtn = Button(control_frame, image=prevBtnImage, borderwidth=0, command=prev_music)

playBtn.grid(row=0, column=1, padx=7, pady=10)
pauseBtn.grid(row=0, column=2, padx=7, pady=10)
nextBtn.grid(row=0, column=3, padx=7, pady=10)
prevBtn.grid(row=0, column=0, padx=7, pady=10)


root.mainloop()
