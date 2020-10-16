import pygame
import numpy
import sys
import random
from grid_drawing import drawgrid
from snakegame import Snake, Apple
from parameters import*

def main():
    # initialize pygame
    pygame.init()
 
    # initialize clock so it updates action at any given time
    clock = pygame.time.Clock()

    # Generate screen and surface
    screen = pygame.display.set_mode(size = (S_WIDTH, S_HEIGHT), flags = 0) #,depth = 32)
    surface = pygame.Surface(screen.get_size())

    # convert the pixel format so its faster
    surface = surface.convert()
   
    # draw the checkered background
    drawgrid(surface)
  
    # initialize snake and food
    snake = Snake(wall = True)
    food = Apple(wall = True)
    food.random_pos()
    # initialize score to zero (becomes one when snake eats the apple)
    score = 0
    i = 1
    myfont = pygame.font.SysFont("fontname", 20) 
    while True:
        # initialize to 10 frames per second
        clock.tick(15)
        snake.handle_keys()
        drawgrid(surface)
        snake.move()
        if snake.get_head_pos() == food.pos:
            snake.len += 1
            score += 1
            food.random_pos()
        # handle events
        snake.draw(surface)
        food.draw(surface)
        # Once action transpires, update and refresh the screen & surface
        screen.blit(surface, (0,0))
        text = myfont.render(f"Score {score}", 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()

main()
