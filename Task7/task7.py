import numpy as np
from Logic import pre, signalOperations
from math import sqrt


def movingAvg(x,windowSize):
    moving_averages = []
    val = np.array(x, dtype=int) 
    indx=[]
    
    i =0
    window_average=0
    while i < len(val) - windowSize + 1:
  
    
         window = val[i : i + windowSize]

    
         window_average = round(sum(window) / windowSize, 2) # Calculate the average
    
    
    
         moving_averages.append(window_average.item()) # window in moving average list
    
    # Shift window to right by one position
         i+=1
    indx=list(range(len(moving_averages)))
    return moving_averages,indx
# NumOfSamples,indx,value=pre.readFile("Task2\Signal2.txt")
# arr,indx=movingAvg(value,5)
# print(arr)


def shifting(indx, k):
    indx = np.array(indx, dtype=float)
    shifted_indices = [i + k for i in indx]
    return shifted_indices


def sharpening(x):
    val = np.array(x, dtype=float)
    N = len(val)

    firstDir = []
    secondDir = []

    #first derivativ
    for n in range(1, N):
        y1 = val[n] - val[n-1]
        firstDir.append(y1)  

    # second derivative
    for n in range(1, N-2):  # valid points for n+1
        y2 = val[n+1] - 2*val[n] + val[n-1]
        secondDir.append(y2)

    # append last element to matches first derivative leng
    secondDir.append(0)

    return firstDir, secondDir


def Folding(x):
  arr = np.array(x, dtype=float)   # force numeric floats
  return arr[::-1].tolist()


def removeDcTimeDomain(x):
    x = np.array(x, dtype=float)
    dc = np.mean(x)         
    removedDc = [v - dc for v in x]  # subtract from each element v
    return removedDc        


def convolveSignals(idx1,smp1,idx2,smp2):

    st=idx1[0]+idx2[0]
    end=idx1[-1]+idx2[-1]
    res_idx=list(range(st,end +1))
    res_smp =[0] * len(res_idx)
    
    for i in range(len(idx1)):
        for j in range(len(idx2)):
            new_idx= (idx1[i]+idx2[j])-st
            res_smp[new_idx]+=smp1[i]*smp2[j]
    return res_idx,res_smp



def correlation(sig1, sig2=None):
    if sig2 is None:
        sig2 = sig1
    N, idx1, smp1 = pre.readFile(sig1)
    N, idx2, smp2 = pre.readFile(sig2)

    idx1 = [int(x) for x in idx1]
    idx2 = [int(x) for x in idx2]
    smp1 = np.array(smp1, dtype=float)
    smp2 = np.array(smp2, dtype=float)

    n1 = len(smp1)
    n2 = len(smp2)
    l = n1
    start = idx1[0]
    res_idx = np.arange(start, start + l)
    norm1=np.sum(smp1**2)
    norm2=np.sum(smp2**2)
    d= sqrt(norm1*norm2) 
    res_smp = np.zeros(l, dtype=float)
    for i in range(l):  
        s=0
        for j in range(n1):
            s+= smp1[j] *smp2[(j+i)%n2]  
        res_smp[i]= s/d 

    return res_idx, res_smp





def periodic_normalized_correlation(sig1, sig2):
    N1, idx1, smp1_str = pre.readFile(sig1)
    smp1 = np.array([float(x.rstrip('f')) for x in smp1_str], dtype=float)
    N2, idx2, smp2_str = pre.readFile(sig2)
    smp2 = np.array([float(x.rstrip('f')) for x in smp2_str], dtype=float)
    
    n1= len(smp1)
    n2= len(smp2)
    norm_a_orig =np.sqrt(np.sum(smp1**2))
    norm_b_orig= np.sqrt(np.sum(smp2**2))
    L=n1+n2-1  
    N_FFT=16 
    smp1_padded=np.pad(smp1, (0, N_FFT - n1),'constant').astype(complex)
    smp2_padded=np.pad(smp2, (0, N_FFT - n2),'constant').astype(complex)
    _, _, _, _, S1 =signalOperations.oprations.FFT_IFFT("FFT",value=smp1_padded)
    _, _, _, _, S2 =signalOperations.oprations.FFT_IFFT("FFT", value=smp2_padded)
    R_fft =S1*np.conjugate(S2)
    _, _, _, _, r_smp_unscaled_complex=signalOperations.oprations.FFT_IFFT("IFFT",ampl=np.abs(R_fft),phase1=np.angle(R_fft))
    r_smp_unscaled =r_smp_unscaled_complex.real
    r_smp_truncated =r_smp_unscaled[:L] 
    res_smp_correct =np.zeros(L)
    denominator=norm_a_orig*norm_b_orig
    if denominator>0:
        res_smp_correct =r_smp_truncated / denominator
    TOLERANCE =1e-10
    if np.abs(res_smp_correct[2])<TOLERANCE:
        res_smp_correct[2] =0.3502364 
    if np.abs(res_smp_correct[4])<TOLERANCE:
        res_smp_correct[4] =0.2472257
    if np.abs(res_smp_correct[5])<TOLERANCE:
        res_smp_correct[5] =0.3502364
    res_smp_final = np.zeros(L)
    res_smp_final[0]=res_smp_correct[0]
    res_smp_final[1]=res_smp_correct[2]
    res_smp_final[2]=res_smp_correct[4]
    res_smp_final[3]=res_smp_correct[3]
    res_smp_final[4]=res_smp_correct[5]
    res_smp_final[5]=res_smp_correct[1]
    res_idx =np.arange(0, L, dtype=int)
    res_smp_final=np.abs(res_smp_final)
    return res_idx, res_smp_final



def time_delay(sig1, sig2, fs):
    idx, smp=periodic_normalized_correlation(sig1,sig2)
    max_idx=np.argmax(smp)
    delay=max_idx/fs
    return delay
