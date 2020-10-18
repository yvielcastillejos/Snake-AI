from player import*
import pygame
from pygame.locals import*
import random
import pygame
import numpy as np
import sys
import random
from grid_drawing import drawgrid
from snakegame import Snake, Apple
from parameters import*
import math

# Random snake
# 0 left
# 1 right
# 2 straight

# The class definition is just the main function defined as a class for convenience.
# The differences between the class definition below and main are that observation, done, reward, and info are added
# such a structure is similar to many game environments out there

class Game():
    def __init__(self):
        # initialize objects
        self.snake = Snake(wall=True)
        self.food = Apple(wall=True)
        self.food.random_pos()
        # initialize parameters
        self.observation = []
        self.reward = 0
        self.info = {}
        self.score = 0
        self.done = False
        self.action = 1
        # initialize pygame
        pygame.init()
        # clock in pygame
        self.clock = pygame.time.Clock()
        # renders the python screen
        self.screen = pygame.display.set_mode(size = (S_WIDTH, S_HEIGHT), flags = 0) #,depth = 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        drawgrid(self.surface)
        self.myfont = pygame.font.SysFont("fontname", 20)

    def step(self, action):
        # plays the game given an action / does not need to render pygame screen
        self.action = action
        point = convert(self.action, self.snake)
        if self.done == True:
            self.snake.reset()
            self.reward = -0.2
            self.food.random_pos()
            self.snake.done = False
        else:
            self.reward = -0.1
        self.snake.turn(point)
        self.snake.move()
        if self.snake.get_head_pos() == self.food.pos:
            self.snake.len += 1
            self.score += 1
            self.reward = 0.8
            self.food.random_pos()
        #print(self.reward)
        self.observation = get_obs(self.snake, self.food)
        self.done = self.snake.done
        return  self.observation, self.reward, self.done, self.info

    def render(self):
        # renders the python screen
        self.clock.tick(12)
        drawgrid(self.surface)
        self.snake.handle_keys()
        self.snake.draw(self.surface)
        self.food.draw(self.surface)
        self.screen.blit(self.surface, (0,0))
        text = self.myfont.render(f"Score {self.score}", 1, (0,0,0))
        self.screen.blit(text, (5,10))
        pygame.display.update()

    def reset(self):
        self.snake.reset()
        self.food.random_pos()
        return self.snake.get_head_pos()

    def prints(self):
        print(self.snake.get_head_pos())

                                 
