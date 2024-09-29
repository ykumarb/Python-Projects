import tkinter as tk
from tkinter import messagebox, Scrollbar, Frame
from pytube import Search
import webbrowser
import speech_recognition as sr
from PIL import Image, ImageTk  # Import Pillow for image handling
import pyttsx3
import threading
import time
import os

# Global variable to store the current video URL
current_video_url = None

# Load and resize the microphone image
def load_and_resize_icon(file_path, size):
    original_image = Image.open(file_path)  # Load the original image
    resized_image = original_image.resize(size, Image.Resampling.LANCZOS)  # Resize the image
    return ImageTk.PhotoImage(resized_image)  # Convert to PhotoImage for Tkinter

# Set the desired size for the microphone icon
icon_size = (40, 40)  # Adjust the size as needed

# Function to search YouTube videos
def search_youtube(query):
    s = Search(query)
    results = s.results
    if results:
        return [(video.title, video.watch_url) for video in results[:45]]  # Return top 5 results
    else:
        return []

# Function to play selected video in web browser
def play_video(url):
    global current_video_url
    current_video_url = url
    webbrowser.open(url)

# Function to pause video
def pause_video():
    if current_video_url:
        webbrowser.open("https://www.youtube.com/pause")  # YouTube doesn't have a direct pause URL; this is illustrative.

# Function to stop the video
def stop_video():
    if current_video_url:
        webbrowser.open("https://www.youtube.com/stop")  # YouTube doesn't have a direct stop URL; this is illustrative.

# Function triggered when the search button is clicked
def search_and_display():
    query = search_entry.get()
    if not query:
        messagebox.showerror("Input Error", "Please enter a search query.")
        return

    # Clear previous results in frame
    for widget in video_list_frame.winfo_children():
        widget.destroy()

    # Search and display results
    videos = search_youtube(query)

    if videos:
        for idx, (title, url) in enumerate(videos):
            video_button = tk.Button(video_list_frame, text=title, command=lambda u=url: play_video(u),
                                     bg="#4285F4", fg="white", font=("Helvetica", 12), relief="flat")
            video_button.pack(padx=5, pady=5, fill='x')

    else:
        messagebox.showinfo("No Results", "No videos found for the query.")

def speak(prompt_text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(prompt_text)
    engine.runAndWait()

# Initalize the recognizer and microphone once at the beginning
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Preconfigure the microphone settings at app start (calibrate for ambient noise)
with microphone as source:
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
def recognize_speech():
    # Re-use the pre-initialized microphone
    with microphone as source:
        # Speak a prompt asking the user to say a search query
        speak("Listening. Please say your query now")
        # print("Listening. Please say your query now")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            search_entry.delete(0, tk.END)
            search_entry.insert(0, query)
            search_and_display()
        except sr.UnknownValueError:
            messagebox.showerror("Recognition Error", "Could not understand audio.")
        except sr.RequestError as e:
            messagebox.showerror("API Error", "Could not request results from Google Speech Recognition service.")

# Initialize the GUI
root = tk.Tk()
root.title("YouTube Video Search")
root.geometry("500x500")
root.configure(bg="#F9F9F9")

# Maximize the window
root.state('zoomed') # This maximizes the window

# Title Label
title_label = tk.Label(root, text="YouTube Video Search", bg="#F9F9F9", font=("Helvetica", 18, "bold"))
title_label.pack(pady=20)

# Input field for search
search_label = tk.Label(root, text="Enter video search query:", bg="#F9F9F9", font=("Helvetica", 12))
search_label.pack(pady=10)

search_entry = tk.Entry(root, width=50, font=("Helvetica", 12), borderwidth=2, relief="groove")
search_entry.pack(pady=10)

# Search button
search_button = tk.Button(root, text="Search", command=search_and_display, bg="#DB4437", fg="white", font=("Helvetica", 12))
search_button.pack(pady=10)

# Replace the search button with a microphone icon
microphone_icon = load_and_resize_icon("microphone1.png", icon_size)  # Load the resized microphone image
voice_icon_button = tk.Label(root, image=microphone_icon, bg="#F9F9F9")  # Create a Label with the icon
voice_icon_button.pack(pady=10)


# Bind click event on the microphone icon to trigger speech recognition
voice_icon_button.bind("<Button-1>", lambda event: recognize_speech())

# Control buttons
control_frame = tk.Frame(root, bg="#F9F9F9")
control_frame.pack(pady=10)

# Play button (Green)
play_button = tk.Button(control_frame, text="Play", command=lambda: play_video(current_video_url),
                        bg="#34A853", fg="white", font=("Helvetica", 12), relief="raised")  # Green color
play_button.pack(side='left', padx=5)

# Pause button (Orange)
pause_button = tk.Button(control_frame, text="Pause", command=lambda: pause_video(),
                         bg="#FFA500", fg="white", font=("Helvetica", 12), relief="raised")  # Orange color
pause_button.pack(side='left', padx=5)

# Stop button (Red)
stop_button = tk.Button(control_frame, text="Stop", command=lambda: stop_video(),
                        bg="#DB4437", fg="white", font=("Helvetica", 12), relief="raised")  # Red color
stop_button.pack(side='left', padx=5)

# Display results in Canvas with Scrollbar
result_frame = tk.Frame(root, bg="#F9F9F9")
result_frame.pack(pady=10, fill='both', expand=True)

canvas = tk.Canvas(result_frame)
scrollbar = Scrollbar(result_frame, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="right", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

video_list_frame = scrollable_frame  # Renamed for clarity

# Start the tkinter app
root.mainloop()
