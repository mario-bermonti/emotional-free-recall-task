#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.5),
    on lun  8 jul 16:20:04 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.5'
expName = 'free recall task'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/MBP/Box Sync/PHSU/Design and stats consultation/Eliut Rivera/Suicide and Emotional Regulation Project/Free recall task/free recall task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "choose_block_setup"
choose_block_setupClock = core.Clock()
import random
import pandas as pd

# Specify the name of the file that specifies the 
# range of trials in each block
block_ranges = pd.read_csv('choose_blocks.csv')

# Randomize experiment blocks
block_ranges_exp = list(block_ranges.choose_blocks_exp)
random.shuffle(block_ranges_exp)


# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text_instructions = visual.TextStim(win=win, name='text_instructions',
    text="Vas a ver una lista de palabras.\n\nLas palabras van a ser presentadas una a la vez. \n\nLuego vas a escribir todas las palabras que recuerdes de la lista, separadas por un espacio.\n\nPresiona 'Enter' cuando termines de escribir todas las palabras que recuerdes.\n\n\nPresiona cualquier tecla para continuar.",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation_cross_routine"
fixation_cross_routineClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.15, 0.15),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "practice_words"
practice_wordsClock = core.Clock()
text_word_practice = visual.TextStim(win=win, name='text_word_practice',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
current_word_list = []

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISI_screen = visual.Rect(
    win=win, name='ISI_screen',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "participant_response_practice"
participant_response_practiceClock = core.Clock()
text_prompt_practice = visual.TextStim(win=win, name='text_prompt_practice',
    text='Escribe palabras:',
    font='Arial',
    pos=(0, .20), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
resp_feedback_practice = visual.TextStim(win=win, name='resp_feedback_practice',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp_feedback_text_practice= ''

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text_instructions = visual.TextStim(win=win, name='text_instructions',
    text="Vas a ver una lista de palabras.\n\nLas palabras van a ser presentadas una a la vez. \n\nLuego vas a escribir todas las palabras que recuerdes de la lista, separadas por un espacio.\n\nPresiona 'Enter' cuando termines de escribir todas las palabras que recuerdes.\n\n\nPresiona cualquier tecla para continuar.",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fixation_cross_routine"
fixation_cross_routineClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.15, 0.15),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()
text_word = visual.TextStim(win=win, name='text_word',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
current_word_list = []
current_word_list_valence = []

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISI_screen = visual.Rect(
    win=win, name='ISI_screen',
    width=(1, 1)[0], height=(1, 1)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor='black', fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "participant_response_exp"
participant_response_expClock = core.Clock()
text_prompt_exp = visual.TextStim(win=win, name='text_prompt_exp',
    text='Escribe palabras:',
    font='Arial',
    pos=(0, .20), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
resp_feedback_exp = visual.TextStim(win=win, name='resp_feedback_exp',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
resp_feedback_text_exp = ''

# Initialize components for Routine "rest"
restClock = core.Clock()
# Initial value for word list
word_list_number = 1
text_rest_instructions = visual.TextStim(win=win, name='text_rest_instructions',
    text='¡Toma un descanso!\n\nPresiona cualquier tecla para comenzar\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "choose_block_setup"-------
t = 0
choose_block_setupClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
choose_block_setupComponents = []
for thisComponent in choose_block_setupComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "choose_block_setup"-------
while continueRoutine:
    # get current time
    t = choose_block_setupClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in choose_block_setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "choose_block_setup"-------
for thisComponent in choose_block_setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "choose_block_setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instructions"-------
    t = 0
    InstructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_start = event.BuilderKeyResponse()
    # keep track of which components have finished
    InstructionsComponents = [text_instructions, key_resp_start]
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Instructions"-------
    while continueRoutine:
        # get current time
        t = InstructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_instructions* updates
        if t >= 0.0 and text_instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_instructions.tStart = t
            text_instructions.frameNStart = frameN  # exact frame index
            text_instructions.setAutoDraw(True)
        
        # *key_resp_start* updates
        if t >= 0.0 and key_resp_start.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_start.tStart = t
            key_resp_start.frameNStart = frameN  # exact frame index
            key_resp_start.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_start.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instructions"-------
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "fixation_cross_routine"-------
    t = 0
    fixation_cross_routineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_cross_routineComponents = [polygon]
    for thisComponent in fixation_cross_routineComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation_cross_routine"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation_cross_routineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon.status == STARTED and t >= frameRemains:
            polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_cross_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_cross_routine"-------
    for thisComponent in fixation_cross_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    practice_trial = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('practice_trials.csv'),
        seed=None, name='practice_trial')
    thisExp.addLoop(practice_trial)  # add the loop to the experiment
    thisPractice_trial = practice_trial.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            exec('{} = thisPractice_trial[paramName]'.format(paramName))
    
    for thisPractice_trial in practice_trial:
        currentLoop = practice_trial
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
        if thisPractice_trial != None:
            for paramName in thisPractice_trial:
                exec('{} = thisPractice_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "practice_words"-------
        t = 0
        practice_wordsClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        text_word_practice.setText(text)
        
        # keep track of which components have finished
        practice_wordsComponents = [text_word_practice]
        for thisComponent in practice_wordsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "practice_words"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practice_wordsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_word_practice* updates
            if t >= 0.0 and text_word_practice.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_word_practice.tStart = t
                text_word_practice.frameNStart = frameN  # exact frame index
                text_word_practice.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_word_practice.status == STARTED and t >= frameRemains:
                text_word_practice.setAutoDraw(False)
            
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_wordsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "practice_words"-------
        for thisComponent in practice_wordsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        current_word_list.append(text)
        
        # ------Prepare to start Routine "ISI"-------
        t = 0
        ISIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [ISI_screen]
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ISI_screen* updates
            if t >= 0.0 and ISI_screen.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI_screen.tStart = t
                ISI_screen.frameNStart = frameN  # exact frame index
                ISI_screen.setAutoDraw(True)
            frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if ISI_screen.status == STARTED and t >= frameRemains:
                ISI_screen.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
    # completed 1 repeats of 'practice_trial'
    
    
    # ------Prepare to start Routine "participant_response_practice"-------
    t = 0
    participant_response_practiceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_practice = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    participant_response_practiceComponents = [key_resp_practice, text_prompt_practice, resp_feedback_practice]
    for thisComponent in participant_response_practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "participant_response_practice"-------
    while continueRoutine:
        # get current time
        t = participant_response_practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_practice* updates
        if t >= 0 and key_resp_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_practice.tStart = t
            key_resp_practice.frameNStart = frameN  # exact frame index
            key_resp_practice.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_practice.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_practice.status == STARTED:
            theseKeys = event.getKeys(keyList=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'space', 'backspace', 'return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_practice.keys.extend(theseKeys)  # storing all keys
                key_resp_practice.rt.append(key_resp_practice.clock.getTime())
        
        # *text_prompt_practice* updates
        if t >= 0 and text_prompt_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_prompt_practice.tStart = t
            text_prompt_practice.frameNStart = frameN  # exact frame index
            text_prompt_practice.setAutoDraw(True)
        
        # *resp_feedback_practice* updates
        if t >= 0 and resp_feedback_practice.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_feedback_practice.tStart = t
            resp_feedback_practice.frameNStart = frameN  # exact frame index
            resp_feedback_practice.setAutoDraw(True)
        if resp_feedback_practice.status == STARTED:  # only update if drawing
            resp_feedback_practice.setText(resp_feedback_text_practice
, log=False)
        # insert the correct symbol when the participant
        # press backspace
        if "backspace" in key_resp_practice.keys:
            key_resp_practice.keys.remove("backspace")
            
            if len(key_resp_practice.keys) > 0:
                key_resp_practice.keys.pop()
                
        # insert the correct symbol when the participant
        # press space
        elif "space" in key_resp_practice.keys:
                key_resp_practice.keys.remove("space")
                key_resp_practice.keys.append(' ')
        
        # save results and end routine when
        # return in entered
        elif 'return' in key_resp_practice.keys:
            key_resp_practice.keys.remove('return')
            # add data to results file
            thisExp.addData('text', 'summary_practice')
            thisExp.addData('word_list', ' '.join(current_word_list))
            thisExp.addData('word_list_valence', ' '.join(current_word_list_valence))
            thisExp.addData('recall_resp_exp', resp_feedback_text_practice)
            continueRoutine = False
                
        resp_feedback_text_practice = ''.join(key_resp_practice.keys)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in participant_response_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "participant_response_practice"-------
    for thisComponent in participant_response_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_practice.keys in ['', [], None]:  # No response was made
        key_resp_practice.keys=None
    thisExp.addData('key_resp_practice.keys',key_resp_practice.keys)
    if key_resp_practice.keys != None:  # we had a response
        thisExp.addData('key_resp_practice.rt', key_resp_practice.rt)
    thisExp.nextEntry()
    resp_feedback_text_practice = ''
    current_word_list.clear()
    current_word_list_valence.clear()
    # the Routine "participant_response_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'practice'


# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_start = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [text_instructions, key_resp_start]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instructions* updates
    if t >= 0.0 and text_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instructions.tStart = t
        text_instructions.frameNStart = frameN  # exact frame index
        text_instructions.setAutoDraw(True)
    
    # *key_resp_start* updates
    if t >= 0.0 and key_resp_start.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_start.tStart = t
        key_resp_start.frameNStart = frameN  # exact frame index
        key_resp_start.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_start.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block_loops = data.TrialHandler(nReps=len(block_ranges_exp), method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block_loops')
thisExp.addLoop(block_loops)  # add the loop to the experiment
thisBlock_loop = block_loops.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock_loop.rgb)
if thisBlock_loop != None:
    for paramName in thisBlock_loop:
        exec('{} = thisBlock_loop[paramName]'.format(paramName))

for thisBlock_loop in block_loops:
    currentLoop = block_loops
    # abbreviate parameter names if possible (e.g. rgb = thisBlock_loop.rgb)
    if thisBlock_loop != None:
        for paramName in thisBlock_loop:
            exec('{} = thisBlock_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation_cross_routine"-------
    t = 0
    fixation_cross_routineClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_cross_routineComponents = [polygon]
    for thisComponent in fixation_cross_routineComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation_cross_routine"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation_cross_routineClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon.status == STARTED and t >= frameRemains:
            polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_cross_routineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_cross_routine"-------
    for thisComponent in fixation_cross_routineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    word_list = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('exp_trials.csv', selection=block_ranges_exp.pop()),
        seed=None, name='word_list')
    thisExp.addLoop(word_list)  # add the loop to the experiment
    thisWord_list = word_list.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisWord_list.rgb)
    if thisWord_list != None:
        for paramName in thisWord_list:
            exec('{} = thisWord_list[paramName]'.format(paramName))
    
    for thisWord_list in word_list:
        currentLoop = word_list
        # abbreviate parameter names if possible (e.g. rgb = thisWord_list.rgb)
        if thisWord_list != None:
            for paramName in thisWord_list:
                exec('{} = thisWord_list[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        text_word.setText(text)
        
        # keep track of which components have finished
        trialComponents = [text_word]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_word* updates
            if t >= 0.0 and text_word.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_word.tStart = t
                text_word.frameNStart = frameN  # exact frame index
                text_word.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_word.status == STARTED and t >= frameRemains:
                text_word.setAutoDraw(False)
            
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        current_word_list.append(text)
        current_word_list_valence.append(condition)
        
        # ------Prepare to start Routine "ISI"-------
        t = 0
        ISIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [ISI_screen]
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ISI_screen* updates
            if t >= 0.0 and ISI_screen.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI_screen.tStart = t
                ISI_screen.frameNStart = frameN  # exact frame index
                ISI_screen.setAutoDraw(True)
            frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if ISI_screen.status == STARTED and t >= frameRemains:
                ISI_screen.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
    # completed 1 repeats of 'word_list'
    
    
    # ------Prepare to start Routine "participant_response_exp"-------
    t = 0
    participant_response_expClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_exp = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    participant_response_expComponents = [key_resp_exp, text_prompt_exp, resp_feedback_exp]
    for thisComponent in participant_response_expComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "participant_response_exp"-------
    while continueRoutine:
        # get current time
        t = participant_response_expClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_exp* updates
        if t >= 0 and key_resp_exp.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_exp.tStart = t
            key_resp_exp.frameNStart = frameN  # exact frame index
            key_resp_exp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_exp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_exp.status == STARTED:
            theseKeys = event.getKeys(keyList=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'space', 'backspace', 'return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_exp.keys.extend(theseKeys)  # storing all keys
                key_resp_exp.rt.append(key_resp_exp.clock.getTime())
        
        # *text_prompt_exp* updates
        if t >= 0 and text_prompt_exp.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_prompt_exp.tStart = t
            text_prompt_exp.frameNStart = frameN  # exact frame index
            text_prompt_exp.setAutoDraw(True)
        
        # *resp_feedback_exp* updates
        if t >= 0 and resp_feedback_exp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_feedback_exp.tStart = t
            resp_feedback_exp.frameNStart = frameN  # exact frame index
            resp_feedback_exp.setAutoDraw(True)
        if resp_feedback_exp.status == STARTED:  # only update if drawing
            resp_feedback_exp.setText(resp_feedback_text_exp, log=False)
        # insert the correct symbol when the participant
        # press backspace
        if "backspace" in key_resp_exp.keys:
            key_resp_exp.keys.remove("backspace")
            
            if len(key_resp_exp.keys) > 0:
                key_resp_exp.keys.pop()
                
        # insert the correct symbol when the participant
        # press space
        elif "space" in key_resp_exp.keys:
                key_resp_exp.keys.remove("space")
                key_resp_exp.keys.append(' ')
        
        # save results and end routine when
        # return in entered
        elif 'return' in key_resp_exp.keys:
            key_resp_exp.keys.remove('return')
            # add data to results file
            thisExp.addData('text', 'summary')
            thisExp.addData('word_list', ' '.join(current_word_list))
            thisExp.addData('word_list_valence', ' '.join(current_word_list_valence))
            thisExp.addData('recall_resp_exp', resp_feedback_text_exp)
            continueRoutine = False
                
        resp_feedback_text_exp = ''.join(key_resp_exp.keys)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in participant_response_expComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "participant_response_exp"-------
    for thisComponent in participant_response_expComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_exp.keys in ['', [], None]:  # No response was made
        key_resp_exp.keys=None
    block_loops.addData('key_resp_exp.keys',key_resp_exp.keys)
    if key_resp_exp.keys != None:  # we had a response
        block_loops.addData('key_resp_exp.rt', key_resp_exp.rt)
    resp_feedback_text_exp = ''
    current_word_list.clear()
    current_word_list_valence.clear()
    # the Routine "participant_response_exp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rest"-------
    t = 0
    restClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # Presents a break if the number of the current 
    # list is in the list
    
    # If the number of lists presented before each
    # rest changes, the list needs to be updated with the
    # trial number after which there should be
    # a break
    if word_list_number not in [3, 6, 9]:
        continueRoutine = False
    
    # Needs to be updated after verifying
    # the list of word lists so it correctly
    # presents the break after the specified
    # word list number
    word_list_number += 1
    key_stop_rest = event.BuilderKeyResponse()
    # keep track of which components have finished
    restComponents = [text_rest_instructions, key_stop_rest]
    for thisComponent in restComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "rest"-------
    while continueRoutine:
        # get current time
        t = restClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_rest_instructions* updates
        if t >= 0.0 and text_rest_instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_rest_instructions.tStart = t
            text_rest_instructions.frameNStart = frameN  # exact frame index
            text_rest_instructions.setAutoDraw(True)
        
        # *key_stop_rest* updates
        if t >= 0.0 and key_stop_rest.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_stop_rest.tStart = t
            key_stop_rest.frameNStart = frameN  # exact frame index
            key_stop_rest.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_stop_rest.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed len(block_ranges_exp) repeats of 'block_loops'







# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
