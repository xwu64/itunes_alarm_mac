from __future__ import print_function
import commands;
import os;
import random;
import sys;
from datetime import datetime
from time import sleep


def play():
    commands.getoutput("osascript -e 'tell application \"iTunes\" to play'")

if __name__ == "__main__":
    hour,minute = int(sys.argv[1]),int(sys.argv[2])
    print ('alarm at %d:%d' % (hour,minute))
    while not (datetime.now().hour==hour and datetime.now().minute==minute):
        sleep(30)
        print(datetime.now(),end='\r')
        sys.stdout.flush()
    play()
