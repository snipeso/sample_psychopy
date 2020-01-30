# sample_psychopy

The starting point for any experiments I want to create in psychopy.

## Design

This is the starting point of all psychopy based experiments.

## Scripts

### main

This file dictates what each experiment really does, what it shows when, etc.

### config

This is a folder with multiple configurations. configSession.json (needs to be called this) should include any information that is not task specific and could be shared with different tasks (and thus saved somewhere else, like a common folder). configSample.py updates the json with task specific-configurations, as well as implements version-specific parameters. updateConfig is a class that processes the json file, and applies pythony things to it, as well as lets you update content, like the triggers.

Versions
In the json, specify a version; then the python configuration file will select the appropriate values based on the specified version. There must always be a "main" version, and then whatever else you want. I use "debug" for making a small window, and "demo" for showing experiments with shorter timing.

### screen

This is a class that takes care of ALL screen related activity, initializing all the visual components, and then providing clean functions for showing different setups

### datalog

This is a class that takes care of saving the data to an output folder, grouped by day. It saves the configuration in its entirety, and a second file that saves a dictionary with anything the main.py file dumps into it.

### trigger

This is a class that takes care of all the technical details of sending triggers.

### scorer

This is optional, it lets you easily keep track of participant performance, so that you can spit out the result in the terminal at the end, or whenver you quit.

## Setup Instructions (Linux)

### Setting up env

Copy local env:

1. Run within current folder: `cp {env} .`
2. Run `pyvenv env`

Make env (recommended into a general projects folder so can use for other experiments):

1. Create in folder `pyvenv psychopyEnv`
2. Activate with `source psychopyEnv/bin/activate`
3. Install requirements: `pip install -r requirements.txt`

If psychopy has problems, just download all of these:

`sudo apt install python3-dev libx11-dev libasound2-dev portaudio19-dev libusb-1.0-0-dev libxi-dev build-essential libgtk-3-dev gtk3.0 python3-wxgtk3.0`

and if you need more:

`sudo apt-get install libjpeg-dev libtiff-dev libgtk2.0-dev libsdl1.2-dev freeglut3 freeglut3-dev libnotify-dev libgstreamerd-3-dev`

Create requirements:

`pip freeze > requirements.txt`

### Give account access to ports for triggers (and for shortcuts ?)

1. Add you user to the riht group: `sudo uermod -a -G dialout $USER`
2. Identify the name of the port, and save as "serial_device" in CONF: `ls /dev/tty{USB,ACM}*`, only one should show up.

### Create starting shortcut

This is needed so you can start the experiment from wherever in the terminal.

1. Make sure there is the file exp-sample
2. Run `code ~/.bashrc` in terminal
3. Add at the bottom: `export PATH=~/Projects/sample_psychopy/:$PATH` and save
4. Give permission to use that file: `chmod +x Projects/sample_psychopy/exp-sample`
5. Start a new window to see if it worked

Then from a new terminal, you can run directly `exp-match2sample` and it starts!

### Get monitor settings

#### Linux

1. Run `xrandr` in terminal

### setting up pupillometry

You need a seperate computer and a common network for both stimulus and eye tracking computer

1. make sure you have all the pupillometry software
2. Start up Pupil Capture, and make sure you have the "Annotation Capture" extension
3. Find out what is the pupillometry computer IP address:
   a. go to the little wifi menu in the bottom right corner
   b. on the network you're in, click on "Properties" and scroll down to where the ip address is listed
4. copy the IP address to the main configurations file

Whenever recording pupillometry, just make sure Pupil Capture is open

## How to run

### Linux

From within folder:

1. Enter psychopy environment in terminal, either using shortcut `psyEnv` or `source ~/Projects/psychopyEnv/bin/activate`
2. Then run with `python3 main.py`

From anywhere (needs to setup shortcut first):

1. Configure participant and session: `export participant=P00 session=0`
2. Run specific task: `exp-sample`

### Windows

1. Open psychopy
2. Open visual studio code (or similar)
   - modify participant ID and session in the configSession.json, save
3. Open "mainSample.py" for this experiment
4. Click the green run button

## How to check that everything works

### How to measure reaction time accuracy (just python vs reality)

1. Set the stimulus position to always be 0.0, and the color to be blue, and the ISI (inter stimulus interval) is between 1 and 2
2. on an iphone 6 or later (but better if less than XR), download the app "is it snappy"
3. start recording just before starting the task, such that the key you will press and the screen are both in view
4. play the task at least 20 trials
5. on the app, reveiw the video
   - go frame by frame until you reach the first frame in which the stimulus appears
   - mark this as "input" in the bottom left
   - continue until the first frame in which you visibily see the key being pressed down, mark this as "output"
     the app will calculate the difference in miliseconds. repeat until desired.
6. open the output, identify the corresponding reaction times, subtract, and determine the average difference between filmed RTs and computer recorded RTs

## Credits:

Sounds:

- horn.wav: https://freesound.org/people/mcpable/sounds/131930/

# TODO: remove psychtoobox
