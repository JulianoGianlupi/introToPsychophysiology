# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 17:23:35 2018

@author: jferrari
"""

import pandas as pd
import numpy as np
import numpy.fft as fft
import csv


def getDataButFirstLine(fileName):
    with open(fileName,'r') as data:
        lines = data.readlines()
    lines = lines[1:]
    fLines = []
    for line in lines:
        fLines.append(float(line))
    
    return np.array(fLines)

samplingRate = 10**-3

direc = 'subjectA/'

fileName = direc + 'subjectA.csv'


timeFile = direc+'time.csv'
channel1File = direc+'channel1.csv'
channel2File = direc+'channel2.csv'
channel3File = direc+'channel3.csv'
channel5File = direc+'channel5.csv'
channel13File = direc+'channel13.csv'
channel15File = direc+'channel15.csv'



timeArray = getDataButFirstLine(timeFile)
channel1Array = getDataButFirstLine(channel1File)
channel2Array = getDataButFirstLine(channel1File)
channel3Array = getDataButFirstLine(channel1File)
channel5Array = getDataButFirstLine(channel1File)
channel13Array = getDataButFirstLine(channel1File)
channel15Array = getDataButFirstLine(channel1File)



frequencies = fft.fftfreq(timeArray.size, d=samplingRate)
fftChannel1 = fft.fft( channel1Array, norm = 'ortho')
fftChannel2 = fft.fft( channel2Array, norm = 'ortho')
fftChannel3 = fft.fft( channel3Array, norm = 'ortho')
fftChannel5 = fft.fft( channel5Array, norm = 'ortho')
fftChannel13 = fft.fft( channel13Array, norm = 'ortho')
fftChannel15 = fft.fft( channel15Array, norm = 'ortho')