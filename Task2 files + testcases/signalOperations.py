import numpy as np
import pre


class oprations:
    # indx1,val1 = pre.readFile("Signal1.txt")
    # indx2,val2 = pre.readFile("Signal2.txt")
    

    def sub(sig1,sig2):
        indx1,val1 = pre.readFile(sig1)
        indx2,val2 = pre.readFile(sig2)
        output=[]
        for i in range(len(indx1)):
            # print(i)
            if(int(indx1[i])==int(indx2[i])):
                
                output.append(int(val1[int(indx1[i])])-int(val2[int(indx2[i])]))
        return indx1,output
    # out=sub(indx1,val1,indx2,val2)
    # Task2Test.SubSignalSamplesAreEqual("Signal1.txt","Signal2.txt",indx1,out)
            

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