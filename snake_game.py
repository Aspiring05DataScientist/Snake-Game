import pygame
import time
import random

# Initialize pygame
pygame.init()

# Game window size
WIDTH = 600
HEIGHT = 400
BLOCK = 20

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)

# Setup display
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🐍 Snake Game')

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)

def draw_snake(snake_blocks):
    for block in snake_blocks:
        pygame.draw.rect(win, GREEN, [block[0], block[1], BLOCK, BLOCK])

def show_score(score):
    text = font.render("Score: " + str(score), True, WHITE)
    win.blit(text, [10, 10])

def game_loop():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0

    snake = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK) / BLOCK) * BLOCK
    food_y = round(random.randrange(0, HEIGHT - BLOCK) / BLOCK) * BLOCK

    while not game_over:
        while game_close:
            win.fill(BLACK)
            msg = font.render("Game Over! Press R to Restart or Q to Quit", True, RED)
            win.blit(msg, [WIDTH // 6, HEIGHT // 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK
                    x_change = 0

        x += x_change
        y += y_change

        # Check collision with wall
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        win.fill(BLACK)
        pygame.draw.rect(win, RED, [food_x, food_y, BLOCK, BLOCK])

        snake.append([x, y])
        if len(snake) > snake_length:
            del snake[0]

        # Check collision with self
        for block in snake[:-1]:
            if block == [x, y]:
                game_close = True

        draw_snake(snake)
        show_score(snake_length - 1)
        pygame.display.update()

        # Check if food is eaten
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK) / BLOCK) * BLOCK
            food_y = round(random.randrange(0, HEIGHT - BLOCK) / BLOCK) * BLOCK
            snake_length += 1

        clock.tick(10)

    pygame.quit()
    quit()

# Start the game
game_loop()
