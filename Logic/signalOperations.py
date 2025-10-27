import numpy as np
from Logic import pre
import math

class oprations:

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

    def normZeroOne(sig1=None,values=None):
        out = []
        indx = []
        if values is not None:
           val = np.array(values, dtype=float)
        if sig1 is not None:  
           N,indx,val = pre.readFile(sig1) 
        val = np.array(val, dtype=float)     
        out=[]
        minval=val.min()
        maxval=val.max()
        rang=maxval-minval
        
        for i in range(len(val)):
             out.append(((val[i])-minval)/(rang))
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
    def quantization(signal, bits=None, levels=None):
        if bits is None and levels is None:
            raise ValueError("You must specify either 'bits' or 'levels'.")

        # Derive levels from bits if necessary
        if bits is not None:
            levels = 2 ** bits
        else:
            bits = int(math.log2(levels))

        # Use the preprocessor's readFile method
        numSamples, index, signalVal = pre.readFile(signal)
        signal_array = np.array(signalVal, dtype=float)

        minval = np.min(signal_array)
        maxval = np.max(signal_array)
        rang = maxval - minval
        delta = rang / levels

        Quantized = []
        Encoded = []
        Intervals = []
        ErrorList = []

        for i in range(int(numSamples)):
            levelIndex = math.floor((signal_array[i] - minval) / delta)
            levelIndex = min(levelIndex, levels - 1)

            Intervals.append(levelIndex + 1)

            binary_code = format(levelIndex, f'0{int(bits)}b')
            Encoded.append(binary_code)

            q_val = round(minval + (levelIndex + 0.5) * delta, 4)
            Quantized.append(q_val)
            ErrorList.append(round(q_val - signal_array[i], 3))

        return {
            "intervals": Intervals,
            "quantized": Quantized,
            "encoded": Encoded,
            "error": ErrorList
        }
   # intervals,quantized,encodedvalue,errorlist=levelquantization("/home/fatimakhalid/Desktop/DSP-Tasks/Task3/Quan2_input.txt",4)
   # print(intervals)

    def Fouriore(Type,amp=None,phase=None):

     originalSignal=[]
     phases=[]
     amplitued=[]
     index=[]
     if(Type=="DFT"):
      NumOfSamples,indx,value=pre.readFile(signal)
      N = int(NumOfSamples)
      n = np.array(indx, dtype=int) # convertit into an array of int
      k = n.reshape((N, 1)) # reshapes the 1D array n into a column vector (N rows and 1 column.)

      value=np.array(value, dtype=float)
      e = np.exp(-2j * np.pi * k * n / N)
      X_k = np.zeros_like(k, dtype=np.complex128) # setting the array X_k = 0real+0imag to fill its values
      X_k = np.dot(e, value) # dot product (same as 2 for loops for summing the x[k] in n)
      amplitued=np.abs(X_k) # calculate the amplitude
      phases=np.angle(X_k) # calculate the tan inverse 


     else: # if IDFT
      NumOfSamples,amp,phase=pre.readFile(signal)
      if amp is None and phase is None:
         amp=0
         phase=0
      else:
        amp = np.array([float(x.rstrip('f')) for x in amp], dtype=float) # convert to float array
        phase=np.array([float(x.rstrip('f')) for x in phase], dtype=float)  # convert to float array
      
      N = int(NumOfSamples)
      n = np.arange(N)
      index=n
      k = n.reshape((N, 1)) # reshapes the 1D array n into a column vector (N rows and 1 column.)

      X_k = amp * np.exp(1j*phase)
      e = np.exp(2j * np.pi * k * n / N)
      X_k = np.dot(e, X_k)/N # dot product
      originalSignal= np.rint(X_k.real).astype(int) # round to nearest number

     return index,originalSignal,amplitued,phases
# indx,originalSignal,phases,amplitued=oprations.Fouriore("IDFT","Task4\\input_Signal_IDFT,A,phase.txt")
# print(originalSignal)
#    def CalcFrequencies(samplingFreq,phase,amplitude):