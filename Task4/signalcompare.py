import math
from Logic import signalOperations, pre, functions

def SignalComapreAmplitude(SignalInput=[], SignalOutput=[]):
    if len(SignalInput) != len(SignalOutput):
        return False
    for i in range(len(SignalInput)):
        SignalInput[i] = float(str(SignalInput[i]).rstrip('f'))
        SignalOutput[i] = float(str(SignalOutput[i]).rstrip('f'))
        if abs( SignalInput[i] -  SignalOutput[i]) > 0.001:
            return False
    return True

def RoundPhaseShift(P):
    while P < 0:
        P += 2 * math.pi
    return float(P % (2 * math.pi))

def SignalComaprePhaseShift(SignalInput=[], SignalOutput=[]):
    if len(SignalInput) != len(SignalOutput):
        return False
    for i in range(len(SignalInput)):
        SignalInput[i] = float(str(SignalInput[i]).rstrip('f'))
        SignalOutput[i] = float(str(SignalOutput[i]).rstrip('f'))
        A = round(RoundPhaseShift( SignalInput[i]), 4)
        B = round(RoundPhaseShift( SignalOutput[i]), 4)
        if abs(A - B) > 0.0001:
            return False
    return True

# DFT TEST 
# index, originalSignal, amplitued, phases = signalOperations.oprations.Fouriore("DFT",signal="Task4\input_Signal_DFT.txt")
# N, expected_amplitudes, expected_phases = pre.readFile("Task4\Output_Signal_DFT,A,phase.txt")

# amplitude_result = SignalComapreAmplitude(amplitued, expected_amplitudes)
# phase_result = SignalComaprePhaseShift(phases, expected_phases)
# if amplitude_result and phase_result:
#     print("DFT Test Passed successfully ")
# else:
#     print("DFT Test Failed ")
#     if not amplitude_result:
#         print("Amplitude mismatch")
#     if not phase_result:
#         print("Phase mismatch")




# IDFT TEST 
# index, originalSignal, amplitued, phases = signalOperations.oprations.Fouriore("IDFT",signal="Task4\input_Signal_IDFT,A,phase.txt")

# N, expected_index, expected_signal = pre.readFile("Task4\Output_Signal_IDFT.txt")
# expected_signal = [float(str(x).rstrip('f')) for x in expected_signal]

# if SignalComapreAmplitude(originalSignal, expected_signal):
#     print("IDFT Test Passed successfully")
# else:
#     print("IDFT Test Failed ")

