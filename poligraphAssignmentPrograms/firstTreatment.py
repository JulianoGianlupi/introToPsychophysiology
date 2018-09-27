# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 17:23:35 2018

@author: jferrari
"""

#import pandas as pd
#import numpy as np
#import numpy.fft as fft
import csv




direc = 'subjectA/'

fileName = direc + 'subjectA.csv'

time = []
channel1 = []
channel2 = []
channel3 = []
channel5 = []
channel13 = []
channel15 = []

writeTime = open(direc+'time.csv','w')
writeChannel1 = open(direc+'channel1.csv','w')
writeChannel2 = open(direc+'channel2.csv','w')
writeChannel3 = open(direc+'channel3.csv','w')
writeChannel5 = open(direc+'channel5.csv','w')
writeChannel13 = open(direc+'channel13.csv','w')
writeChannel15 = open(direc+'channel15.csv','w')


with open(fileName,'r') as csvdata:
    data = csv.reader(csvdata)
    for i, line in enumerate(data):
       
        if i == 0:
            time.append(line[0])
            channel1.append(line[1])
            channel2.append(line[2])
            channel3.append(line[3])
            channel5.append(line[4])
            channel13.append(line[5])
            channel15.append(line[6])
            
            writeTime.write('%s\n'%(time[i]))
            writeChannel1.write('%s\n'%( channel1[i] ))
            writeChannel2.write('%s\n'%( channel2[i] ))
            writeChannel3.write('%s\n'%( channel3[i] ))
            writeChannel5.write('%s\n'%( channel5[i] ))
            writeChannel13.write('%s\n'%( channel13[i] ))
            writeChannel15.write('%s\n'%( channel15[i] ))
            
            
            
            
        else:
            time.append(float(line[0]))
            channel1.append(float(line[1]))
            channel2.append(float(line[2]))
            channel3.append(float(line[3]))
            channel5.append(float(line[4]))
            channel13.append(float(line[5]))
            channel15.append(float(line[6]))
            
            writeTime.write('%f\n'%(time[i]))
            writeChannel1.write('%f\n'%( channel1[i] ))
            writeChannel2.write('%f\n'%( channel2[i] ))
            writeChannel3.write('%f\n'%( channel3[i] ))
            writeChannel5.write('%f\n'%( channel5[i] ))
            writeChannel13.write('%f\n'%( channel13[i] ))
            writeChannel15.write('%f\n'%( channel15[i] ))








writeTime.close()
writeChannel1.close()
writeChannel2.close()
writeChannel3.close()
writeChannel5.close()
writeChannel13.close()
writeChannel15.close()
