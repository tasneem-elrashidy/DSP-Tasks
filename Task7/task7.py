import numpy as np
from Logic import pre
import math


def movingAvg(x,windowSize):
    moving_averages = []
    val = np.array(x, dtype=int) # convertit into an array of int
    indx=[]
    # Loop through the array to consider
    # every window of size 3
    i =0
    window_average=0
    while i < len(val) - windowSize + 1:
  
    # Store elements from i to i+window_size
    # in list to get the current window
         window = val[i : i + windowSize]

    # Calculate the average of current window
         window_average = round(sum(window) / windowSize, 2)
    
    # Store the average of current
    # window in moving average list
         moving_averages.append(window_average.item())
    
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
