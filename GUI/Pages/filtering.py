import numpy as np
import streamlit as st
from Logic import pre
from Task7 import task7
from Task8 import task8
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
                indx1,filtered = task8.filter("low-pass",8000,500,50,fc=1500)
                    
            elif(option=="Resampling"):
                k=st.number_input("Enter shifting steps")
if submit:
 st.download_button(
                label="Download filtered signal",
                data="\n".join(map(str, filtered.tolist())),
                file_name="fi;tered.txt"
            )


               