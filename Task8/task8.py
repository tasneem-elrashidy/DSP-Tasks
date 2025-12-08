import numpy as np
from Logic import pre, signalOperations

def resampling(sig, l,m):
    N, idx, smp = pre.readFile(sig)
    idx = np.array([float(x.rstrip('f')) for x in idx], dtype=float)
    smp = np.array([float(x.rstrip('f')) for x in smp], dtype=float)

    smp_up=[]
    smp_down=[]
    if not m and l:
        smp_up=np.zeros(len(smp)+((l-1)*(len(smp)-1)))
        smp_up[::l]=smp
        # smp_up=low-pass(smp_up)
        return idx,smp_up
    elif m and not l:
        #smp= low-pass(smp)
        smp_down=smp[::m]
        return idx,smp_down
    elif m and l:
        smp_up=np.zeros(len(smp)+((l-1)*(len(smp)-1)))
        smp_up[::l]=smp
        #smp_up=low-pass(smp_up)
        smp_down=smp_up[::m]
        return idx,smp_down
    else:
        idx,smp=None
        return idx,smp
    
