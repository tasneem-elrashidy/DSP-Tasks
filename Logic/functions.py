import numpy as np
import matplotlib as plt
from Logic import signalOperations,pre


def calcOmega(fs,N):
   f=[]
   omega=2*np.pi/(N*fs)
   for i in range(0,N):
      f.append(omega*(i+1))
   return f

def dominantFrequencies(amp,fs):
  out=[]
  f=calcOmega(fs,len(amp))
  for i in range(0,len(amp)):
      if(amp[i]>.5):
         out.append(f[i])
  return out


def modifyAmpPhase(amp,phases,idx,newAmp,newPhase ):
   amp[idx]=newAmp
   phases[idx]=newPhase
   return amp,phases



def removeDC(sig):
   indx,originalsig,amp,phase=signalOperations.oprations.Fouriore("DFT",signal=sig) #dft ver
   amp[0]=0
   phase[0]=0

   indx,originalsig,amp,phase=signalOperations.oprations.Fouriore("IDFT",ampl=amp,phase1=phase) #idft ver
   return indx,originalsig  
  