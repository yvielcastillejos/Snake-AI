import pygame
import numpy
import sys
import random
from parameters import*
#from grid_drawing import drawgrid
#from snakegame import snake, food

def drawgrid(surface):
   clr1 = (242, 250, 204)
   clr2 = (144, 179, 244)
   for y in range(0, int(GRID_HEIGHT)):
       for x in range(int(GRID_WIDTH)):
          # make a checkered background
          if (x+y)%2 == 0:
              # Size of a rectangle and position
              r = pygame.Rect((GRIDSIZE*x, GRIDSIZE*y),(GRIDSIZE, GRIDSIZE))
              # draw the rectangle on surface at position r with size defined in r
              pygame.draw.rect(surface, clr2 , r)
          else:
              # Size of a rectangle and position
              r = pygame.Rect((GRIDSIZE*x, GRIDSIZE*y),(GRIDSIZE, GRIDSIZE))
              # draw the rectangle on surface at position r with size defined in r
              pygame.draw.rect(surface, clr1, r)
   return


