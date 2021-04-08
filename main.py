# TETRIS GAME
# By Nguyen Anh Do
# My email: nguyenanhdo200213@gmail.com
# 8/4/2021


import os
import sys
import pygame


from config import *
from shape import Shape
from board import Board
from sound import Sound

class Game:

    def __init__(self):
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT + 1, DELAY)
        pygame.key.set_repeat(225, 25)
        pygame.display.set_caption('Tetris')

        self.surface = pygame.display.set_mode(WND_SIZE)
        self.clock = pygame.time.Clock()
        self.font_16 = pygame.font.SysFont('courier new', 16)
        self.font_30 = pygame.font.SysFont('courier new', 30)
        self.isEndGame = False
        self.isStart = False
        self.soundToggle = True
        self.sound = Sound()

        self.initClasses()

    def run(self):
        self.sound.themeSound()
        self.keyEventHandler()

    def initClasses(self):
        self.board = Board()
        self.shape = Shape(self.surface, self.board)


    def draw(self):
        self.board.draw()
        self.shape.draw()
        self.drawSeparateLine()
        self.drawTopCover()
        self.drawScore()
        self.drawImages()

    def keyEventHandler(self):
        while True:

            self.surface.fill(BLACK)


            # draw first message
            if not self.isStart:
                pygame.draw.rect(self.surface, WHITE, pygame.Rect(10, H // 2, 270, 90))
                self.drawText(self.font_30, 'TETRIS', RED, (85, H // 2 + 6))
                self.drawText(self.font_16, 'Press Space to start', GREEN, (30, H // 2 + 50))
                self.drawText(self.font_16, 'Press M to toggle sound', GREEN, (20, H // 2 + 70))
            self.draw()

            if self.isEndGame:
                pygame.draw.rect(self.surface, WHITE, pygame.Rect(10, H // 2, 270, 90))
                self.drawText(self.font_30, 'Gameover', RED, (77, H // 2 + 6))
                self.drawText(self.font_16, 'Press Space to restart', GREEN, (30, H // 2 + 50))

            for event in pygame.event.get():
                # close window event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.isEndGame = self.checkEndGame()
                
                if not self.isEndGame and self.isStart:
                    if event.type == pygame.USEREVENT + 1:
                        self.shape.fall()

                if event.type == pygame.KEYDOWN:
                    if not self.isEndGame:
                        if event.key == pygame.K_RIGHT:
                            self.shape.moveRight()
                        
                        if event.key == pygame.K_LEFT:
                            self.shape.moveLeft()

                        if event.key == pygame.K_DOWN:
                            self.shape.fall()

                        if event.key == pygame.K_UP:
                            self.shape.rotate()

                        if event.key == pygame.K_m:
                            if self.soundToggle:
                                pygame.mixer_music.pause()
                                self.soundToggle = False
                            else:
                                pygame.mixer_music.play()
                                self.soundToggle = True

                    if event.key == pygame.K_SPACE:
                        if self.isEndGame:
                            self.isEndGame = False
                            self.board = Board()
                            self.shape = Shape(self.surface, self.board)
                        elif not self.isStart:
                            self.isStart = True
        
            pygame.display.update()
            
            self.clock.tick(FPS)

    def drawSeparateLine(self):
        pygame.draw.line(self.surface, WHITE, (W, 0), (W, H), 2)
        pygame.draw.line(self.surface, WHITE, (0, 4 * CS), (W, 4 * CS), 2)

    def drawTopCover(self):
        pygame.draw.rect(self.surface, BLACK, pygame.Rect(0, 0, W + 2, 4 * CS))

    def checkEndGame(self):
        if self.shape.row < 4 and not self.shape.canFall(self.shape.cells):
            return True
        return False

    def drawText(self, font,  text, color, pos = [0,0]):
        s = font.render(text, True, color)
        self.surface.blit(s, pos)

    def drawScore(self):
        self.drawText(self.font_16, 'Your score:', GREEN, (W + 20, CS * 4))
        pygame.draw.rect(self.surface, RED, [W  + 20, T_SPACE + 20, 150, 50], 2)
        self.drawText(self.font_30, str(self.board.score), WHITE, (W + 30, T_SPACE + 28))
 
    def drawImages(self):
        tetrisLogo = pygame.transform.scale(pygame.image.load(os.path.join('imgs','tetris_logo.png')), (300, 50))
        self.surface.blit(tetrisLogo, (10, 30))


if __name__ == '__main__':
    game = Game()
    game.run()