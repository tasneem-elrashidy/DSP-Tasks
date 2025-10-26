import PyPDF2
import numpy as np
class signal:
    signalType =0
    isPeridoc=0
    numSamples=0

    x=[]
    y=[]

def readFile(file):
    if isinstance(file,str):
        with open(file,'r') as f:
            lines=f.read().splitlines()
    else:
        lines=file.getvalue().decode("utf-8").splitlines() 
    i = 0
    s=signal()
    signalInfo = []
    xfinal = []
    yfinal = []

    for line in lines:
        if i<3:
            signalInfo.append(line)
            i+=1
            continue
        else:
            l=line.split(' ',2)
            s.x=l[0]
            s.y=l[1]
            xfinal.append(s.x)
            yfinal.append(s.y)
    s.signalType=signalInfo[0]
    s.isPeridoc=signalInfo[1]
    s.numSamples=signalInfo[2]

    return signalInfo[2],xfinal, yfinal

# def quantizationFile(file):
#     if isinstance(file,str):
#         with open(file,'r') as f:
#             lines=f.read().splitlines()
#     else:
#         lines=file.getvalue().decode("utf-8").splitlines() 
#     i = 0
#     s=signal()
#     signalInfo = []
#     xfinal = []
#     yfinal = []

#     for line in lines:
#         if i<3:
#             signalInfo.append(line)
#             i+=1
#             continue
#         else:
#             l=line.split(' ',2)
#             s.x=l[0]
#             s.y=l[1]
#             xfinal.append(s.x)
#             yfinal.append(s.y)
#     s.signalType=signalInfo[0]
#     s.isPeridoc=signalInfo[1]
#     s.numSamples=signalInfo[2]

#     return signalInfo[2],xfinal, yfinal





       
# file="E:\Work\DSP\Task2 files + testcases\Signal1.txt"


