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

# Function definitions useful for structuring the game into a class
def player():
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
    reward = 0
    myfont = pygame.font.SysFont("fontname", 20)
  
    while True:

        # initialize to 10 frames per second
        clock.tick(10)
        action = 1 #random.randrange(0,3)
        point = convert(action, snake)
        snake.handle_keys()
        snake.turn(point)
        drawgrid(surface)
        snake.move()
        reward += 1

        if snake.get_head_pos() == food.pos:
            snake.len += 1
            score += 1
            reward += 100
            food.random_pos()
        observation = get_obs(snake, food)
        done = snake.done 
        if done == True:
           reward = 0
           snake.done = False
        snake.draw(surface)
        food.draw(surface)

        # Once action transpires, update and refresh the screen & surface
        screen.blit(surface, (0,0))
        text = myfont.render(f"Score {score}", 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()

def convert(action, snake):
    if action == 0:
        if snake.dir == UP:
            point = LEFT
        elif snake.dir == DOWN:
            point = RIGHT
        elif snake.dir == RIGHT:
            point = UP
        else:
            point = DOWN
    elif action == 1: 
        if snake.dir == UP:
            point = RIGHT
        elif snake.dir == DOWN:
            point = LEFT
        elif snake.dir == RIGHT:
            point = DOWN
        else:
            point = UP
    elif action == 2:
        point = snake.dir
    return point

def distance(snake, apple,  dir):
    # this should return 3 things:
    # 1. distance to wall 2. distance to food 3. distance to body
    distance = 0
    wall_dis = -1
    apple_dis = -1
    body_dis = -1
    
    # one grid is one unit distance
    un_dis = math.sqrt((dir[0] ** 2) + (dir[1] ** 2))

    # head position
    x_head = snake.get_head_pos()[0]
    y_head = snake.get_head_pos()[1]
    gs = GRIDSIZE

    # for ex, self.dir == left get distance straight of it (-1,0)
    x_inc = dir[0]*gs
    y_inc = dir[1]*gs
  
    # position of walls, apple, and body
    walls = snake.totwall
    apple = apple.pos
    body = snake.pos[1:]
  
    # set variable (it's the only variable that constrains the grid)
    found_wall = False

    # Body, Apple, Wall distance calculation
    while found_wall == False:
        if (x_head, y_head) == body:
            if body_dis == -1:
                body_dis = distance
        if (x_head, y_head) == apple:
            if apple_dis == -1:
                apple_dis = distance
        x_head +=  x_inc
        y_head +=  y_inc
        distance += un_dis
        if (x_head, y_head) in walls:
            wall_dis = distance
            found_wall = True
    if apple_dis == -1:
        # If one unit distance is one grid, we can take the maximum grid distance and just input it into this variable if apple != found
        apple_dis = math.sqrt((GRID_HEIGHT** 2) + (GRID_WIDTH ** 2))
    if body_dis == -1:
        body_dis = math.sqrt((GRID_HEIGHT** 2) + (GRID_WIDTH ** 2))
    return [wall_dis, apple_dis, body_dis]
    

def get_obs(snake, apple):
    # This function will return an array of 8 directions, with 3 distances [wall, apple, body] per direction
    # The order will be clockwise of the directions (i.e. so clockwise of NEWS compass bearing)
    # The reason for this is because we have 3 actions, straight, left or right
    # for example (relative to a snake going up)
    # UP, UPRIGHT, RIGHT, DOWNRIGHT, DOWN, DOWNLEFT, LEFT, UPLEFT
    curr_dir = snake.dir
    if curr_dir == UP:
        observation = np.array([distance(snake, apple, UP), distance(snake, apple, (1,-1)), distance(snake, apple, RIGHT), distance(snake, apple, (1,1)),
                                distance(snake, apple, DOWN), distance(snake, apple, (-1,1)), distance(snake, apple, LEFT), distance(snake, apple, (-1,-1))])
    elif curr_dir == DOWN:
        observation = np.array([distance(snake, apple, DOWN), distance(snake, apple, (-1,1)), distance(snake, apple, LEFT), distance(snake, apple, (-1,-1)),
                                distance(snake, apple, UP), distance(snake, apple, (1,-1)),distance(snake, apple, RIGHT),  distance(snake, apple, (1,1))]) 
    elif curr_dir == LEFT:
        observation = np.array([distance(snake, apple, LEFT), distance(snake, apple, (-1,-1)), distance(snake, apple, UP), distance(snake, apple, (1,-1)),
                                distance(snake, apple, RIGHT),  distance(snake, apple, (1,1)),distance(snake, apple, DOWN), distance(snake, apple, (-1,1))])
    elif curr_dir == RIGHT:
        observation = np.array([distance(snake, apple, RIGHT),  distance(snake, apple, (1,1)),distance(snake, apple, DOWN), distance(snake, apple, (-1,1)),
                                distance(snake, apple, LEFT), distance(snake, apple, (-1,-1)), distance(snake, apple, UP), distance(snake, apple, (1,-1))])
    observation.shape = (24,)
    scale =  math.sqrt((GRID_HEIGHT** 2) + (GRID_WIDTH ** 2))
    # normalizes it so not found = -1
    observation_s = 1-2*observation/scale
    # The more positive a number is the closer it is and vice versa
    return observation_s
  





