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

#set window parameters MAKE SURE TO CHANGE SIZE WHEN VIEWING ON OWN MONITOR #1680, 1050 pygame pyglet
win = p.visual.Window(size=(1680, 1050), color=(-1, -1, -1), colorSpace='rgb', fullscr=True,
allowGUI=True, blendMode='avg', screen=0, allowStencil=False, stereo=False, winType = 'pygame', monitor = 'testMonitor')

#parameters for flash
circle = p.visual.Circle(win, units='pix', radius = 38.9, pos = (0,-194.97), fillColor = (1, 1, 1), lineColor = (1, 1, 1))

#set fixation cross parameters
fixation = visual.TextStim(win=win, ori=0, name='fixation',
    text='+',    font='Arial',
    pos=(0, 0), height=.15, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


#beep parameters
beep = p.sound.Sound(value = 3500.0, secs = 0.007, octave = 3)

#instruction for beginning experiment
instruction_A = p.visual.TextStim(win = win, ori = 0, text = 'You will see a series of beeps and flashes.',
font = 'Arial Narrow', height = 0.08, color = (1, 1, 1), pos = (0, .5))

instruction_A2 = p.visual.TextStim(win = win, ori = 0, text = 'The number of each varies independently from 1-3.',
font = 'Arial Narrow', height = 0.08, color = (1, 1, 1), pos = (0, .4))

instruction_A3 = p.visual.TextStim(win = win, ori = 0, text = 'To indicate number of beeps use keys "q, w, e" which are equal to the values 1, 2, 3 respectively.',
font = 'Arial Narrow', height = 0.08, color = (1, 1, 1), pos = (0, .3))

instruction_A4 = p.visual.TextStim(win = win, ori = 0, text = 'To indicate the number of flashes use keys "i, o, p" which are equal to the values 1, 2, 3 respectively.',
font = 'Arial Narrow', height = 0.08, color = (1, 1, 1), pos = (0, .2))

#instruction for beeps
instruction_B = p.visual.TextStim(win = win, ori = 0, text = 'Number of Beeps',
font = 'Arial Narrow', height = 0.1, color = (1, 1, 1), pos = (0, 0.1))

#instruction for flashes
instruction_F = p.visual.TextStim(win = win, ori = 0, text = 'Number of Flashes',
font = 'Arial Narrow', height = 0.1, color = (1, 1, 1), pos = (0, 0.1))

#instruction for beep block
instruction_IB = p.visual.TextStim(win = win, ori = 0, text = 'Beep Block',
font = 'Arial Narrow', height = 0.1, pos = (0,0.7), color = (1, 1, 1))
instruction_IB2 = p.visual.TextStim(win = win, ori = 0, text = 'This is an individual block for the beep particiapnt',
font = 'Arial Narrow', height = 0.07, pos = (0,0.5), color = (1, 1, 1))

#instruction for flash block
instruction_IF = p.visual.TextStim(win = win, ori = 0, text = 'Flash Block',
font = 'Arial Narrow', height = 0.1, pos = (0,0.7), color = (1, 1, 1))
instruction_IF2 = p.visual.TextStim(win = win, ori = 0, text = 'This is an individual block for the flash particiapnt',
font = 'Arial Narrow', height = 0.07, pos = (0,0.5), color = (1, 1, 1))

#instruction for joint block
instruction_J = p.visual.TextStim(win = win, ori = 0, text = 'Joint Block',
font = 'Arial Narrow', height = 0.1, pos = (0,0.7), color = (1, 1, 1))
instruction_J2 = p.visual.TextStim(win = win, ori = 0, text = 'This is a joint block for both participants.  Which participant responds first',
font = 'Arial Narrow', height = 0.07, pos = (0,0.5), color = (1, 1, 1))

instruction_J3 = p.visual.TextStim(win = win, ori = 0, text = 'will vary from trial to trial. Please pay attention to the response order.', font = 'Arial Narrow', height = 0.07, pos = (0,0.4), color = (1, 1, 1))

#instruction for continue
instruction_E = p.visual.TextStim(win = win, ori = 0, text = 'Please press enter to continue',
font = 'Arial Narrow', height = 0.07, pos = (0,0.3), color = (1, 1, 1))

#frames per second
FPS = 60

#function to play sound
def callsound():
    fpsClock = pygame.time.Clock()
    for frameN in range(1):
        if frameN == 0:
            beep.play()
        fpsClock.tick(FPS)

#function for flash
def flash():
    fpsClock = pygame.time.Clock()
    for frameN in range(1):
        fixation.draw(win)
        if frameN % 30  ==  0:
            circle.draw(win)
        win.flip()
        fpsClock.tick(FPS)
#interval functions
#beep-beep or flash-flash interval
def soa_0():
    fpsClock = pygame.time.Clock()
    for frameN in range(3):
        fixation.draw(win)
        win.flip()
        fpsClock.tick(FPS)
#beep-flash interval
def soa():
    fpsClock = pygame.time.Clock()
    for frameN in range(1):
        fixation.draw(win)
        win.flip()
        fpsClock.tick(FPS)

#setting clocks for keypress timestamps
clock_B = core.Clock()
clock_F = core.Clock()

#possible combination of blocks array
conditions = [1, 2, 3]

#randomize block conditions
random.shuffle(conditions)
#sets trials at one
Trial = 1

#draw beginning insturctions with enter press to continue
instruction_A.draw()
instruction_A2.draw()
instruction_A3.draw()
instruction_A4.draw()

win.flip()
keys_A = p.event.waitKeys(keyList = ["return","escape"])
print keys_A
if keys_A[0] == "escape":
    win.close()
    core.quit()
win.flip()

#begins experiment with particular block
for c in range(3):
    fixation.draw()
    #chooses one condition
    Block = conditions[0]
    print "Block = ", Block

    if Block == 1:  #individual beep block
        instruction_IB.draw()
        instruction_IB2.draw()
        instruction_E.draw()
        win.flip()
        keys_G = p.event.waitKeys(keyList = ["return","escape"])
        print keys_G
        if keys_G[0] == "escape":
            win.close()
            core.quit()
    elif Block == 2:    #individual flash block
        instruction_IF.draw()
        instruction_IF2.draw()
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
        instruction_J2.draw()
        instruction_J3.draw()
        win.flip()
        keys_G = p.event.waitKeys(keyList = ["return","escape"])
        print keys_G
        if keys_G[0] == "escape":
            win.close()
            core.quit()

    #beep/flash combinations
    option = [1, 2, 3, 4, 5, 6, 7, 8, 9]*10 #multiply my 1/9 number of trials desired
    random.shuffle(option)
    for t in range(30): #number of trials per condition
        #set up data saves
        data = []
        data.append(SUB)
        data.append(Block)
        print "Trial number =", Trial
        data.append(Trial)


        for i in range(1):
            #choose random combination
            '''for frameN in range(60):
                fixation.draw()
                win.flip()'''
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
                    fixation.draw()
                    instruction_B.draw()
                    win.flip()
                    clock_B.reset()
                    keys_B = p.event.waitKeys(keyList = ["q", "w", "e", "escape"])
                    if keys_B == "q" or keys_B == "w" or keys_B == "e":
                        #time stamps the key press
                        clock_B.getTime()
                        break
                    elif keys_B[0] == "escape":
                        win.close()
                        core.quit()

                    print "keys_B = ", keys_B
                    print "clock_B = ", clock_B.getTime()
                    AnswerPB = keys_B

                    #defines letter keys as numerical value to save in correct Beep or Flash column of data
                    for l in AnswerPB:
                        if (l == "q"):
                            ChosenBeep = 1
                        elif (l == "w"):
                            ChosenBeep = 2
                        elif (l == "e"):
                            ChosenBeep = 3
                        ChosenFlash = "NA"

                    #appends data to file
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
                    RTBeep = clock_B.getTime()
                    data.append(RTBeep)
                    win.flip()
                    break

                elif Block == 2:    #individual flash block
                    fixation.draw()
                    instruction_F.draw()
                    win.flip()
                    clock_F.reset()
                    keys_F = p.event.waitKeys(keyList = ["i", "o", "p", "escape"])
                    if keys_F == "i" or keys_F == "o" or keys_F == "p":
                        #timestamps key press
                        clock_F.getTime()
                        break
                    elif keys_F[0] == "escape":
                        win.close()
                        core.quit()

                    print "keys_F = ", keys_F
                    print "clock_F = ", clock_F.getTime()
                    AnswerPF = keys_F
                    for l in AnswerPF:
                        if (l == "i"):
                            ChosenFlash = 1
                        elif (l == "o"):
                            ChosenFlash = 2
                        elif (l == "p"):
                            ChosenFlash = 3
                        ChosenBeep = "NA"

                    #appends data to file
                    print "AnswerPF = ", AnswerPF
                    print "Given Flash = ", GivenFlash
                    data.append(GivenFlash)
                    print "ChosenFlash = ", ChosenFlash
                    data.append(ChosenFlash)
                    print "CorrectFlash = ", CorrectFlash
                    data.append(CorrectFlash)
                    RTFlash = clock_F.getTime()
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
                    #randomizes which participant responds first in a joint block trial
                    Randomization = [1, 2]
                    random.shuffle(Randomization)
                    if Randomization[0] == 1:
                        fixation.draw()
                        instruction_B.draw()
                        win.flip()
                        clock_B.reset()
                        keys_B = p.event.waitKeys(keyList = ["q", "w", "e", "escape"])

                        if keys_B == "q" or keys_B == "w" or keys_B == "e":
                            clock_B.getTime()
                            break
                        elif keys_B[0] == "escape":
                            win.close()
                            core.quit()

                        #flash instructions
                        fixation.draw()
                        instruction_F.draw()
                        win.flip()
                        clock_F.reset()
                        keys_F = p.event.waitKeys(keyList = ["i", "o", "p", "escape"])
                        if keys_F == "i" or keys_F == "o" or keys_F == "p":
                            clock_F.getTime()
                            break
                        elif keys_F[0] == "escape":
                            win.close()
                            core.quit()
                    #flips randomization order from above
                    if Randomization[0] == 2:
                        fixation.draw()
                        instruction_F.draw()
                        win.flip()
                        clock_F.reset()
                        keys_F = p.event.waitKeys(keyList = ["i", "o", "p", "escape"])
                        if keys_F == "i" or keys_F == "o" or keys_F == "p":
                            clock_F.getTime()
                            break
                        elif keys_F[0] == "escape":
                            win.close()
                            core.quit()

                        #beep instructions
                        fixation.draw()
                        instruction_B.draw()
                        win.flip()
                        clock_B.reset()
                        keys_B = p.event.waitKeys(keyList = ["q", "w", "e", "escape"])

                        if keys_B == "q" or keys_B == "w" or keys_B == "e":
                            clock_B.getTime()
                            break
                        elif keys_B[0] == "escape":
                            win.close()
                            core.quit()
                    #sets keys as numerical values
                    AnswerPB = keys_B
                    for l in  AnswerPB:
                        if l == "q":
                            ChosenBeep = 1
                        elif l == "w":
                            ChosenBeep = 2
                        elif l == "e":
                            ChosenBeep = 3

                    AnswerPF = keys_F
                    for l in AnswerPF:
                        if l == "i":
                            ChosenFlash = 1
                        elif l == "o":
                            ChosenFlash = 2
                        elif l == "p":
                            ChosenFlash = 3

                    #appends data to file
                    print "keys_B = ", keys_B
                    print "keys_F = ", keys_F
                    print "clock_B = ", clock_B.getTime()
                    print "clock_F = ", clock_F.getTime()
                    print "AnswerPB = ", AnswerPB
                    print "AnswerPF = ", AnswerPF
                    print "Given Flash = ", GivenFlash
                    data.append(GivenFlash)
                    print "ChosenFlash = ", ChosenFlash
                    data.append(ChosenFlash)
                    print "CorrectFlash = ", CorrectFlash
                    data.append(CorrectFlash)
                    RTFlash = clock_F.getTime()
                    data.append(RTFlash)
                    print "Given Beep = ", GivenBeep
                    data.append(GivenBeep)
                    print "ChosenBeep = ", ChosenBeep
                    data.append(ChosenBeep)
                    print "CorrectBeep = ", CorrectBeep
                    data.append(CorrectBeep)
                    RTBeep = clock_B.getTime()
                    data.append(RTBeep)
                    win.flip()
                    break
        #allows fixation cross to always be on the screen (for one second total)
        for frameN in range(60):
            fixation.draw()
            win.flip()


    # write data to file
        with open(path, 'a') as f:
            wr = csv.writer(f)
            wr.writerow(data)

    #takes block out of randomization when finished t # of trials
    del conditions[0]


win.close()
core.quit()
