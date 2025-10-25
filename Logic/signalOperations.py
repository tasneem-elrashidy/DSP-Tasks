import numpy as np
from Logic import pre
import math

class oprations:
    # indx1,val1 = pre.readFile("Signal1.txt")
    # indx2,val2 = pre.readFile("Signal2.txt")
    # indx1, val1 = pre.readFile("/home/fatimakhalid/Desktop/DSP-Tasks/Task3/Quan1_input.txt")
    # indx2, val2 = pre.readFile("/home/fatimakhalid/Desktop/DSP-Tasks/Task1/input/Signal2.txt")


    def sub(sig1,sig2):
        indx1,val1 = pre.readFile(sig1)
        indx2,val2 = pre.readFile(sig2)
        output=[]
        for i in range(len(indx1)):
            # print(i)
            if(int(indx1[i])==int(indx2[i])):
                
                output.append(int(val1[int(indx1[i])])-int(val2[int(indx2[i])]))
        return indx1,output
    # index,out=sub("/home/fatimakhalid/Desktop/DSP-Tasks/Task1/input/Signal1.txt","/home/fatimakhalid/Desktop/DSP-Tasks/Task1/input/Signal2.txt")
    # Task2Test.SubSignalSamplesAreEqual("/home/fatimakhalid/Desktop/DSP-Tasks/Task1/input/Signal1.txt","/home/fatimakhalid/Desktop/DSP-Tasks/Task1/input/Signal2.txt",indx1,out)
    # print(out)        

    def add(sig1,sig2):
        indx1,val1 = pre.readFile(sig1)
        indx2,val2 = pre.readFile(sig2)
        output=[]
        for i in range(len(indx1)):
            # print(i)
            if(int(indx1[i])==int(indx2[i])):
                
                output.append(int(val1[int(indx1[i])])+int(val2[int(indx2[i])]))
        return indx1,output
    # out=add(indx1,val1,indx2,val2)
    # # print(out)
    

    def square(sig1):
        indx,val = pre.readFile(sig1)
        out=[]
        for i in range(len(val)):
            out.append(int(val[i])**2)
        return indx,out
    # out=sq(val1)
    # print(out)


    def muli(sig1,const):
        indx1,val = pre.readFile(sig1)
        out=[]
        for i in range(len(val)):
            out.append(int(val[i])*const)
        return indx1,out
    # out=muli(val1,5)
    # print(out)
    
    def acc(sig1):
        indx,val = pre.readFile(sig1)
        output=[0]
        
        for i in range(len(val)):
            if i!=0:
                a=int(val[i])+output[i-1]
                output.append(a)
        return indx,output
    # out=acc(val1)
    # print(out)

    def normZeroOne(sig1):
        indx,val = pre.readFile(sig1)
        out=[]
        minval=int(val[0])
        maxval=int(val[1000])
        rang=maxval-minval
        
        for i in range(len(val)):
            out.append((int(val[i])-minval)/(rang))
        return indx,out
    # out=norm(val2)
    # print(out)

    def normOneToOne(sig1):
        indx,val = pre.readFile(sig1)
        out=[]
        minval=int(val[0])
        maxval=int(val[1000])
        rang=maxval-minval
        
        for i in range(len(val)):
            out.append(((int(val[i])-minval)/(rang)*2)-1)
        return indx,out
    # out=normOneToOne(val1)
    # print(out)

    def bitquantization(signal,bits):
        numSamples,index,signalVal = pre.quantizationFile(signal)
        Quantized=[]
        encodedval=[]
        signal_array = np.array(signalVal)
        converyed_signals= signal_array.astype(float)
        
        minval=min(converyed_signals)
        maxval=max(converyed_signals)
        rang=maxval-minval
        levels=2**bits
        delta=rang/levels
        
        for i in range(int(numSamples)):
         levelIndex = math.floor((converyed_signals[i] - minval) / delta) # level number for which sampe belongs to
         levelIndex = min(levelIndex, levels - 1) # for large values to equal large number in range
         binary_code = format(levelIndex, f'0{int(bits)}b') #encoding level number 
         encodedval.append(binary_code)
         Quantized.append(round((minval + (levelIndex + 0.5) * delta),4))
        return Quantized,encodedval
        
    # out,encodedvalue=bitquantization("/home/fatimakhalid/Desktop/DSP-Tasks/Task3/Quan1_input.txt",8)
    # print(out,encodedvalue)

    def levelquantization(signal,levels):
        numSamples,index,signalVal = pre.quantizationFile(signal)
        Quantized=[]
        encodedval=[]
        errorlist=[]
        intervals=[]
        signal_array = np.array(signalVal)
        converyed_signals= signal_array.astype(float)
        
        minval=min(converyed_signals)
        maxval=max(converyed_signals)
        rang=maxval-minval
        delta=rang/levels
        bits=math.log2(levels)


        for i in range(int(numSamples)):
         levelIndex = math.floor((converyed_signals[i] - minval) / delta) # level number for which sampe belongs to
         levelIndex = min(levelIndex, levels - 1) # for large values to equal large number in range
         intervals.append(levelIndex+1)
         
         binary_code = format(levelIndex, f'0{int(bits)}b') #encoding level number 
         encodedval.append(binary_code)
         Quantized.append(round((minval + (levelIndex + 0.5) * delta),4))
         errorlist.append(round(Quantized[i]-converyed_signals[i],3))
        return intervals,Quantized,encodedval,errorlist
        
    # intervals,quantized,encodedvalue,errorlist=levelquantization("/home/fatimakhalid/Desktop/DSP-Tasks/Task3/Quan2_input.txt",4)
    # print(intervals)