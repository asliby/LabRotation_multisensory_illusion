

import psychopy as p
import numpy as np
import random
import os
import csv
import sys
import pygame
from psychopy import prefs
prefs.general['audioLib'] = ['pygame']
from psychopy import visual, core, event, data, sound

# prompt user to enter pair number
SUB = raw_input("Please enter pair number: ")

# looks where code is located and defines this as EXPPATH
EXPPATH = os.path.dirname(os.path.abspath(__file__))

# folder name for pair directory
SUBDIR = "%s/Data/Sub%s/" %(EXPPATH,SUB)

# csvfile name
csvfile = "Sub%s.csv" % SUB

# path for data file
path = SUBDIR + csvfile

# create header
header = ["Subjectnumber","Block", "Trial","GivenFlashes",
"ChosenFlash","CorrectFlash","RTFlash","GivenBeeps",
"ChosenBeeps","CorrectBeeps","RTBeep"]

#check whether subject folder exists. If not, create it and add header to it
if not os.path.exists(SUBDIR):
    os.makedirs(SUBDIR)
    with open(path, 'wb') as f:
        wr = csv.writer(f)
        wr.writerow(header)

#set window parameters MAKE SURE TO CHANGE SIZE WHEN VIEWING ON OWN MONITOR
win = p.visual.Window(size=(1440, 900), color=(-1, -1, -1), colorSpace='rgb', fullscr=True,
allowGUI=True, monitor='testMonitor', blendMode='avg', pos = (-.5, 0),
screen=0, allowStencil=False, stereo=False, winType = 'pyglet')
#parameters for flash
circle = p.visual.Circle(win, units='deg', radius = 2, pos = (0,-5), fillColor = (1, 1, 1), lineColor = (1, 1, 1))
#set fixation cross parameters
fixation = visual.TextStim(win=win, ori=0, name='fixation',
    text='+',    font='Arial',
    pos=(0, 0), height=.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


#beep parameters
beep = p.sound.Sound(value = 3500.0, secs = 0.007, octave = 3)
#instruction for beeps
instruction_B = p.visual.TextStim(win = win, ori = 0, text = 'Number of Beeps',
font = 'Arial Narrow', height = 0.1, color = (1, 1, 1))
#instruction for flashes
instruction_F = p.visual.TextStim(win = win, ori = 0, text = 'Number of Flashes',
font = 'Arial Narrow', height = 0.1, color = (1, 1, 1))
#instruction for joint
instruction_BF = p.visual.TextStim(win = win, ori = 0, text = 'Number of Flashes / Beeps',
font = 'Arial Narrow', height = 0.1, color = (1, 1, 1))
#instruction for beep block
instruction_IB = p.visual.TextStim(win = win, ori = 0, text = 'Beep Block',
font = 'Arial Narrow', height = 0.1, pos = (0,0), color = (1, 1, 1))
#instruction for flash block
instruction_IF = p.visual.TextStim(win = win, ori = 0, text = 'Flash Block',
font = 'Arial Narrow', height = 0.1, pos = (0,0), color = (1, 1, 1))
#instruction for joint block
instruction_J = p.visual.TextStim(win = win, ori = 0, text = 'Joint Block',
font = 'Arial Narrow', height = 0.1, pos = (0,0), color = (1, 1, 1))
#instruction for continue
instruction_E = p.visual.TextStim(win = win, ori = 0, text = 'Please press enter to continue',
font = 'Arial Narrow', height = 0.07, pos = (0,-0.2), color = (1, 1, 1))

#keys for beeps
FPS = 60
#function to play sound
def callsound():
    fpsClock = pygame.time.Clock()
    for frameN in range(16):
        if frameN == 0:
            beep.play()
        fpsClock.tick(FPS)

#function for flash
def flash():
    fpsClock = pygame.time.Clock()
    for frameN in range(16):
        fixation.draw(win)
        if frameN % 30  ==  0:
            circle.draw(win)
        win.flip()
        fpsClock.tick(FPS)
#interval functions
#beep-beep or flash-flash interval
def soa_0():
    fpsClock = pygame.time.Clock()
    for frameN in range(48):
        fixation.draw(win)
        win.flip()
        fpsClock.tick(FPS)
#beep-flash interval
def soa():
    fpsClock = pygame.time.Clock()
    for frameN in range(16):
        fixation.draw(win)
        win.flip()
        fpsClock.tick(FPS)

clock = core.Clock()

#possible combination of blocks array
conditions = [1,2,3]
#randomize block conditions
random.shuffle(conditions)
Trial = 1
for c in range(3):
    #chooses one condition
    Block = conditions[0]
    print "Block = ", Block

    if Block == 1:  #individual beep block
        instruction_IB.draw()
        instruction_E.draw()
        win.flip()
        keys_G = p.event.waitKeys(keyList = ["return","escape"])
        print keys_G
        if keys_G[0] == "escape":
            win.close()
            core.quit()
    elif Block == 2:    #individual flash block
        instruction_IF.draw()
        instruction_E.draw()
        win.flip()
        keys_G = p.event.waitKeys(keyList = ["return","escape"])
        print keys_G
        if keys_G[0] == "escape":
            win.close()
            core.quit()

    elif Block == 3:    #joint block
        instruction_E.draw()
        instruction_J.draw()
        win.flip()
        keys_G = p.event.waitKeys(keyList = ["return","escape"])
        print keys_G
        if keys_G[0] == "escape":
            win.close()
            core.quit()
    #beep/flash combinations
    option = [1, 2, 3, 4, 5, 6, 7, 8, 9]*2 #multiply my 1/9 number of trials desired
    random.shuffle(option)
    for t in range(2): #number of trials per condition
        data = []
        data.append(SUB)
        data.append(Block)
        print "Trial number =", Trial
        data.append(Trial)


        for i in range(1):
            #choose random combination
            core.wait(1)
            optionNum = option[0]
            print "optionNum = ", optionNum

            #1B 1F
            if optionNum == 1:
                callsound()
                soa()
                flash()
                GivenFlash = 1
                GivenBeep = 1
                CorrectFlash = GivenFlash
                CorrectBeep = GivenBeep
            #1B 2F
            elif optionNum == 2:
                callsound()
                soa()
                flash()
                soa_0()
                flash()
                GivenFlash = 2
                GivenBeep = 1
                CorrectFlash = GivenFlash
                CorrectBeep = GivenBeep
            #1B 3F
            elif optionNum == 3:
                callsound()
                soa()
                flash()
                soa_0()
                flash()
                soa_0()
                flash()
                GivenFlash = 3
                GivenBeep = 1
                CorrectFlash = GivenFlash
                CorrectBeep = GivenBeep
            #2B 1F
            elif optionNum == 4:
                callsound()
                soa()
                flash()
                soa()
                callsound()
                GivenFlash = 1
                GivenBeep = 2
                CorrectFlash = GivenFlash
                CorrectBeep = GivenBeep
            #2B 2F
            elif optionNum == 5:
                callsound()
                soa()
                flash()
                soa()
                callsound()
                soa()
                flash()
                GivenFlash = 2
                GivenBeep = 2
                CorrectFlash = GivenFlash
                CorrectBeep = GivenBeep
            #2B 3F
            elif optionNum == 6:
                callsound()
                soa()
                flash()
                soa()
                callsound()
                soa()
                flash()
                soa_0()
                flash()
                GivenFlash = 3
                GivenBeep = 2
                CorrectFlash = GivenFlash
                CorrectBeep = GivenBeep
            #3B 1F
            elif optionNum == 7:
                callsound()
                soa()
                flash()
                soa()
                callsound()
                soa_0()
                callsound()
                GivenFlash = 1
                GivenBeep = 3
                CorrectFlash = GivenFlash
                CorrectBeep = GivenBeep
            #3B 2F
            elif optionNum == 8:
                callsound()
                soa()
                flash()
                soa()
                callsound()
                soa()
                flash()
                soa()
                callsound()
                GivenFlash = 2
                GivenBeep = 3
                CorrectFlash = GivenFlash
                CorrectBeep = GivenBeep
            #3B 3F
            elif optionNum == 9:
                callsound()
                soa()
                flash()
                soa()
                callsound()
                soa()
                flash()
                soa()
                callsound()
                soa()
                flash()
                GivenFlash = 3
                GivenBeep = 3
                CorrectFlash = GivenFlash
                CorrectBeep = GivenBeep
            win.flip()

            #delete flash-beep combination from total possible combo/trial list
            del option[0]
            #records trial numbers
            Trial = Trial + 1
            #participant input
            while True:
                if Block == 1:  #individual beep block
                    instruction_B.draw()
                    win.flip()
                    clock.reset()
                    keys_B = p.event.waitKeys(keyList = ["q", "w", "e", "escape"], timeStamped = clock)
                    if keys_B == "q" or keys_B == "w" or keys_B == "e":
                        break
                    elif keys_B[0] == "escape":
                        win.close()
                        core.quit()

                    print "keys_B = ", keys_B
                    AnswerTB = keys_B[0]
                    AnswerPB = AnswerTB[0]
                    #defines letter keys as numerical value to save in correct Beep or Flash column of data
                    for l in AnswerPB:
                        if (l == "q"):
                            ChosenBeep = 1
                        elif (l == "w"):
                            ChosenBeep = 2
                        elif (l == "e"):
                            ChosenBeep = 3
                        ChosenFlash = "NA"


                    print "AnswerPB = ", AnswerPB
                    print "Given Flash = ", GivenFlash
                    data.append(GivenFlash)
                    print "ChosenFlash = ", ChosenFlash
                    data.append(ChosenFlash)
                    print "CorrectFlash = ", CorrectFlash
                    data.append(CorrectFlash)
                    RTFlash = "NA"
                    data.append(RTFlash)
                    print "Given Beep = ", GivenBeep
                    data.append(GivenBeep)
                    print "ChosenBeep = ", ChosenBeep
                    data.append(ChosenBeep)
                    print "CorrectBeep = ", CorrectBeep
                    data.append(CorrectBeep)
                    RTBeep = AnswerTB[1]
                    data.append(RTBeep)
                    win.flip()
                    break
                elif Block == 2:    #individual flash block
                    instruction_F.draw()
                    win.flip()
                    clock.reset()
                    keys_F = p.event.waitKeys(keyList = ["i", "o", "p", "escape"], timeStamped = clock)
                    if keys_F == "i" or keys_F == "o" or keys_F == "p":
                        break
                    elif keys_F[0] == "escape":
                        win.close()
                        core.quit()

                    print "keys_F = ", keys_F
                    AnswerTF = keys_F[0]
                    AnswerPF = AnswerTF[0]
                    for l in AnswerPF:
                        if (l == "i"):
                            ChosenFlash = 1
                        elif (l == "o"):
                            ChosenFlash = 2
                        elif (l == "p"):
                            ChosenFlash = 3
                        ChosenBeep = "NA"


                    print "AnswerPF = ", AnswerPF
                    print "Given Flash = ", GivenFlash
                    data.append(GivenFlash)
                    print "ChosenFlash = ", ChosenFlash
                    data.append(ChosenFlash)
                    print "CorrectFlash = ", CorrectFlash
                    data.append(CorrectFlash)
                    RTFlash = AnswerTF[1]
                    data.append(RTFlash)
                    print "Given Beep = ", GivenBeep
                    data.append(GivenBeep)
                    print "ChosenBeep = ", ChosenBeep
                    data.append(ChosenBeep)
                    print "CorrectBeep = ", CorrectBeep
                    data.append(CorrectBeep)
                    RTBeep = "NA"
                    data.append(RTBeep)

                    win.flip()
                    break
                elif Block == 3:    #joint block
                    instruction_BF.draw()
                    win.flip()
                    clock.reset()
                    flashresp = 0
                    beepresp = 0
                    #order of participant key press does not matter
                    while flashresp == 0 or beepresp == 0:
                        keys_BF = p.event.waitKeys(keyList = ["q", "w", "e","i", "o", "p", "escape"], timeStamped = clock)
                        if keys_BF[0] == "q" or keys_BF[0] == "w" or keys_BF[0] == "e":
                            beepresp = 1
                            print beepresp
                            AnswerTB = keys_BF[0]
                            AnswerPB = AnswerTB[0]
                        if keys_BF[0] == "i" or keys_BF[0] == "o" or keys_BF[0] == "p":
                            flashresp = 1
                            print flashresp
                            AnswerTF = keys_BF[0]
                            AnswerPF = AnswerTF[0]
                        elif keys_BF[0] == "escape":
                            win.close()
                            core.quit()

                        for l in  AnswerPB:
                            if l == "q":
                                ChosenBeep = 1
                            elif l == "w":
                                ChosenBeep = 2
                            elif l == "e":
                                ChosenBeep = 3

                        for l in AnswerPF:
                            if l == "i":
                                ChosenFlash = 1
                            elif l == "o":
                                ChosenFlash = 2
                            elif l == "p":
                                ChosenFlash = 3

                        print "keys_BF = ", keys_BF
                        print "AnswerPB = ", AnswerPB
                        print "AnswerPF = ", AnswerPF
                        print "Given Flash = ", GivenFlash
                        data.append(GivenFlash)
                        print "ChosenFlash = ", ChosenFlash
                        data.append(ChosenFlash)
                        print "CorrectFlash = ", CorrectFlash
                        data.append(CorrectFlash)
                        RTFlash = AnswerTF[1]
                        data.append(RTFlash)
                        print "Given Beep = ", GivenBeep
                        data.append(GivenBeep)
                        print "ChosenBeep = ", ChosenBeep
                        data.append(ChosenBeep)
                        print "CorrectBeep = ", CorrectBeep
                        data.append(CorrectBeep)
                        RTBeep = AnswerTB[1]
                        data.append(RTBeep)
                    win.flip()
                    print "here"
                    break
        core.wait(2)

    # write data to file
        with open(path, 'a') as f:
            wr = csv.writer(f)
            wr.writerow(data)

    #takes block out of randomization when finished t # of trials
    del conditions[0]


win.close()
core.quit()
