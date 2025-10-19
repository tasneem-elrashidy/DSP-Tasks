import numpy as np

class SignalGenerator:
    def generate(type,amp, freq, fs, theta):
        
        n = np.arange(0, fs, 1)
        ang=(2*np.pi*freq*n)/fs+theta
        
        x= np.array([])
        if type=="sin":
            x=amp*np.sin(ang)
        elif type=="cos":  
            x= amp*np.cos(ang)
        else:
            print("Signal type must be sin or cos!!")
            
        return n,x
    