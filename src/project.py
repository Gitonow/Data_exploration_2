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
import matplotlib.pyplot as plt

##################
## DATA LOADING ##
##################

def read_stimuli(path):
    # This function reads the different stimuli that a neuron has been tested with
    # path: folder where the different stimuli are located
    arraySpikes = []
    listFiles = os.listdir(path) # dir is your directory path
    number_files = len(listFiles)
    
    print(path) # print the folder being read
    
    for i in range(int(number_files/2)):
        # for each stimuli, read the list of spikes and the file name where it is located
        if os.name == 'nt':
            # for Windows
            pathSpike = path + "\\spike" + str(i+1)
            pathStim = path + "\\stim" + str(i+1)
        else:
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
        if neuronName != ".DS_Store":
            # for each neuron in the folder
            if os.name == 'nt':
                # for Windows
                arrayFolder = glob.glob(path+"\\"+neuronName+"\\"+"*")
            else:
                arrayFolder = glob.glob(path+"/"+neuronName+"/"+"*")
                listTypes = []
                for folder in arrayFolder:
                    # get the list of the types of stimuli that the neuron was tested with
                    if os.name == 'nt':
                        # for Windows
                        listTypes.append(folder[len(path+"\\"+neuronName+"\\"):])
                    else:
                        listTypes.append(folder[len(path+"/"+neuronName+"/"):])
                arrayStimuli = []
                for t in listTypes:
                    # for each type in the list, read the spikes generated and the stimuli tested
                    if os.name == 'nt':
                        # for Windows
                        arraySpikes = read_stimuli(path+"\\"+neuronName+"\\"+t)
                    else:
                        arraySpikes = read_stimuli(path+"/"+neuronName+"/"+t)
                    arrayStimuli.append({"type": t, "spikes": arraySpikes})
                    arrayNeur.append({"name": neuronName, "stimuli": arrayStimuli})
    return arrayNeur

listAreas = ["Field_L_cells","MLd_cells"] # list of areas to get the data from

if os.name == 'nt':
    # for Windows
    currentDir = os.getcwd().replace("\\src","")+"\\data\\crcns-aa1" # find the folder where the data is located
else:
    currentDir = os.getcwd().replace("/src","")+"/data/crcns-aa1" # find the folder where the data is located

arrayAreas = []
for area in listAreas:
    # read each folder of each area
    if os.name == 'nt':
        # for Windows
        arrayNeurons = read_area(currentDir + "\\" + area)
    else:
        arrayNeurons = read_area(currentDir + "/" + area)
    arrayAreas.append({"name": area, "neurons": arrayNeurons})

sleep(1.5) # keep output for some time    
clear_output()
print("Loading of the data done!")

#################
## RASTER PLOT ##
#################

import graphics

nb_flatrip = 0
nb_conspecific = 0

nb_flatrip = len(arrayAreas[0]["neurons"][0]["stimuli"][0]["spikes"])
nb_conspecific = len(arrayAreas[0]["neurons"][0]["stimuli"][1]["spikes"])
print(nb_flatrip)
print(nb_conspecific)
n_rows = min(nb_conspecific,nb_flatrip)

fig, axes = plt.subplots(nrows=n_rows, ncols=2, sharex=True, figsize=(15, 9))

# code inspired by https://stackoverflow.com/questions/31006971/setting-the-same-axis-limits-for-all-subplots-in-matplotlib/31007233
for (m,n), subplot in np.ndenumerate(axes):
    subplot.set_xlim(-2000,4000) # sets the xlim between -2000 and 4000

for (m,n), subplot in np.ndenumerate(axes):
    if m == 0:
        if n == 0:
            subplot.set_title("Flatrip (synthetic)",fontsize=20) # sets the title of left column
        else:
            subplot.set_title("Conspecific (authentic)",fontsize=20) # sets the title of left column
    if m == (n_rows-1):
        subplot.set_xlabel("Milliseconds",fontsize=15) # sets the title of left column

listNeurons_field_l_neuron1 = arrayAreas[0]["neurons"][1]["stimuli"]
#print(listNeurons_field_l[0]["stimuli"])

index_stimuli = 0
while index_stimuli < n_rows:
    # flatrip is white noise (synthetic)
    spikes_flatrip = listNeurons_field_l_neuron1[0]["spikes"][index_stimuli]["seriesSpikes"]
    graphics.plot_raster(axes[index_stimuli][0],spikes_flatrip)
    # conspecific is authentic sound
    spikes_conspecific = listNeurons_field_l_neuron1[1]["spikes"][index_stimuli]["seriesSpikes"]
    graphics.plot_raster(axes[index_stimuli][1],spikes_conspecific)
    index_stimuli+=1
    
    
#####################
## DISTANCE MATRIX ##
#####################
import pyspike

