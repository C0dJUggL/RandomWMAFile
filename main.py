import os
import random
import tkinter as tk
import vlc


# Function to play a random wma file
def play_random_file():
    global current_file, current_player, is_paused

    # Stop the current playback if there is any
    if current_player is not None:
        current_player.stop()

    # Select a random file that hasn't been played yet
    available_files = [f for f in wma_files if f not in played_files]

    if not available_files:  # If all files have been played, reset the list
        played_files.clear()
        available_files = wma_files

    current_file = random.choice(available_files)
    file_path = os.path.join(directory, current_file)

    # Create a new player and play the file
    current_player = vlc.MediaPlayer(file_path)
    current_player.play()

    # Update the list of played files
    played_files.append(current_file)

    # Update the state of the pause/play button
    is_paused = False
    update_play_pause_button()


# Function to display the name of the current file
def show_current_file():
    if current_file:
        file_label.config(text=f"Now playing: {current_file}")
    else:
        file_label.config(text="No file is being played")


# Function to toggle between pause and play
def toggle_pause_play():
    global is_paused

    if current_player is not None:
        if is_paused:
            current_player.play()
            is_paused = False
        else:
            current_player.pause()
            is_paused = True
        update_play_pause_button()


# Update the text on the pause/play button
def update_play_pause_button():
    if is_paused:
        play_pause_button.config(text="Resume")
    else:
        play_pause_button.config(text="Pause")


# Function to restart the current track
def restart_track():
    if current_player is not None:
        current_player.stop()
        current_player.play()


# Directory with wma files
directory = 'D:/shuman'  # Specify the path to your directory

# Get the list of all wma files in the directory
wma_files = [f for f in os.listdir(directory) if f.endswith('.wma')]

# Variables to store the current player, file, and pause state
current_player = None
current_file = None
is_paused = False
played_files = []  # List of already played files

# Create the graphical interface
root = tk.Tk()
root.title("Random WMA Player")
root.geometry("300x350")  # Window size
root.configure(bg="#282c34")  # Background color of the window

# Window header
header_frame = tk.Frame(root, bg="#44475a", pady=10)
header_frame.pack(fill="x")

header_label = tk.Label(header_frame, text="Random WMA Player", bg="#44475a", fg="#f8f8f2",
                        font=("Helvetica", 16, "bold"))
header_label.pack()

# Use a frame for the buttons
button_frame = tk.Frame(root, padx=10, pady=10, bg="#282c34")
button_frame.pack(expand=True)


# Create buttons with specified colors
def create_button(parent, text, command, bg_color, fg_color):
    button = tk.Button(parent, text=text, command=command, width=20, height=2,
                       bg=bg_color, fg=fg_color, font=("Helvetica", 12, "bold"))
    button.pack(pady=5)
    return button


# Add buttons
play_button = create_button(button_frame, "Play Random File", play_random_file, "#50fa7b", "#282c34")
play_pause_button = create_button(button_frame, "Pause", toggle_pause_play, "#ffb86c", "#282c34")
restart_button = create_button(button_frame, "Restart", restart_track, "#ff5555", "#282c34")
show_file_button = create_button(button_frame, "Show Current File", show_current_file, "#8be9fd", "#282c34")

# Label to display the file name
file_label = tk.Label(root, text="No file is being played", bg="#282c34", fg="#ffffff", pady=10,
                      font=("Helvetica", 12))
file_label.pack()

# Start the main application loop
root.mainloop()
