import pygame
import time
import random

# init pygame
pygame.init()

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)

# display configuration
# define size of the display
width, height = 600, 400
game_display = pygame.display.set_mode((width, height))
# defines a title
pygame.display.set_caption("Snake Game")

# clock configuration
clock = pygame.time.Clock()

# snake configuration
snake_size = 10  # size of one snake pixel
snake_speed = 15

# fonts definition
# creates fonts object -> SysFont
message_font = pygame.font.SysFont("ubuntu", 30)
score_font = pygame.font.SysFont("ubuntu", 25)


def draw_score(score):
    """
       draws the score 
    """
    text = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0, 0])  # text to display and position


# MIN 9:35
def draw_snake(snake_size, snake_pixels):
    """
       draws the snake  
        snake_pixels -> list with the position of the pixels 

    """
    for pixel in snake_pixels :  # TRY TO TAKE THIS LOOP OUT
        # draws a rectangle (pixel)
        # pixel[0] and pixel[1] -> position x and y of the pixel
        # pixel[0], pixel[1] -> snake starts with one pixel sized snake_size
        pygame.draw.rect(game_display, white, [
                         pixel[0], pixel[1], snake_size, snake_size])


def run_game() :
    game_over = False
    game_close = False  # closing the game

    # starting position
    x = width / 2
    y = height / 2

    # snake starts without speed
    x_speed = 0
    y_speed = 0

    # holds the length that the snake gets
    snake_pixels = []
    snake_length = 1

    # target position
    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    # game moves
    while not game_over:

        # handling loss
        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over!", True, red)
            game_display.blit(game_over_message, [width / 3, height / 3])
            print(snake_length - 1)

            '''
            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN :
                    #get off of the loops -> get off of the game
                    if event.key == pygame.K_1 :
                        game_over = True
                        game_close = False
                    #restarts game
                    if event.key == pygame.K_2 :
                        run_game()
                # QUIT = opposite of the pygame.init() -> runs code that deactivates the Pygame library
                if event.type == pygame.QUIT :
                    game_over = True
                    game_close = False
            '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over == True
            # checks if a key is pressed
            if event.type == pygame.KEYDOWN:
                # snake will move in a speed as big as it size
                if event.key == pygame.K_LEFT:
                    x_speed = - snake_size  # x coordinate is decresed to left
                    y_speed = 0  # TRY TO REMOVE THIS LATER
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = - snake_size  # y coordinate is decresed downwards
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_speed

        # checks if the snake reached the screen limits
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        # continous movement of the snake
        x += x_speed
        y += y_speed

        # drawing in the pygame window
        game_display.fill(black)  # background
        pygame.draw.rect(game_display, orange, [
                        target_x, target_y, snake_size, snake_size])  # target

        # add snake head to the list so the snake is moving
        snake_pixels.append([x, y])
        if len(snake_pixels) > snake_length:
            # removes snake tail from the list so the snake doesnt grow automatically
            del snake_pixels[0]

        # iterates till before the last block of pixels
        for pixel in snake_pixels[:-1]:
            # checks if one of the snake pixels is in the head position -> snake hits itself
            if pixel == [x, y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)

        # print score
        print(snake_length - 1)

        pygame.display.update()

        # checks if snake finds a target
        if x == target_x and y == target_y:
            # position a new target
            target_x = round(random.randrange(
                0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(
                0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

        pygame.quit()
        quit()


run_game()
