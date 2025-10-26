import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from Logic import signalOperations
 

st.title("Quantization")
with st.form(key="Quantization_Form"):
    st.subheader("Upload Files")
    signal=st.file_uploader("Upload the First Signal", type=["txt"])
    choice=st.radio('Choose an Option',['levels','bits'])
    submit=st.form_submit_button(label="Submit")
    if submit:
        if not signal or not choice:
            st.warning("Please Fill all Fields!")
        else:
            if choice=='levels':
             levels=st.number_input("Enter number of levels", min_value=1)
             result =signalOperations.oprations.quantization(signal,levels=levels)
             intervals = result["intervals"]
             quantized = result["quantized"]
             encoded = result["encoded"]
             error = result["error"]

             st.subheader("Quantization Results")
             st.write("**Intervals:**", intervals)
             st.write("**Quantized Values:**", quantized)
             st.write("**Encoded Values:**", encoded)
             st.write("**Quantization Error:**", error)
            else:
             bits=st.number_input("Enter number of bits", min_value=1)
             result =signalOperations.oprations.quantization(signal,bits=bits)
             intervals = result["intervals"]
             quantized = result["quantized"]

             st.subheader("Quantization Results")
             st.write("**Intervals:**", intervals)
             st.write("**Quantized Values:**", quantized)
