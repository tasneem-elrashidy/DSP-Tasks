import streamlit as st 
import numpy as np
import matplotlib as plt
import signalOperations
import pre


def add():
    # pdf1 = st.file_uploader('upload signal 1', type="txt")
    # if pdf1 is None:
    #    pdf1 = stringio.read()
    #    print("hi")
    # pdf2 = st.file_uploader('upload signal 2', type="txt")
    # print("hi2")
    # if pdf1 is not None and pdf2 is not None:
     input1=input("input file path1")
     input2=input("input file path2")
     if input1 is None and input2 is None:
      signal1x,signal1y=pre.readFile(input1)
      signal2x,signal2y=pre.readFile(input2)
      addition=signalOperations.oprations.add(signal1x,signal1y,signal2x,signal2y)
    #  fig1, ax1 = plt.subplots()
    #  ax1.plot(signal1x, signal1y, label='Signal 1', linestyle='--')
    #  ax1.plot(signal2x, signal2y, label='Signal 2', linestyle='--')
    #  ax1.plot(signal1x, addition, label='Added Signal', color='red')
    #  ax1.set_title("Continuous Signals")
    #  ax1.legend()
    #  st.pyplot(fig1)