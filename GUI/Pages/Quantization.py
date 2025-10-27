import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from  Logic import signalOperations


st.title("Quantization")
with st.form(key="Quantization_Form"):
    st.subheader("Upload Files")
    signal=st.file_uploader("Upload the First Signal", type=["txt"])
    inputvalue=st.number_input("Enter number of bits or levels", min_value=1)
    choice=st.radio('Choose an Option',['levels','bits'])
    submit=st.form_submit_button(label="Submit")
    if submit:
        if not signal or not choice:
            st.warning("Please Fill all Fields!")
        else:
            if choice=='levels':
             result =signalOperations.oprations.quantization(signal,bits=None,levels=inputvalue)
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
             result =signalOperations.oprations.quantization(signal,bits=inputvalue,levels=None)
             intervals = result["intervals"]
             quantized = result["quantized"]

             st.subheader("Quantization Results")
             st.write("**Intervals:**", intervals)
             st.write("**Quantized Values:**", quantized)
