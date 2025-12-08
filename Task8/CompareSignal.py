from Logic import signalOperations, pre,functions
from Task8 import task8
from Task7 import task7
import numpy as np

def Compare_Signals(file_name,Your_indices,Your_samples):      
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
    print("Current Output Test file is: ")
    print(file_name)
    print("\n")
    if (len(expected_samples)!=len(Your_samples)) and (len(expected_indices)!=len(Your_indices)):
        print("Test case failed, your signal have different length from the expected one")
        print(len(expected_samples),len(Your_samples))
        return
    for i in range(len(Your_indices)):
        if(Your_indices[i]!=expected_indices[i]):
            print("Test case failed, your signal have different indicies from the expected one")
            return
    for i in range(len(expected_samples)):
        if abs(Your_samples[i] - expected_samples[i]) < 0.2:
            continue
        else:
            print("Test case failed, your signal have different values from the expected one") 
            return
    print("Test case passed successfully")

# test-case 1 passed
# indx,filtered = task8.filter("low-pass",8000,500,50,fc=1500)
# Compare_Signals("Task8/FIR test cases/Testcase 1/LPFCoefficients.txt",indx,filtered)


# test-case 2
# NumOfSamples,index,value= pre.readFile("Task8/FIR test cases/Testcase 2/ecg400.txt")
# indx1,filtered = task8.filter("low-pass",8000,500,50,fc=1500)
# value = [float(v) for v in value]
# index = [int(i) for i in index]
# indx,filtervalues=task7.convolveSignals(index,value,indx1,filtered)
# filtervalues=np.array(filtervalues)
# print(filtervalues)
# Compare_Signals("Task8/FIR test cases/Testcase 2/ecg_low_pass_filtered.txt",indx,filtervalues)


# test-case 3 passed
# indx,filtered = task8.filter("high-pass",8000,500,70,fc=1500)
# Compare_Signals("Task8\FIR test cases\Testcase 3\HPFCoefficients.txt",indx,filtered)


# test-case 4 
# NumOfSamples,index,value=pre.readFile("Task8\FIR test cases\Testcase 3\Filter Specifications.txt")
# indx,filtered = task8.filter("high-pass",8000,500,70,fc=1500)
# Compare_Signals("Task8\FIR test cases\Testcase 3\HPFCoefficients.txt",indx,filtered)


# test-case 5 passed
# indx,filtered = task8.filter("band-pass",1000,50,60,f1=150,f2=250)
# Compare_Signals("Task8\FIR test cases\Testcase 5\BPFCoefficients.txt",indx,filtered)


# test-case 6
# NumOfSamples,index,value=pre.readFile("Task8\FIR test cases\Testcase 5\Filter Specifications.txt")
# indx,filtered = task8.filter("band-pass",1000,50,60,f1=150,f2=250)
# Compare_Signals("Task8\FIR test cases\Testcase 5\BPFCoefficients.txt",indx,filtered)


# test-case 7 passed
# indx,filtered = task8.filter("band-stop",1000,50,60,f1=150,f2=250)
# Compare_Signals("Task8\FIR test cases\Testcase 7\BSFCoefficients.txt",indx,filtered)

# test-case 8 
# NumOfSamples,index,value=pre.readFile("Task8\FIR test cases\Testcase 7\Filter Specifications.txt")
# indx,filtered = task8.filter("band-stop",1000,50,60,f1=150,f2=250)
# Compare_Signals("Task8\FIR test cases\Testcase 7\BSFCoefficients.txt",indx,filtered)

# resampling - test-case 1
idx,smp=task8.resampling(r"Task8\Sampling test cases\Testcase 1\ecg400.txt",0,2,8000,1500,500,50)
Compare_Signals(r"Task8\Sampling test cases\Testcase 1\Sampling_Down.txt",idx,smp)
# print(smp)

# resampling - test-case 2
idx,smp=task8.resampling(r"Task8\Sampling test cases\Testcase 2\ecg400.txt",l=3,m=0,fs=8000,fc=1500,Δf=500,attenuation=50)
Compare_Signals(r"Task8\Sampling test cases\Testcase 2\Sampling_Up.txt",idx,smp)
# print(smp)

# resampling - test-case 3
idx,smp=task8.resampling(r"Task8\Sampling test cases\Testcase 3\ecg400.txt",l=3,m=2,fs=8000,fc=1500,Δf=500,attenuation=50)
Compare_Signals(r"Task8\Sampling test cases\Testcase 3\Sampling_Up_Down.txt",idx,smp)
# print(idx)
