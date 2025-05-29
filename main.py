import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
display_width = 500
display_height = 500

# Initialize game display
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Set game clock
clock = pygame.time.Clock()

# Snake block size and speed
snake_block = 10
snake_speed = 6

# Font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    """Display the current score."""
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    """Draw the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """Display a message on the screen."""
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [display_width / 6, display_height / 3])

def gameLoop():
    """Main game loop."""
    game_over = False
    game_close = False

    # Initial snake position
    x1 = display_width / 2
    y1 = display_height / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            # Game over screen
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            # Check for play again or quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        # Check for wall collision
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
            print("Wall collision detected")

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        # Draw food
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        # Update snake body
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        # Remove extra segments if snake exceeds maximum length
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for self collision
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
                print("Self collision detected")

        # Draw snake
        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Check for food collision
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            print("Food eaten, length increased to", length_of_snake)

        # Control game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()
