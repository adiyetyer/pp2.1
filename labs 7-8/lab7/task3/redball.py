import pygame

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
BALL_SIZE = 50
BALL_RADIUS = BALL_SIZE // 2
BALL_COLOR = (255, 0, 0)  # Red color
MOVE_DISTANCE = 20
FPS = 60

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Ball")

# Start position for the ball
ball_pos = [WIDTH // 2, HEIGHT // 2]

# Function to draw the ball on the screen
def draw_ball(position):
    screen.fill((0, 0, 0))  # Clear screen with black background
    pygame.draw.circle(screen, BALL_COLOR, position, BALL_RADIUS)
    pygame.display.flip()  # Update the display

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_pos[1] = max(BALL_RADIUS, ball_pos[1] - MOVE_DISTANCE)
            elif event.key == pygame.K_DOWN:
                ball_pos[1] = min(HEIGHT - BALL_RADIUS, ball_pos[1] + MOVE_DISTANCE)
            elif event.key == pygame.K_LEFT:
                ball_pos[0] = max(BALL_RADIUS, ball_pos[0] - MOVE_DISTANCE)
            elif event.key == pygame.K_RIGHT:
                ball_pos[0] = min(WIDTH - BALL_RADIUS, ball_pos[0] + MOVE_DISTANCE)

    # Draw the ball
    draw_ball(ball_pos)

    # Cap the frame rate
    pygame.time.Clock().tick(FPS)

pygame.quit()
