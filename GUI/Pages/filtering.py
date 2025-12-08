import numpy as np
import streamlit as st
from Logic import pre
from Task7 import task7
import plotly.graph_objects as go

st.title("Filtering & Resampling oprations")
with st.form(key="task8"):
    st.subheader("Upload a File")
    signal=st.file_uploader("Upload the Signal", type=["txt"])

    option = st.selectbox(
        "Filtering or Resampling?",
        ( "Filtering","Resampling"),
    )
    submit=st.form_submit_button(label="Submit")
    if submit:
        if not signal :
            st.warning("Please Fill all Fields!")
        else:
            NumOfSamples,index,value=pre.readFile(signal)
            if(option=="Filtering"):
                k=st.number_input("Enter the window size to Multiply")

            elif(option=="Resampling"):
                k=st.number_input("Enter shifting steps")
                result=task7.Folding(value)
                shifted=task7.shifting(index,k)
                st.subheader("Shifting a folded signal Results")
                st.write("**values:**", result)
                st.write("**indices:**", shifted)


               