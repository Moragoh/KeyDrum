# -*- coding: utf-8 -*-
"""
Created on Thu May  4 22:08:22 2017

@author: comcast_wizard
"""
#KeyBand
'''
Drum samples downladed from here: http://www.soundsinhd.com/45-free-sp1200-acoustic-drum-samples-sounds-in-hd/
TF2 sound effects downloaded from the TF2 wiki
Drum image downloaded from Derpo's Magnificent Sprites:
https://forums.terraria.org/index.php?threads/derpos-magnificent-sprites.9091/page-46 
'''
import pygame, sys
from pygame.locals import *

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 12)

'''
songlist = font.render('List of songs:', False, (0,0,0))
(Songs were removed on the published version)
'''

drumlist = font.render('List of drum effects:',False,(0,0,0))
snare_ = font.render('W: Snare',False,(0,0,0)) 
clap_ = font.render('A: Clap',False,(0,0,0))
tom_ = font.render('S: Tom',False,(0,0,0))
hat_ = font.render('D: Hat',False,(0,0,0))
basedrum_ = font.render('Q: Basedrum1',False,(0,0,0))
basedrum2_ = font.render('E: Basedrum2',False,(0,0,0))
crash_ = font.render('R: Crash',False,(0,0,0))
snareroll_ = font.render('F: Snare roll',False,(0,0,0))

effectslist = font.render('List of special effects:',False,(0,0,0))
badum_ = font.render('Y: Badum tss',False,(0,0,0))
scream_ = font.render('U: Wilhelm scream',False,(0,0,0))
gong_ = font.render('I: Gong',False,(0,0,0)) 
yeah_ = font.render('H: Yeah',False,(0,0,0))
nope_ = font.render('J: Nope',False,(0,0,0))
nom_ = font.render('K: Nom nom',False,(0,0,0))
down_ = font.render('L: It goes down!',False,(0,0,0))

stopmusic = font.render('P: Stop all sounds',False,(0,0,0))
pausemusic = font.render('0: Pause all sounds',False,(0,0,0))
unpausemusic = font.render('9: Unpause all sounds',False,(0,0,0))

#Code for making it display in a window
display = pygame.display.set_mode((400, 600))
pygame.display.set_caption('KeyBand')
bg = pygame.image.load("pixdrum.png")
white = (255, 255, 255)

while True: 
    #Background
    display.fill((white))
    display.blit(bg,(125,0))
    
    
    #Text display:
    '''
    display.blit(songlist,(10,100))
    display.blit(weez01,(10,120))
    display.blit(weez02,(10,135))
    display.blit(weez03,(10,150))
    display.blit(weez04,(10,165))
    display.blit(gday01,(10,180))
    display.blit(gday02,(10,195))
    display.blit(oasis01,(10,210))
    '''
    display.blit(drumlist,(10,230))
    display.blit(snare_,(10,245))
    display.blit(clap_,(10,260))
    display.blit(tom_,(10,275))
    display.blit(hat_,(10,290))
    display.blit(basedrum_,(10,305))
    display.blit(basedrum2_,(10,320))
    display.blit(crash_,(10,335))
    display.blit(snareroll_,(10,350))
    display.blit(effectslist,(10,370))
    display.blit(badum_,(10,385))
    display.blit(scream_,(10,400))
    display.blit(gong_,(10,415))
    display.blit(yeah_,(10,430))
    display.blit(nope_,(10,445))
    display.blit(nom_,(10,460))
    display.blit(down_,(10,475))
    display.blit(stopmusic, (10,550))
    display.blit(pausemusic,(10,565))
    display.blit(unpausemusic,(10,580))
    
    pygame.display.update()
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        #Event to check for pressed keys
        if event.type == pygame.KEYDOWN:
            #Choose background music
            #Choose a song (as background music), and then drum along.
            #Songs were removed on the published version
            
            #Play sound effects
            #creates sound objects and assigns them into different channels so they can be played simultaneously
            if event.key == pygame.K_w:
            #snare
                snare = pygame.mixer.Sound('snare.wav')
                snare.set_volume(0.4)
                pygame.mixer.Channel(1).play(snare)
                
            if event.key == pygame.K_a:
            #clap
                clap = pygame.mixer.Sound('clap.wav')
                clap.set_volume(0.4)
                pygame.mixer.Channel(7).play(clap)
                
            if event.key == pygame.K_s:
            #tom
                tom = pygame.mixer.Sound('tom.wav')
                tom.set_volume(0.4)
                pygame.mixer.Channel(2).play(tom)

            if event.key == pygame.K_d:
            #hat
                hat = pygame.mixer.Sound('hat.wav')
                tom.set_volume(0.4)
                pygame.mixer.Channel(4).play(hat)
                
            if event.key == pygame.K_q:
            #basedrum1
                basedrum = pygame.mixer.Sound('basedrum.wav')
                basedrum.set_volume(0.4)
                pygame.mixer.Channel(5).play(basedrum)
                
            if event.key == pygame.K_e:
            #basedrum2
                basedrum2 = pygame.mixer.Sound('basedrum2.wav')
                basedrum2.set_volume(0.4)
                pygame.mixer.Channel(6).play(basedrum2)
                
            if event.key == pygame.K_r:
            #crash
                crash = pygame.mixer.Sound('crash.wav')
                crash.set_volume(0.4)
                pygame.mixer.Channel(3).play(crash)
                
            if event.key == pygame.K_f:
            #snare roll
                snareroll = pygame.mixer.Sound('snareroll.wav')
                snareroll.set_volume(0.4)
                pygame.mixer.Channel(4).play(snareroll)
            
            #Play special effects:
            if event.key == pygame.K_y:
            #badum tss
                badum = pygame.mixer.Sound('badumtss.wav')
                badum.set_volume(0.5)
                pygame.mixer.Channel(1).play(badum)
                
            if event.key == pygame.K_u:
            #wilhelm scream
                scream = pygame.mixer.Sound('willscream.wav')
                scream.set_volume(0.5)
                pygame.mixer.Channel(3).play(scream)
                
            if event.key == pygame.K_i:
            #gong
                gong = pygame.mixer.Sound('gong.wav')
                gong.set_volume(0.45)
                pygame.mixer.Channel(2).play(gong)
                
            if event.key == pygame.K_h:
            #yeah
                yeah = pygame.mixer.Sound('yeah.wav')
                yeah.set_volume(0.6)
                pygame.mixer.Channel(4).play(yeah)
                
            if event.key == pygame.K_j:
            #nope
                nope = pygame.mixer.Sound('nope.wav')
                nope.set_volume(0.6)
                pygame.mixer.Channel(5).play(nope)
                
            if event.key == pygame.K_k:
            #nom nom
                nom = pygame.mixer.Sound('nom.wav')
                nom.set_volume(0.6)
                pygame.mixer.Channel(6).play(nom)
                
            if event.key == pygame.K_l:
                down = pygame.mixer.Sound('down.wav')
                pygame.mixer.Channel(7).play(down)
            
                
            #Stop all sounds:
            if event.key == pygame.K_p:
                pygame.mixer.stop()
            if event.key == pygame.K_0:
                pygame.mixer.pause()
            if event.key == pygame.K_9:
                pygame.mixer.unpause()
 
