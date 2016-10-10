import psychopy as p
import numpy as np
import random
import os
import sys
from psychopy.visual import GratingStim, RatingScale, TextStim, ShapeStim
from psychopy import visual, core, event, data
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

for frameN in range(10,100):
    if 30 <= frameN < 110:
        fixation.draw()
        circle.draw()
        win.flip()
