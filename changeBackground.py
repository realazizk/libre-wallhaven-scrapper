#!/usr/bin/env python2

# Constants
# the delay of changing the background is 10 minutes
DELAY = 0.2
# backgrounds path
MYPATH = '/home/mohamed/back'
# This works on gnome (tested on Mate 1.8)
from os import system
from time import sleep
from os import listdir
from os.path import isfile, join

# An infinite loop (if you want more performance replace True with 1)
while True :
  files = [ f for f in listdir(MYPATH) if isfile(join(MYPATH,f)) ]
  for filename in files :
    print join(MYPATH, filename)
    system('gsettings set org.mate.background picture-filename ' + join(MYPATH, filename))
    sleep(DELAY*60)
