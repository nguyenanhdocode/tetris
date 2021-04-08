import pygame

from config  import *

class Cell:

    def __init__(self, surface, row, col, color):
        self.surface = surface
        self.row = row
        self.col = col
        self.color = color


    def draw(self):
        pygame.draw.rect(self.surface, self.color, pygame.Rect(self.col * CS + LINE_W, self.row * CS + LINE_W, CS - 3 * LINE_W, CS - 3 * LINE_W))

