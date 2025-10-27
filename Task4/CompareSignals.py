from Logic import signalOperations, pre,functions

def SignalsAreEqual(TaskName,given_output_filePath,Your_indices,Your_samples):
    expected_indices=[]
    expected_samples=[]
    with open(given_output_filePath, 'r') as f:
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
        # return
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

new_indices, new_signal = functions.removeDC("Task4\DC_component_input.txt")
# excepted_index, excepted_signal = pre.readFile("Task4\DC_component_input.txt")
SignalsAreEqual("removeDC", "Task4\DC_component_output.txt", new_indices, new_signal)

