#!/usr/bin/env python

import sys, os, re, subprocess
import autoProcessTV ,ConfigParser

dir = None
hash = ""
    
for item in sys.argv:
    if os.path.isdir(item):
        dir = os.path.abspath(item)
    if os.path.isfile(item):
        dir = os.path.abspath(item)
    elif not os.path.isfile(item):
        hash = item
    
autoProcessTV.processEpisode(dir)
