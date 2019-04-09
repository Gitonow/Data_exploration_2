#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:49:03 2019

@author: damienchambon
"""

import sys
import os
import inspect
import glob
import numpy as np
from time import sleep #prevents exceeding data rate limit
from IPython.display import clear_output

def read_stimuli(path):
    # This function reads the different stimuli that a neuron has been tested with
    # path: folder where the different stimuli are located
    arraySpikes = []
    listFiles = os.listdir(path) # dir is your directory path
    number_files = len(listFiles)
    
    print(path) # print the folder being read
    
    for i in range(int(number_files/2)):
        # for each stimuli, read the list of spikes and the file name where it is located
        pathSpike = path + "/spike" + str(i+1)
        pathStim = path + "/stim" + str(i+1)
        listOfSpikes = []
        with open(pathSpike, "rt") as fp:
            # read the array of spikes
            listOfSpikes = ([np.fromstring(line, sep=" ") for line in fp])
        with open(pathStim) as f:
            # read the file name
            nameStim = f.readline()
        arraySpikes.append({"filename": nameStim, "seriesSpikes": listOfSpikes})
    return arraySpikes

def read_area(path):
# This function reads the different neurons of different areas in the brain
# path: folder where the different areas are located
    arrayNeur = []
    for neuronName in os.listdir(path):
        # for each neuron in the folder
        arrayFolder = glob.glob(path+"/"+neuronName+"/"+"*")
        listTypes = []
        for folder in arrayFolder:
            # get the list of the types of stimuli that the neuron was tested with
            listTypes.append(folder[len(path+"/"+neuronName+"/"):])
        arrayStimuli = []
        for t in listTypes:
            # for each type in the list, read the spikes generated and the stimuli tested
            arraySpikes = read_stimuli(path+"/"+neuronName+"/"+t)
            arrayStimuli.append({"type": t, "spikes": arraySpikes})
        arrayNeur.append({"name": neuronName, "stimuli": arrayStimuli})
    return arrayNeur

listAreas = ["Field_L_cells","MLd_cells"] # list of areas to get the data from

currentDir = os.getcwd().replace("/src","")+"/data/crcns-aa1" # find the folder where the data is located

arrayAreas = []
for area in listAreas:
    # read each folder of each area
    arrayNeurons = read_area(currentDir + "/" + area)
    arrayAreas.append({"name": area, "neurons": arrayNeurons})

sleep(1.5) # keep output for some time    
clear_output()
print("Loading of the data done!")