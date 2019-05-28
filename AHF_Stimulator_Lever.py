 #! /usr/bin/python
#-*-coding: utf-8 -*

import ptLeverThread
from array import array
from AHF_Stimulator import AHF_Stimulator
from AHF_Rewarder import AHF_Rewarder
import time
import json


# a1 =lt.posBuffer[68:75] + lt.posBuffer [0:67] + lt.posBuffer [68:120]
class AHF_Stimulator_Lever (AHF_Stimulator):
    """
    AHF_Stimulator_Lever runs a lever task by calling ptLeverThread C-module code that records lever position and puts torque on the lever
    """
    LEVER_FREQ = 250 # as set in leverThread.h when ptLeverThread c module is compiled. Frequency in Hz of updating lever position and lever force
    """
    Global settings for the task, things that do not vary on a per mouse basis
    These inlcude hardware settings, trial timing, 
    """
    defaultRecordingTime = 4 #  maximum of seconds of lever position data that will be recorded per trial
    defaultLeverIsReversed = False # False means lever position numbers start at 0 and get bigger when mouse pulls lever, True means numbers get smaller
    defaultGoalCuePin = 23 # GPIO pin to use for a cue played when lever is in goal pos
    defaultGoalCueFreq = 0 # frequency for goal cue - 0 means DC, i.e., turn ON and OFF
    defaultConstForce = 1300 # constant force on lever at stgart of trial that mouse must pull against, as opposed to perturbForce set during a trial a 12 bit value, 0 to 4095
    defaultTrialIsCued = False # True means trials will be started with the start cue; False means mouse starts pulling lever whenever he likes
    """
    Settings for cued trials
    """
    defaultStartCuePin = 27 # GPIO pin to use for a cue when mouse should start a trial, this can be a pulse (freq =0) or a train
    defaultStartCueFreq = 0 # frequency for start cue - 0 means DC, i.e., turn ON and OFF
    defaultStartCueDur = 0.1 # duration in seconds of start cue
    defaultToGoalTime = .25 # mouse has this many seconds from start cue to get lever into goal area, or trial is ended. toGoalTime plus holdTime must be < recordingTime
    defaultTrialTimeout = 0.5 # time in seconds between end of one trial (ended for any reason) and start of the next trial. Lever is rezeroed here
    """
    Settings for uncued trials
    """
    defaultPrePullTime = 0.25 # this many seconds of time before the lever reaches goal position is saved in a circular buffer 


    #pathToData_def = '/home/pi/Documents/' # folder where lever pos files will be saved
    
    @staticmethod
    def about():
        return 'As mice hold a lever in a set angular range, Lever stimulator records lever position and puts torque on the lever by calling ptLeverThread C-module.'
        
    @staticmethod
    def config_user_get (starterDict = {}):
        recordingTime = starterDict.get ('recordingTime', AHF_Stimulator_Lever.defaultRecordingTime)
        response = input('Enter the maximum time in seconds of lever position data that will be recorded per trial(currently {:.2f}): '.format (recordingTime))
        if response != '':
            recordingTime = float (response)

        leverIsReversed = starterDict.get ('leverIsReversed', AHF_Stimulator_Lever.defaultLeverIsReversed)
        response = input ('Is the lever direction reversed ?, (Yes or No, currently {:s}): '.format ('Yes' if leverIsReversed else 'No'))
        if response != '':
            leverIsReversed = True if response [0] == 'y' or response [0] == 'Y' else False

        goalCuePin = starterDict.get ('goalCuePin', AHF_Stimulator_Lever.defaultGoalCuePin)
        response = input('Enter the GPIO pin to use for a cue played whenever lever is in the goal position (currently {:d}): '.format (goalCuePin))
        if response != '':
            goalCuePin = int (response)

        goalCueFreq = starterDict.get ('goalCueFreq', AHF_Stimulator_Lever.defaultGoalCueFreq)
        response = input ('Enter the frequency in Hz to use for the goal cue - 0 turn ON and OFF (currently {:.2f}): '.format (goalCueFreq))
        if response != '':
            goalCueFreq = float (response)

        constForce = starterDict.get ('constForce', AHF_Stimulator_Lever.defaultConstForce)
        response = input ('Enter the constant force applied to the on lever at the start of a trial, from 0 to 4095 (currently {:d}): '.format (constForce))
        if response != '':
            if ( 
            constForce = int (response)
                
        trialIsCued = StarterDict.get ('trialIsCued', AHF_Stimulator_Lever.defaultTrialIsCued)
        response = input ('Do the lever pull trials have a start cue? (yes or no, currently {:.str}): '.format ('Yes' if mybool else 'No'))
        if response != '':
            trialIsCued = True if response [0] == 'y' or response [0] == 'Y' else False
        if trialIsCued:
            
        
        rewardInterval = starterDict.get ('rewardInterval', AHF_Stimulator_Lever.defaultInterval)
        response = input ('Enter the time interval between rewards (currently %.2f seconds): ' % rewardInterval)
        if response != '':
            rewardInterval = float (response)
        starterDict.update({'nRewards' : nRewards, 'rewardInterval' : rewardInterval})
        return starterDict



    def config_user_get (starterDict = {}):

        keyTuple = ('posBufferSize', 'isCued', 'constForce', 'toGoalOrCirc', 'isReversed', 'goalCuePin', 'goalCueFreq','pathToData')
        for key in keyTuple:
            value = input ('Enter a value for ' + key + ':')
            stimDict.update({key : value})

     @staticmethod
    def dict_from_user (stimDict):
        if not 'dataSaveFolder' in stimDict:
            stimDict.update ({'dataSaveFolder' : '/home/pi/Documents/'})

        if not 'decoderReversed' in stimDict:
            stimDict.update ({'decoderReversed' : False})
        if not 'motorPresent' in stimDict:
            stimDict.update ({'motorPresent' : True})
        if not 'motorHasDirection' in stimDict:
            stimDict.update ({'motorHasDirection' : True})
        if not 'motorDirectionPin' in stimDict:
            stimDict.update ({'motorDirectionPin' : 18})
        if not 'startCuePin' in stimDict:
            stimDict.update ({'startCuePin' : 17})
        return super(AHF_Stimulator_Lever, AHF_Stimulator_Lever).dict_from_user (stimDict)
