#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import signalOperations


def ReadSignalFile(file_name):
    expected_indices=[]
    expected_samples=[]
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L=line.strip()
            if len(L.split(' '))==2:
                L=line.split(' ')
                V1=int(L[0])
                V2=float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
    return expected_indices,expected_samples


# In[ ]:


def AddSignalSamplesAreEqual(userFirstSignal,userSecondSignal,Your_indices,Your_samples):
    if(userFirstSignal=='Signal1.txt' and userSecondSignal=='Signal2.txt'):
        file_name="Signal1+signal2.txt" # write here path of signal1+signal2
    elif(userFirstSignal=='Signal1.txt' and userSecondSignal=='Signal3.txt'):
        file_name="signal1+signal3.txt" # write here path of signal1+signal3
    expected_indices,expected_samples=ReadSignalFile(file_name)          
    if (len(expected_samples)!=len(Your_samples)) and (len(expected_indices)!=len(Your_indices)):
        print("Addition Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if(int(Your_indices[i])!=expected_indices[i]):
            print("Addition Test case failed, your signal have different indicies from the expected one") 
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Addition Test case failed, your signal have different values from the expected one") 
            return
    print("Addition Test case passed successfully")

# idx,sapmles=signalOperations.oprations.add("Signal1.txt","Signal2.txt")
# AddSignalSamplesAreEqual("Signal1.txt","Signal2.txt",idx,sapmles)


# In[ ]:


def MultiplySignalByConst(User_Const,Your_indices,Your_samples):
    if(User_Const==5):
        file_name="MultiplySignalByConstant-Signal1 - by 5.txt" # write here path of MultiplySignalByConstant-Signal1 - by 5.txt
    elif(User_Const==10):
        file_name="MultiplySignalByConstant-signal2 - by 10.txt" # write here path of MultiplySignalByConstant-Signal2 - by 10.txt
        
    expected_indices,expected_samples=ReadSignalFile(file_name)      
    if (len(expected_samples)!=len(Your_samples)) and (len(expected_indices)!=len(Your_indices)):
        print(f"Multiply by {User_Const} Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(Your_indices)):
        if(int(Your_indices[i])!=expected_indices[i]):
            print(f"Multiply by {User_Const} Test case failed, your signal have different indicies from the expected one") 
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print(f"Multiply by {User_Const}  Test case failed, your signal have different values from the expected one") 
            return
    print(f"Multiply by {User_Const}  Test case passed successfully")
idx,samples=signalOperations.oprations.muli("Signal1.txt",5)
MultiplySignalByConst(5,idx,samples)
# idx,samples=signalOperations.oprations.muli("Signal2.txt",10)
# MultiplySignalByConst(10,idx,samples)

# In[ ]:


#TaskName => choose it (string explain the name of task like (adding sig1+sig2,subtracting, .... etc.))
#output_file_name => output file path (output file given by TAs)
# Your_indices => your indices list from your code (generated/calculated by you)
# Your_samples => your samples list from your code (generated/calculated by you)
def SignalSamplesAreEqual(TaskName,output_file_name,Your_indices,Your_samples):
    expected_indices=[]
    expected_samples=[]
    with open(output_file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L=line.strip()
            if len(L.split(' '))==2:
                L=line.split(' ')
                V1=int(L[0])
                V2=float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break
    if (len(expected_samples)!=len(Your_samples)) and (len(expected_indices)!=len(Your_indices)):
         print(TaskName+" Test case failed, your signal have different length from the expected one")
         return
    for i in range(len(Your_indices)):
        if(Your_indices[i]!=expected_indices[i]):
            print(TaskName+" Test case failed, your signal have different indicies from the expected one") 
            return             
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print(TaskName+" Test case failed, your signal have different values from the expected one") 
            return
    print(TaskName+" Test case passed successfully")


