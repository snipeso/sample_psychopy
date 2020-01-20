# sample_psychopy

The starting point for any experiments I want to create in psychopy.

## design

### main.py

This file dictates what each experiment really does, what it shows when, etc.

### config

This is a folder with multiple configurations, some of which are additions to the main configuration configSession.py, which should be identical for all tasks in the same experiment.

Specifies all the variables. ALL of them! They are saved in a dictionary, approximately grouping things by theme.

### screen.py

This is a class that takes care of ALL screen related activity, initializing all the visual components, and then providing clean functions for showing different setups

### datalog.py

This is a class that takes care of saving the data to an output folder, grouped by day. It saves the configuration in its entirety, and a second file that saves a dictionary with anything the main.py file dumps into it.

### trigger

This is a class that takes care of all the technical details of sending triggers.

### scorer

This is optional, it lets you easily keep track of participant performance, so that you can spit out the result in the terminal at the end, or whenver you quit.

## Setup Instructions (Linux)

### Setting up env

Copy local env:

1. run within current folder: `cp {env} .`
2. run `pyvenv env`

Make env (recommended into a general projects folder so can use for other experiments):

1. create in folder `pyvenv psychopyEnv`
2. activate with `source psychopyEnv/bin/activate`
3. install requirements: `pip install requirements.txt`

### Create starting shortcut

This is needed so you can start the experiment from wherever in the terminal.

1. make sure there is the file exp-sample
   run `code ~/.bashrc` in terminal
2. add at the bottom: `export PATH=~/Projects/match2sample/:$PATH`
3. Important 4th step I can't remember

Then from a new terminal, you can run directly `exp-match2sample` and it starts!

## How to run

### Linux

From within folder:

1. enter psychopy environment in terminal, either using shortcut `psyEnv` or `source ~/Projects/psychopyEnv/bin/activate`
2. then run with `python3 main.py`

From anywhere (needs to setup shortcut first):

1. Configure participant and session: `export participant=P00 session=0`
2. Run specific task: `exp-sample`

### Windows (booo)

1. open psychopy
2. open visual studio code (or similar)
   - modify participant ID and session, save
3. open "main.py" for this experiment
4. click the green run button

## TODO:

- redo after everything is working!

Specific components:

- triggers (script, computer permission, instructions for finding port)
- executing from terminal (file + instructions)
- requirements
- monitor settings
- output and datalog (script destination folder)
