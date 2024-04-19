import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# List of music file paths
music_files = [
    "./macan1.mp3",
    "./macan2.mp3",
    "./macan3.mp3",
    # Add the path to more music files if you have them
]

# Current track index
current_track_index = 0

# Load the first track
pygame.mixer.music.load(music_files[current_track_index])

# Play the music
pygame.mixer.music.play(-1)  # -1 means loop the song indefinitely

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PLAY or event.key == pygame.K_SPACE:
                # Play or unpause the music
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.play()
            elif event.key == pygame.K_STOP:
                # Stop the music
                pygame.mixer.music.stop()
            elif event.key == pygame.K_NEXT:
                # Play the next track
                current_track_index = (current_track_index + 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track_index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_PREVIOUS:
                # Play the previous track
                current_track_index = (current_track_index - 1) % len(music_files)
                pygame.mixer.music.load(music_files[current_track_index])
                pygame.mixer.music.play()

pygame.quit()
