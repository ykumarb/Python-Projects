from tkinter import filedialog
from tkinter import *
import pygame
import os

# Initialize TK
root = Tk()
root.title('Music Player')
root.iconbitmap('mplayer_icon.ico')
root.geometry("500x310")

# Init the pygame mixer
pygame.mixer.init()

# Globals for songs related
songs = []
current_song = ""
paused = False
from_next = from_prev = False

# Helper to load the music from local storage to List box in the 
# Music player App
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

# Helper to play the current song in the list
def play_music():
    global current_song, paused, from_next, from_prev

    if not paused:
        # print(current_song)
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
        from_prev = from_next = False
        # print("Both prev and next set to False")
    else:
        #print("inside else")
        if from_next is False and from_prev is False:
            # print("inside 1" + " " + current_song)
            pygame.mixer.music.unpause()
            paused = False
        elif ((from_next is True and from_prev is False) or (from_next is False and from_prev is True)):
            # print("inside 2" + " " + current_song)
            pygame.mixer.music.load(os.path.join(root.directory, current_song))
            pygame.mixer_music.play()
            from_next = from_prev = False
            # print("Both prev and next set to False")
        else:
            # This condition not valid real time. Both prev and next can't be pressed at same time.
            #print("Invalid prev/next operation")
            pass

# Helper to pause the current song from the list
def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

# Helper to play the next song from the list
def next_music():
    global current_song, paused, from_next

    try:
        songList.selection_clear(0, END)
        songList.selection_set(songs.index(current_song) + 1)
        current_song = songs[songList.curselection()[0]]
        #print(current_song)
        from_next = True
        #print("next is set to true")
        play_music()
    except:
        pass

# Helper to play the prev song from the list
def prev_music():
    global current_song, paused, from_prev

    try:
        songList.selection_clear(0, END)
        songList.selection_set(songs.index(current_song) - 1)
        current_song = songs[songList.curselection()[0]]
        from_prev = True
        #print("prev is set to true")
        play_music()
    except:
        pass

# Create a menu bar to fill in the songList in Listbox region
menuBar = Menu(root)
root.config(menu=menuBar)

organiseMenu = Menu(menuBar, tearoff=False)
organiseMenu.add_command(label='Select Folder', command=load_music)
menuBar.add_cascade(label='Organise', menu=organiseMenu) 

# Create a song list box
songList = Listbox(root, bg="Black", fg="White", width=100, height=15)
songList.pack()

# Create section and add music buttons
control_frame = Frame(root)
control_frame.pack()

# Get the button images fro local
playBtnImage = PhotoImage(file='play.png')
pauseBtnImage = PhotoImage(file='pause.png')
nextBtnImage = PhotoImage(file='next.png')
prevBtnImage = PhotoImage(file='previous.png')

# Create button to add to the section
playBtn = Button(control_frame, image=playBtnImage, borderwidth=0, command=play_music)
pauseBtn = Button(control_frame, image=pauseBtnImage, borderwidth=0, command=pause_music)
nextBtn = Button(control_frame, image=nextBtnImage, borderwidth=0, command=next_music)
prevBtn = Button(control_frame, image=prevBtnImage, borderwidth=0, command=prev_music)

# Add all these buttons to the control frame in a gri fashion
playBtn.grid(row=0, column=1, padx=7, pady=10)
pauseBtn.grid(row=0, column=2, padx=7, pady=10)
nextBtn.grid(row=0, column=3, padx=7, pady=10)
prevBtn.grid(row=0, column=0, padx=7, pady=10)

# Run the main loop
root.mainloop()
