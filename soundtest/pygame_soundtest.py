# -*- coding: utf-8 -*-
"""
Created on Wed May  3 21:45:40 2017

@author: comcast_wizard
"""
#Sound testing using pygame
#Drum along to all your favorite Weezer songs!!
#Choose a song (as background music), adn then drum along.
import pygame, sys
from pygame.locals import *
import time
from msvcrt import getch

pygame.init()

DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('KeyBand')

#sound_object = pygame.mixer.Sound('yeah.wav')
#sound_object.play()
#time.sleep(3)
#sound_object.stop()



while True: # main game loop
    while True:
        key = ord(getch())
    
        if key == 27: #esc
            break
        if key == 113: #q
            yeah = pygame.mixer.Sound('yeah.wav')
            yeah.play()
            time.sleep(1)
            yeah.stop()
        if key == 119: #w
            nope = pygame.mixer.Sound('nope.wav')
            nope.play()
            time.sleep(1)
            nope.stop()
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
