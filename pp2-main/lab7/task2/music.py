import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the display (not needed for a music player, but required for event handling)
pygame.display.set_mode((200, 200))

# List of music file paths
music_files = [
    "./macan1.mp3",
    "./macan2.mp3",
    "./macan3.mp3",
    # Add more music files if you have them
]

# Current track index
current_track_index = 0

# Load the first track
pygame.mixer.music.load(music_files[current_track_index])

# Music control functions
def play():
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track_index])
    pygame.mixer.music.play()

def previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track_index])
    pygame.mixer.music.play()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop()
                else:
                    play()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_p:
                previous_track()
            elif event.key == pygame.K_q:
                running = False  # Quit the program if 'q' is pressed

pygame.quit()
