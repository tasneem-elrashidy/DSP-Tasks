import numpy as np
import matplotlib as plt
from Logic import signalOperations,pre



def dominantFrequencies(amp,fs):
  out=[]
  for i in range(0,len(amp)):
      if(amp[i]>.5):
         omega=2*np.pi/(len(amp*fs))
         out.append(omega*(i+1))
  return out


def modifyAmpPhase(amp,phases,idx,newAmp,newPhase ):
   amp[idx]=newAmp
   phases[idx]=newPhase
   return amp,phases



def removeDC(sig):
   indx,originalsig,amp,phase=signalOperations.oprations.Fouriore("DFT",sig) #dft ver
   amp[0]=0
   phase[0]=0

   indx,originalsig,amp,phase=signalOperations.oprations.Fouriore("IDFT",sig,amp=0,phase=0) #idft ver
   return originalsig  
  