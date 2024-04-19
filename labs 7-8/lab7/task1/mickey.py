import pygame
import math
from datetime import datetime

# Initialize Pygame and the clock
pygame.init()
clock = pygame.time.Clock()

# Constants for display
WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Load images
mickey_face = pygame.image.load('mickey.png').convert_alpha()
mickey_face = pygame.transform.scale(mickey_face, (WIDTH, HEIGHT))
left_arm = pygame.image.load('leftarm.png').convert_alpha()
right_arm = pygame.image.load('rightarm.png').convert_alpha()

# Define pivot points for the arms relative to the center of the clock
HOUR_HAND_PIVOT = (CENTER[0] - 10, CENTER[1] + 10)  # Example values, adjust as necessary
MINUTE_HAND_PIVOT = (CENTER[0] + 10, CENTER[1] + 10)  # Example values, adjust as necessary

def rotate_and_blit(image, angle, pivot, offset):
    """Rotates an image around a pivot point and blits it to the screen."""
    rotated_image = pygame.transform.rotozoom(image, -angle, 1)
    rotated_offset = pygame.Vector2(offset).rotate(-angle)
    position = (pivot[0] + rotated_offset.x - rotated_image.get_width() // 2,
                pivot[1] + rotated_offset.y - rotated_image.get_height() // 2)
    screen.blit(rotated_image, position)

def get_time_angles():
    """Returns the angles for the hour and minute hands based on the current time."""
    now = datetime.now()
    hour_angle = (now.hour % 12) * (360 / 12) + (now.minute / 60) * (30)
    minute_angle = now.minute * (360 / 60)
    return hour_angle, minute_angle

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill the screen with a white background (or your clock's background color)
    screen.blit(mickey_face, (0, 0))  # Blit Mickey's face

    hour_angle, minute_angle = get_time_angles()  # Get the angles for the current time

    rotate_and_blit(left_arm, hour_angle, HOUR_HAND_PIVOT, (0, -left_arm.get_height() // 2))  # Adjust pivot and offset for hour hand
    rotate_and_blit(right_arm, minute_angle, MINUTE_HAND_PIVOT, (0, -right_arm.get_height() // 2))  # Adjust pivot and offset for minute hand

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Tick the clock at 60 FPS

pygame.quit()
