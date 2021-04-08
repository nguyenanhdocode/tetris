from config import *

class Board:

    def __init__(self):
        # create row * col matrix
        self.matrix = [[0 for i in range(COL)] for j in range(ROW)]
        self.score = 0

    def appendShape(self, cells):
        for cell in cells:
            self.matrix[cell.row][cell.col] = cell
        

    def draw(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] != 0:
                    self.matrix[i][j].draw()

    def isEmptyCell(self, row, col):
        try:
            return self.matrix[row][col] != 0
        except IndexError:
            pass

    def checkFullRow(self, row):
        count = 0
        for cell in row:
            if cell != 0:
                count += 1
                if count == 10:
                    
                    self.score += 10
                    return True
        return False
        

    def removeRow(self):
        for i in range(len(self.matrix)):
            if self.checkFullRow(self.matrix[i]):
               self.matrix.remove(self.matrix[i])
               self.matrix.insert(0, [0 for i in range(COL)])
               
               for j in range(i + 1):
                   for cell in self.matrix[j]:
                       if cell != 0:
                           cell.row += 1
   