import numpy as np
from Logic import pre
import math
from Task7 import task7

def filter(type,fs,Δf,attenution,fc=None,f1=None,f2=None):
    Δf2=Δf/fs
    if(attenution<=21):   # Rectangular
        N = math.ceil(0.9 / Δf2) # round for the nearest integer then if even make odd
        win = np.ones # window function
    elif(attenution<=44):  # hanning
        N = math.ceil(3.1 / Δf2)
        win = np.hanning
    elif(attenution<=53):  # hamming
        N = math.ceil(3.3 / Δf2)
        win = np.hamming
    else:   # blackman
        N = math.ceil(5.5 / Δf2)
        win = np.blackman

    if(N%2==0):
        N=N+1
    M = (N-1)//2 # calculate center for symetricity
    h = np.zeros(N)
    if (type=="low-pass"):
            fc=(fc+(Δf/2)) /fs
            for n in range(N): # calculate the hd(n): ampulse responses
                if n == M:
                    h[n]=2*fc
                else:
                    i = n - M
                    h[n]=2*fc*math.sin(i*2*math.pi*fc)/(i*2*math.pi*fc)
    elif (type=="high-pass"):
            fc=(fc-(Δf/2))/fs
            for n in range(N):
                if n == M:
                    h[n]=1-2*fc 
                else:
                    i = n - M
                    h[n]=-(2*fc*math.sin(i*2*math.pi*fc)/(i*2*math.pi*fc))
                    
    elif (type=="band-pass"):
            fc1 = (f1-(Δf/2))/fs
            fc2 = (f2+(Δf/2))/fs
            for n in range(N):
                if n == M:
                     h[n]=2*(fc2-fc1)
                else:
                    i = n - M
                    h[n]=(2*fc2*math.sin(i*2*math.pi*fc2)/(i*2*math.pi*fc2))-(2*fc1*math.sin(i*2*math.pi*fc1)/(i*2*math.pi*fc1))
    elif (type=="band-stop"):
            fc1 = (f1+(Δf/2))/fs
            fc2 = (f2-(Δf/2))/fs
            for n in range(N):
                if n == M:
                    h[n]=1-2*(fc2-fc1)
                else:
                    i = n - M
                    h[n]=(2*fc1*math.sin(i*2*math.pi*fc1)/(i*2*math.pi*fc1))-(2*fc2*math.sin(i*2*math.pi*fc2)/(i*2*math.pi*fc2))

    w = win(N) # window arr of length N 
    h = h * w
    indx1=np.arange(-M, M + 1)
    return indx1,h

def resampling(sig, l,m,fs,fc,Δf,attenuation):
    N, idx, smp = pre.readFile(sig)
    idx = np.array([float(x.rstrip('f')) for x in idx], dtype=float)
    smp = np.array([float(x.rstrip('f')) for x in smp], dtype=float)

    smp_up=[]
    smp_down=[]
    if not m and l:
        smp_up=np.zeros(len(smp)+((l-1)*(len(smp)-1)))
        smp_up[::l]=smp
        idx = np.arange(len(smp_up))
        indx1,filtered =filter("low-pass",fs=fs,fc=fc,Δf=Δf,attenution=attenuation)
        indx,filtervalues=task7.convolveSignals(idx,smp_up,indx1,filtered)
        filtervalues=np.array(filtervalues)
        return indx1,filtervalues
    elif m and not l:
        indx1,filtered =filter("low-pass",fs=fs,fc=fc,Δf=Δf,attenution=attenuation)
        indx,filtervalues=task7.convolveSignals(idx,smp,indx1,filtered)
        filtervalues=np.array(filtervalues)
        smp_down=filtervalues[::m]
        return indx1,smp_down
    elif m and l:
        smp_up=np.zeros(len(smp)+((l-1)*(len(smp)-1)))
        smp_up[::l]=smp
        idx = np.arange(len(smp_up))
        indx1,filtered =filter("low-pass",fs=fs,fc=fc,Δf=Δf,attenution=attenuation)
        indx,filtervalues=task7.convolveSignals(idx,smp_up,indx1,filtered)
        filtervalues=np.array(filtervalues)
        smp_down=filtervalues[::m]
        return indx1,smp_down
    else:
        idx,smp=None
        return idx,smp
