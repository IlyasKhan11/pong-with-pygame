import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100

# Ball dimensions
BALL_SIZE = 10

# Paddle positions
left_paddle = pygame.Rect(10, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball position
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

# Speeds
left_paddle_speed = 0
right_paddle_speed = 0
ball_speed_x = 4
ball_speed_y = 4

# Scores
left_score = 0
right_score = 0

# Font for displaying score
font = pygame.font.Font(None, 74)

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Paddle movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_paddle_speed = -6
            if event.key == pygame.K_s:
                left_paddle_speed = 6
            if event.key == pygame.K_UP:
                right_paddle_speed = -6
            if event.key == pygame.K_DOWN:
                right_paddle_speed = 6
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                left_paddle_speed = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                right_paddle_speed = 0

    # Move paddles
    left_paddle.y += left_paddle_speed
    right_paddle.y += right_paddle_speed

    # Keep paddles on the screen
    left_paddle.y = max(0, min(HEIGHT - PADDLE_HEIGHT, left_paddle.y))
    right_paddle.y = max(0, min(HEIGHT - PADDLE_HEIGHT, right_paddle.y))

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # Ball out of bounds
    if ball.left <= 0:
        right_score += 1
        ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        ball_speed_x *= -1
    if ball.right >= WIDTH:
        left_score += 1
        ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        ball_speed_x *= -1

    # Drawing everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH // 4, 20))
    screen.blit(right_text, (WIDTH * 3 // 4, 20))

    # Update display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)
