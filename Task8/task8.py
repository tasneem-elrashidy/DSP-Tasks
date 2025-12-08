import numpy as np
from Logic import pre
import math


def filter(values,type,fs,Δf,attenution,fc=None,f1=None,f2=None):
    Δf2=Δf/fs
    values= np.array(values, dtype=float)
    if (type=="low pass"):
        fp=(fc-Δf2) /fs
        fs=(fc+Δf2) /fs
    elif (type=="high pass"):
        fp=(fc+Δf2)/fs
        fs=(fc+Δf2)/fs
    elif (type=="band pass"):
        fp1 = (f1+Δf2)/fs
        fs1 = (f1-Δf2)/fs
        fp2 = (f2-Δf2)/fs
        fs2 = (f2+Δf2)/fs
    elif (type=="band stop"):
        fp1 = (f1-Δf2)/fs
        fs1 = (f1+Δf2)/fs
        fp2 = (f2+Δf2)/fs
        fs2 = (f2-Δf2)/fs

    if(attenution==21):   # Rectangular
        N = math.ceil(0.9 / Δf)
    if(attenution==31):  # hanning
        N = math.ceil(3.1 / Δf)
    if(attenution==37):  # hamming
        N = math.ceil(3.3 / Δf)
    if(attenution==53):   # blackman
        N = math.ceil(5.5 / Δf)

    if(N%2==0):
        N=N+1
      