#! /usr/bin/env python3
# coding: utf-8
import os
from os import listdir
from os.path import isfile, join

# Execute pyui5c to convert ui to py
# -----------------------------------

uipath = os.getcwd() + "/GuardBits/src/ui/template/"
#print("# Path", uipath)

files = [f for f in listdir(uipath) if isfile(join(uipath, f))]
#print("# Files list :", files)

for f in range(len(files)):
    #print("file : ", files[f])
    file_output = files[f].split(".")
    #print("file output", file_output)
    cmd = "pyuic5 -x " + uipath + files[f] + " -o " + uipath + "../" + file_output[0] + ".py"
    print("cmd", cmd)
    os.system(cmd)
