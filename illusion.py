import psychopy as p
import numpy as np
import random
import os
import sys
import pygame

from psychopy import prefs
prefs.general['audioLib'] = ['pygame']
from psychopy.visual import GratingStim, RatingScale, TextStim, ShapeStim
from psychopy import visual, core, event, data, sound
#from numpy.random import random, randint, shuffle, sample
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray


#set window parameters MAKE SURE TO CHANGE SIZE WHEN VIEWING ON OWN MONITOR
win = p.visual.Window(size=(1440, 900), color=(-1, -1, -1), colorSpace='rgb', fullscr=True,
allowGUI=True, monitor='testMonitor', blendMode='avg', pos = (-.5, 0),
screen=0, allowStencil=False, stereo=False, useFBO=True, winType = 'pyglet')

circle = p.visual.Circle(win, units='deg', radius = 2, pos = (0,-5), fillColor = (1, 1, 1), lineColor = (1, 1, 1))
#set fixation cross parameters
fixation = visual.TextStim(win=win, ori=0, name='fixation',
    text='+',    font='Arial',
    pos=(0, 0), height=.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


#pygame.mixer.pre_init(44100,-16,2,2048)
#pygame.init()

beep = p.sound.Sound(value = 3500.0, secs = 0.007, octave = 3)

"""
for frameN in range(57):
    fixation.draw()
    beep.play()
    win.flip()
"""


FPS = 60

def callsound():
    fpsClock = pygame.time.Clock()
    for frameN in range(7):
        if frameN == 0:
            beep.play()
        fpsClock.tick(FPS)


def flash():
    fpsClock = pygame.time.Clock()
    for frameN in range(17):
        fixation.draw(win)
        if frameN % 30  ==  0:
            circle.draw(win)
        win.flip()
        fpsClock.tick(FPS)

def soa():
    fpsClock = pygame.time.Clock()
    for frameN in range(16):
        fixation.draw(win)
        win.flip()
        fpsClock.tick(FPS)




option = [1]


optionNum = random.choice(option)
print optionNum

if optionNum == 1:
    callsound()
    soa()
    flash()
    


"""for i in range(10):
    optionNum = random.choice(option)
    print optionNum

    if optionNum == 1:
        for frameN in range(23):
            fixation.draw(win)
            beep.play()
            win.flip()

        for frameN in range(17):
            fixation.draw(win)
            if frameN % 30  ==  0:
                circle.draw(win)
            win.flip()

    elif optionNum == 2:
        #optionNum ==1
        for frameN in range(50):
            fixation.draw(win)
            win.flip()

        for frameN in range(17):
            fixation.draw(win)
            if frameN % 30 == 0:
                circle.draw(win)
            win.flip()

    elif optionNum ==3:
        #optionNum ==2
        for frameN in range(50):
            fixation.draw(win)
            win.flip()

        for frameN in range(17):
            fixation.draw(win)
            if frameN % 30 == 0:
                circle.draw(win)
            win.flip()"""
