# IDEA WE WILL GET SHAPE FROM SHAPEDATA
# EX: SHAPE T WILL LIKE: [
#   [0,1,0], [1,1,1]
# ]
# THE WE WILL CONVERT SHAPE TO LIST OF CELL OBJECT LIKE: [cell, cell, cell, cell]

import pygame
from random import randint

from config import *
from cell import Cell
from shape_data import shapeData, colors
from sound import Sound

class Shape:

    def __init__(self, surface, board):
        self.surface = surface
        self.board = board
        self.row, self.col = 0, 0
        self.cells = []
        self.shape = []
        self.color = ()
        self.score = 0
        self.sound = Sound()

        # spawn new shape
        self.spawnNew()

    def spawnNew(self):
        self.shape = self.getRandomShape()
        self.rotate()
        # renew cells
        self.cells = []
        self.row = 0
        # make default shape's location is center
        self.col = COL // 2 - len(self.shape[0]) // 2 
        self.cells = self.convertToCells(self.shape)
        

    def getRandomShape(self):
        rand = randint(0, len(shapeData) - 1)
        self.color = colors[rand]
        return shapeData[rand]

    def convertToCells(self, shape):
        cells = []
        for i in range(len(shape)):
            for j in range(len(shape[0])):
                if shape[i][j] != 0:
                    cell = Cell(self.surface, i + self.row, j + self.col, self.color)
                    cells.append(cell)
        return cells

    def draw(self):
        for cell in self.cells:
            cell.draw()

    def fall(self):
        if self.canFall(self.cells):
            for cell in self.cells:
                cell.row += 1
                self.row = cell.row - 2
        else:
            self.sound.hitBottomSound()
            self.board.appendShape(self.cells)
            self.board.removeRow()
            self.spawnNew()

    def canFall(self, cells):
        if not self.isHitBottom(cells) and not self.checkCollision(1, 0, self.cells):
            return True
        return False

    def isHitBottom(self, cells):
        for cell in cells:
            if cell.row == ROW - 1:
                return True
        return False

    def moveRight(self):
        if self.canMoveRight(self.cells):
            for cell in self.cells:
                cell.col += 1
                self.col = cell.col - 1

    def canMoveRight(self, cells):
        if not self.isHitRight(cells) and not self.checkCollision(0, 1, cells):
            return True
        return False

    def isHitRight(self, cells):
        for cell in cells:
            if cell.col == COL - 1:
                return True
        return False
    def moveLeft(self):
        if self.canMoveLeft(self.cells):
            for cell in self.cells:
                cell.col -= 1
                self.col = cell.col - 1

    def canMoveLeft(self, cells):
        if not self.isHitLeft(cells) and not self.checkCollision(0, -1, cells):
            return True
        return False

    def isHitLeft(self, cells):
        for cell in cells:
            if cell.col == 0:
                return True
        return False
    
    # rDirection = 1: check at row + 1
    # rDirection = -1: check at row - 1
    # cDirection = 1: check at col + 1
    # cDirection = -1: check at col - 1
    def checkCollision(self, rDirection, cDirection, cells):
        for cell in cells:
            if self.board.isEmptyCell(cell.row + rDirection, cell.col + cDirection):
                return True
        return False

    def rotateMatrix(self, matrix):
        M = len(matrix)
        N = len(matrix[0])

        destination =[[0 for i in range(M)] for j in range(N)]

        for i in range(N):
            for j in range(M):
                destination[i][j] = matrix[M - j - 1][i]
        return destination

    def rotate(self):
        # tmp shape
        shape = self.rotateMatrix(self.shape)
        cells = self.convertToCells(shape)

        # check before rotate
        if self.canRotate(cells):
            self.shape = shape
            self.cells = cells
       

    def canRotate(self, cells):
        if self.checkCollision(0, 0, cells) or self.checkCollision(0, 0, cells)\
            or self.checkCollision(0, 0, cells) or self.checkCollision(0, 0, cells):
            return False
        for cell in cells:
            if cell.row < 0 or cell.row > ROW - 1:
                return False
            elif cell.col < 0 or cell.col > COL - 1:
                return False
        return True
    