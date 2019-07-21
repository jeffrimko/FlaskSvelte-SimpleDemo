# -*- ubuild -*-

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os.path as op
import time
import webbrowser

from auxly.filesys import Cwd
from auxly.shell import start, silent
from qprompt import alert, warn, status
from ubuild import main, menu

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

PROCS = []

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def is_running():
    global PROCS
    return PROCS != []

@menu
def run():
    global PROCS
    if not is_running():
        with Cwd("app"):
            if op.isdir("node_modules"):
                status("Running NPM install...", silent, ["npm install"])
            PROCS.append(start("rollup -w -c rollup.config.js"))
            PROCS.append(start("python app.py"))
            alert("Application running.")
            time.sleep(3)
            browse()
    else:
        warn("App server already running!")

@menu
def browse():
    if not PROCS:
        warn("Application not running!")
    else:
        webbrowser.open("http://localhost:5000/")

@menu
def stop():
    global PROCS
    if is_running():
        for p in PROCS:
            p.stop()
        PROCS = []
        alert("Application stopped.")
    else:
        warn("Application not running!")

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    main(default="r")
