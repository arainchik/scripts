#!/usr/bin/env python

import os
import sys
import getopt


opt,args = getopt.getopt(sys.argv[1:], "n:")

nFiles = 40
for o,v in opt:
   if o == '-n':
      nFiles = int(v)

if len(args) == 0:
   home = os.path.expanduser("~")
   args = [os.path.join(home,x) for x in["Documents","Pictures","Desktop"]]

for d in args:
    if not  os.path.isdir(d):
       print d, "is not a directory!"
       next
    print "=== procssing", d
    for root,dirs,files in os.walk(d):
        nPict = 0
        for f in files:
           name, ext = os.path.splitext(f)
           if ext.lower() in ['.jpg', '.jpeg', '.gif', '.png']:
              nPict += 1
        if nPict >= nFiles:
           print root, nPict
