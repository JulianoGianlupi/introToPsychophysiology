# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 11:35:03 2018

@author: jferrari
"""

import numpy as np
import numpy.fft as fft
import csv
import pandas as pd

## First I'll get the data from the file,
## separate the ch1 and ch10 signals, and have them in numpy arrays
## I'll measure my time in ms to avoid using floating point numbers. This
## way the index of the array is the time of the signal in ms
fileName = 'HW_data.csv'
chanel1 = []
chanel10 = []

with open(fileName,'r') as csvdata:#opening the file and passing it to lists
    data = csv.reader(csvdata)
    for i, line in enumerate(data):
        if i==0:
            chanel1.append(line[0])
            chanel10.append(line[1])
        else:
            chanel1.append(float(line[0]))
            chanel10.append(float(line[1]))
#converting the list to numpy arrays, excluding the text at the top of the file
npChanel1 = np.array(chanel1[1:])
npChanel10 = np.array(chanel10[1:])
## now I'll do the fourier transform of the signal. numpy's fft normalizes the
## reverse transform by the size of the sample, I prefer the oposite.
ftChanel1 = fft.fft(npChanel1)/npChanel1.size
ftChanel10 = fft.fft(npChanel10)/npChanel10.size

#in order to get the corresponding frequencies to the fft signal numpy has the
# fftfreq function. It takes the size of the original wave sample and the 
#sampling rate as arguments
dt = 10**-3
n = npChanel1.size
freqsChanel1 = fft.fftfreq(n,d=dt)

#even though this frequencies are the same for both signal I did the same for 
#chanel10
dt = 10**-3
n = npChanel10.size
freqsChanel10 = fft.fftfreq(n,d=dt)


## now I'm writing the power of the fft of the signals to files. This will give
## the power spectre. With it the important frequencies are determined.
## Because the original signal is real negative frequencies are redundant.
with open('specter_CH1.csv','w') as file:
    for freq, sig in zip(freqsChanel1,ftChanel1):
        if freq >0:
            file.write('%f,%f\n'%(freq,np.abs(sig)*np.abs(sig)))

with open('specter_CH10.csv','w') as file:
    for freq, sig in zip(freqsChanel10,ftChanel10):
        if freq >0:
            file.write('%f,%f\n'%(freq,np.abs(sig)*np.abs(sig)))
with open('phase_CH1.csv','w') as file:
    for freq, sig in zip(freqsChanel1,ftChanel1):
        if freq >0:
            file.write('%f,%f\n'%(freq,np.angle(sig)))

## after looking at the resulting wave I decided to use the bloodpressure (ch1)
## instead of ECG. As it has less frequencies present.
##
## first I'll clean the signal. To do that I'm copying the values of ch1's fft
## that are in a certain frequency range to another numpy array.
ftBeat = np.zeros(npChanel1.size,dtype = complex)

for i, (freq, sig) in enumerate(zip(freqsChanel1,ftChanel1)):
    if (freq >1  and freq<2) or (freq <-1  and freq>-2):
        #here I'm multiplying by the sample size because I divided by it before
        ftBeat[i] = complex(sig)*npChanel1.size 
## now I'll do the reverse transform. I get the real part because any imaginary
## number here is result of floating point errors (indeed they were in the 
## order of 10^-22)
beat = fft.ifft(ftBeat).real

#writing the clean heart beat to a file
with open('cleanHeartBeat.csv','w') as file:
    for p in beat:
        file.write('%f\n'%(p))


beatSD =np.std(beat)#im
pulseMax=0       
beatsList = [['Time (ms)','Pressure (mmHg) - cleaned signal']] 
with open('heartPulses.csv','w') as file:
    for i, p in enumerate(beat):
        if p>.75*beatSD:
            pulseMax = max(pulseMax,p)
            timeOfPulse = i
        else:
            if pulseMax !=0:
                beatsList.append([timeOfPulse,pulseMax])
                file.write('%i,%f\n'%(timeOfPulse,pulseMax))
            pulseMax = 0
            
beatsDF = pd.DataFrame(beatsList)

beatsDF.to_latex('beatsTable.txt')




