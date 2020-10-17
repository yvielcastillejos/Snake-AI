import pygame
import numpy as np
import sys
import random
from parameters import*

class Snake(object):
   def __init__(self, wall = False):
       # Keep track of snake's length, position, direction, and colour
       self.len = 1
       # A list of xy positions that the snake occupies in the screen
       self.pos = [((S_WIDTH/2),( S_HEIGHT/2))] # put in the middle
       # randomized a direction initially
       self.dir = random.choice([UP,DOWN,LEFT, RIGHT])
       # snake will be black with head as green colour
       self.bodyclr = (33, 31, 34)
       self.headclr = (8, 132, 43)
       self.wall = wall
       self.right = []
       self.left = []
       self.top = []
       self.bot = []
       self.totwall =[]
       # returns previous direction
       self.prev = self.dir
       self.done = False
       
   def get_head_pos(self):
       return self.pos[0]

   def gen_walls(self):
       for i in range(0,S_WIDTH, GRIDSIZE):
           self.right = self.right + [(0,i)]
           self.left = self.left + [(S_HEIGHT-GRIDSIZE, i)]
       for i in range(0,S_HEIGHT, GRIDSIZE):
           self.top = self.top + [(i,0)]
           self.bot = self.bot + [(i, S_WIDTH-GRIDSIZE)] 
       self.totwall = self.right + self.left + self.top + self.bot
   
   def turn(self, point):
       # the point will be as defined by the parameters taken from user input
       # if the length of snake == 1, it can go to any direction
       if self.len == 1:
           self.dir = point
       # if the lenth of snake is not 1, it can only move for three directions
       else:
           if tuple(np.array(point)*-1) == self.dir or tuple(np.array(point)*-1) == self.prev:
               self.dir = self.dir
           else:
               self.dir = point

   def move(self):
       self.prev = self.dir
       cur_head = self.get_head_pos()
       x, y = self.dir
       new_head = (((cur_head[0]+ (x*GRIDSIZE))%S_WIDTH), ((cur_head[1]+ (y*GRIDSIZE))%S_HEIGHT))
       if len(self.pos) > 2 and (new_head in self.pos[2:]):
           self.done = True
           self.reset()
       else:
           # insert the new head position
           self.pos.insert(0,new_head)
           # pop the tail position
           if len(self.pos) > self.len:
               self.pos = self.pos[:-1]
       if self.wall == True:
           self.gen_walls()
           if new_head in self.totwall:
               self.done = True
               self.reset()  
 
   def reset(self):
       # make the default values
       self.len = 1
       self.pos = [((S_WIDTH/2, S_HEIGHT/2))]
       self.dir =  random.choice([UP,DOWN,LEFT, RIGHT])
       self.prev = self.dir

   def draw(self, surface):
       # draw the snake on the surface
       for pos in self.pos:
           if pos == self.pos[0]:
               r = pygame.Rect((pos[0], pos[1]), (GRIDSIZE, GRIDSIZE))
               pygame.draw.rect(surface, self.headclr, r)
               pygame.draw.rect(surface, (255, 255, 255), r, 1)
           else:
               r = pygame.Rect((pos[0], pos[1]), (GRIDSIZE, GRIDSIZE))
               pygame.draw.rect(surface, self.bodyclr, r)
               pygame.draw.rect(surface, (255, 255, 255), r, 1)
       # draw the wall
       if self.wall == True:
           self.gen_walls()
           for block in self.totwall:
               r = pygame.Rect((block[0], block[1]), (GRIDSIZE, GRIDSIZE)) 
               pygame.draw.rect(surface, (59, 108, 178), r)
               pygame.draw.rect(surface, (255, 255, 255), r, 1)

   def handle_keys(self):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
       # check for key presses
           elif event.type == pygame.KEYDOWN:
               if (event.key == pygame.K_UP) or (event.key == pygame.K_w):
                   self.turn(UP)
               elif (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
                   self.turn(DOWN)
               elif (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                   self.turn(LEFT)
               elif (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                   self.turn(RIGHT)

class Apple(object):

   def __init__(self, wall = False):
      # needs one position
      self.pos = (0,0)
      self.colour = (202, 56, 56)
      self.wall = wall
 
   def random_pos(self):
      if self.wall == False:
          x = random.randint(3, 240)
          y = random.randint(3, 240)
          self.pos = (random.randint(0,(GRID_WIDTH-1))*GRIDSIZE, random.randint(0,(GRID_HEIGHT-1))*GRIDSIZE)
      else:
          self.pos = (random.randint(1,(GRID_WIDTH-2))*GRIDSIZE, random.randint(1,(GRID_HEIGHT-2))*GRIDSIZE)

   def draw(self, surface):
       r = pygame.Rect((self.pos[0], self.pos[1]), (GRIDSIZE, GRIDSIZE))
       pygame.draw.rect(surface, self.colour, r)
       pygame.draw.rect(surface, (255, 255, 255), r, 1)

