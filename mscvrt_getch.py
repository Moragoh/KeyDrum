# -*- coding: utf-8 -*-
"""
Created on Mon May  1 21:27:12 2017

@author: comcast_wizard
"""
from msvcrt import getch
while True:
    key= ord(getch())
    
    if key == 27:
        break
    if key == 113: #the w key
    #play this note