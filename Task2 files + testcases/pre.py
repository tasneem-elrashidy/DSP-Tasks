import PyPDF2
import numpy as np
class signal:
    signalType =0
    isPeridoc=0
    numSamples=0

    x=[]
    y=[]

def readFile(file):
    # if isinstance(file, str):
    #     text = open(file)
    # else:
    #     # For Streamlit uploaded files, decode the content
    #     text = file.getvalue().decode("utf-8").splitlines()
    text=open(file)
    i=0
    s=signal()
    print(text)
    signalInfo=[]
    xfinal=[]
    yfinal=[]
    for lines in text :
       if (i<3):
           signalInfo.append(lines)
           i+=1
           continue
       else :
           line =lines.split(' ',2)
           s.x=line[0]
           s.y=line[1]
           xfinal.append(s.x)
           yfinal.append(s.y)
           

           
    s.signalType=signalInfo[0]
    s.isPeridoc=signalInfo[1]
    s.numSamples=signalInfo[2]

    
    return xfinal,yfinal
       


       
file="E:\Work\DSP\Task2 files + testcases\Signal1.txt"


