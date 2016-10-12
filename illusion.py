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

#beep parameters
beep = p.sound.Sound(value = 3500.0, secs = 0.007, octave = 3)
#instruction for beeps
instruction_B = p.visual.TextStim(win = win, ori = 0, text = 'Number of Beeps',
font = 'Arial Narrow', height = 0.1, alignVert = 'top', alignHoriz = 'left', color = (1, 1, 1))
#instruction for flashes
instruction_F = p.visual.TextStim(win = win, ori = 0, text = 'Number of Flashes',
font = 'Arial Narrow', height = 0.1, alignVert = 'bottom', color = (1, 1, 1))

instruction_IB = p.visual.TextStim(win = win, ori = 0, text = 'Beep Block',
font = 'Arial Narrow', height = 0.1, alignVert = 'top', pos = (0,0), color = (1, 1, 1))

instruction_IF = p.visual.TextStim(win = win, ori = 0, text = 'Flash Block',
font = 'Arial Narrow', height = 0.1, alignVert = 'top', pos = (0,0), color = (1, 1, 1))

instruction_J = p.visual.TextStim(win = win, ori = 0, text = 'Joint Block',
font = 'Arial Narrow', height = 0.1, alignVert = 'top', pos = (0,0), color = (1, 1, 1))

#keys for beeps
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

def soa_B0():
    fpsClock = pygame.time.Clock()
    for frameN in range(57):
        fixation.draw(win)
        win.flip()
        fpsClock.tick(FPS)

def soa_F0():
    fpsClock = pygame.time.Clock()
    for frameN in range(50):
        fixation.draw(win)
        win.flip()
        fpsClock.tick(FPS)

def soa_F1():
    fpsClock = pygame.time.Clock()
    for frameN in range(16):
        fixation.draw(win)
        win.flip()
        fpsClock.tick(FPS)

def soa_B2():
    fpsClock = pygame.time.Clock()
    for frameN in range(24):
        fixation.draw(win)
        win.flip()
        fpsClock.tick(FPS)

def soa_F2():
    fpsClock = pygame.time.Clock()
    for frameN in range(19):
        fixation.draw(win)
        win.flip()
        fpsClock.tick(FPS)

def soa_B3():
    fpsClock = pygame.time.Clock()
    for frameN in range(21):
        fixation.draw(win)
        win.flip()
        fpsClock.tick(FPS)

def soa_F3():
    fpsClock = pygame.time.Clock()
    for frameN in range(22):
        fixation.draw(win)
        win.flip()
        fpsClock.tick(FPS)

#possible combination array

conditions = [1, 2, 3]
for i in range(1):
    conditionsNum = random.choice(conditions)
    if conditionsNum == 1:
        instruction_IB.draw()
        win.flip()
        keys_G = p.event.waitKeys(keyList = ["return"])
    elif conditionsNum == 2:
        instruction_IF.draw()
        win.flip()
        keys_G = p.event.waitKeys(keyList = ["return"])
    elif conditionsNum == 3:
        instruction_J.draw()
        win.flip()
        keys_G = p.event.waitKeys(keyList = ["return"])

option = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(2):
    #choose random combination
    core.wait(1)
    optionNum = random.choice(option)
    print optionNum

    #1B 1F
    if optionNum == 1:
        callsound()
        soa_F1()
        flash()
    #1B 2F
    elif optionNum == 2:
        callsound()
        soa_F1()
        flash()
        soa_F0()
        flash()
    #1B 3F
    elif optionNum == 3:
        callsound()
        soa_F1()
        flash()
        soa_F0()
        flash()
        soa_F0()
        flash()
    #2B 1F
    elif optionNum == 4:
        callsound()
        soa_F1
        flash()
        soa_B2()
        callsound()
    #2B 2F
    elif optionNum == 5:
        callsound()
        soa_F1
        flash()
        soa_B2()
        callsound()
        soa_F2()
        flash()
    #2B 3F
    elif optionNum == 6:
        callsound()
        soa_F1()
        flash()
        soa_B2()
        callsound()
        soa_F2
        flash()
        soa_F0()
        flash()
    #3B 1F
    elif optionNum == 7:
        callsound()
        soa_F1()
        flash()
        soa_B2()
        callsound()
        soa_B0()
        callsound()
    #3B 2F
    elif optionNum == 8:
        callsound()
        soa_F1()
        flash()
        soa_B2
        callsound()
        soa_F2()
        flash()
        soa_B3()
        callsound()
    #3B 3F
    elif optionNum == 9:
        callsound()
        soa_F1()
        flash()
        soa_B2()
        callsound()
        soa_F2()
        flash()
        soa_B3()
        callsound()
        soa_F3
        flash()
    win.flip()
    #thisresp = None
    while True:
        if conditionsNum == 1:
            instruction_B.draw()
            win.flip()
            keys_B = p.event.waitKeys(keyList = ["q", "w", "e"])
            if keys_B == "q" or keys_B == "w" or keys_B == "e":
                break
            print keys_B
            win.flip()
            break
        elif conditionsNum == 2:
            instruction_F.draw()
            win.flip()
            keys_F = p.event.waitKeys(keyList = ["i", "o", "p"])
            if keys_F == "i" or keys_F == "o" or keys_F == "p":
                break
            win.flip()
            break
        elif conditionsNum == 3:
            instruction_B.draw()
            win.flip()
            keys_B = p.event.waitKeys(keyList = ["q", "w", "e"])
            if keys_B == "q" or keys_B == "w" or keys_B == "e":
                break
            instruction_F.draw()
            win.flip()
            keys_F = p.event.waitKeys(keyList = ["i", "o", "p"])
            if keys_F == "i" or keys_F == "o" or keys_F == "p":
                break
            print keys_B
            print keys_F
            win.flip()
            break
    core.wait(2)
