import logging
import os
import random
import time
import sys

from screen import Screen
from scorer import Scorer
from trigger import Trigger
from psychopy import core, event, sound
from psychopy.hardware import keyboard

from datalog import Datalog
from config.configPVT import CONF

#########################################################################

######################################
# Initialize screen, logger and inputs
logging.basicConfig(
    level=CONF["loggingLevel"],
    format='%(asctime)s-%(levelname)s-%(message)s',
)  # This is a log for debugging the script, and prints messages to the terminal

screen = Screen(CONF)

datalog = Datalog(OUTPUT_FOLDER=os.path.join(
    'output', CONF["task"]["name"]), CONF=CONF)  # This is for saving data

kb = keyboard.Keyboard()

mainClock = core.MonotonicClock()  # starts clock for timestamping events

Alarm = sound.Sound(os.path.join('sounds', CONF["instructions"]["alarm"]),
                    stereo=True)
scorer = Scorer()

trigger = Trigger(CONF["trigger"]["serial_device"],
                  CONF["trigger"]["labels"], CONF["sendTriggers"])

logging.info('Initialization completed')

#########################################################################


def quitExperimentIf(toQuit):
    "Quit experiment if condition is met"

    if toQuit:

        scorer.getScore()
        logging.info('quit experiment')
        trigger.send("Quit")
        trigger.reset()
        sys.exit(2)


def onFlip():
    "Send and restart clocks as soon as screen changes"
    trigger.send("Stim")
    kb.clock.reset()
    datalog["startTime"] = mainClock.getTime()
