# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:39:27 2018

@author: juliano

This takes a numpy array of signal strengh and signal frequency,
 a frequency to block/pass/lowpass/highpass, and a variance for the 
 blocked/passed frequency. 

Block: Returns the numpy array with that frequency eliminated by multiplying
the signal by 1- exp(- (x-frequency)^2 / 2var^2) / var sqrt(2pi).

Pass: Returns the numpy array with only that frequency by multiplying
the signal by exp(- (x-frequency)^2 / 2var^2) / var sqrt(2pi).

HighPass: Returns the numpy array multiplied 
by exp(- (x-frequency)^2 / 2var^2) / var sqrt(2pi) up to the cutoff frequency.

LowPass: Returns the numpy array multiplied 
by exp(- (x-frequency)^2 / 2var^2) / var sqrt(2pi) after the cutoff frequency.
"""



import numpy as np


class gaussianFilters:
    def __init__(self,signal,signalFreqs,frequency,variance):
        
        self.signal = signal
        
        self.signalFreqs = signalFreqs
        
        self.lenght = len(self.signalFreqs)
             
        self.frequency = frequency
        
        self.variance = variance
        
        self.gaussian = np.zeros(self.lenght)        
        for i in range(len(self.gaussian)):
            self.gaussian[i] = self.gaussianFunc(self.signalFreqs[i])
        
    def gaussianFunc(self,x):
        freq = self.frequency
        var = self.variance
        exponent = - ((x - freq)**2)/(2*var*var)
        g = np.exp(exponent)/(var*np.sqrt(2*np.pi))
        return g
        
    
    def gaussianBlock(self):
        self.blockGauss = np.zeros(self.lenght)
        self.blockedSignal = np.zeros(self.lenght)
        for i, x in enumerate(self.gaussian):
            self.blockGauss[i] = 1 - x
        self.blockedSignal[:] = self.blockGauss[:]*self.signal[:]
        #print(blockGauss)
        return self.blockedSignal#self.signal[:]
    
    def gaussianPass(self):
        self.passedSignal = np.zeros(self.lenght)
        self.passedSignal[:] = self.gaussian[:]*self.signal[:]
        return self.passedSignal
    
    def gaussianHighPass(self):
        self.returnSignal = np.zeros(self.lenght)
        for i, f in enumerate(self.signalFreqs):
            if f>self.frequency:
                self.returnSignal[i] = self.signal[i]
            else:
                self.returnSignal[i] = self.signal[i]*self.gaussian[i]
        return self.returnSignal
    
    def gaussianLowPass(self):
        self.returnSignal = np.zeros(self.lenght)
        for i, f in enumerate(self.signalFreqs):
            if f<self.frequency:
                self.returnSignal[i] = self.signal[i]
            else:
                self.returnSignal[i] = self.signal[i]*self.gaussian[i]
        return self.returnSignal