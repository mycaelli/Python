import pygame
import time
import random

#init pygame
pygame.init()

#define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)

#display configuration
#define size of the display
width, height = 600, 400
game_display = pygame.display.set_mode((width, height))
#defines a title 
pygame.display.set_caption("Snake Game")

#clock configuration
clock = pygame.time.Clock()

#snake configuration (pixels)
snake_size = 10
snake_speed = 15

#fonts definition
#creates fonts object -> SysFont
message_font = pygame.font.SysFont("ubuntu", 30)
score_font = pygame.font.SysFont("ubuntu", 25)

def draw_score(score) :
    """
       draws the score 
    """
    text = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [0,0]) # text to display and position 


#MIN 9:35
def draw_snake(snake_size, snake_pixels) :
    """
       draws the snake 
       
    """
    for pixel in snake_pixels :
        #draws a rectangle (pixel)
        #pixel[0] and pixel[1] -> draws pixel in the required position
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])