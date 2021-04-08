import os
import pygame

class Sound:

    def __init__(self):
        pygame.mixer.init()

    def hitBottomSound(self):
        sound = pygame.mixer.Sound(os.path.join('sounds', 'hitbottom_sound.mp3'))
        pygame.mixer.Sound.play(sound)

    def rotateSound(self):
        pass

    def themeSound(self):
        music = pygame.mixer.music.load(os.path.join('sounds', 'theme_sound.mp3'))
        pygame.mixer.music.play(-1)

    def pause(self):
        pygame.mixer.pause()