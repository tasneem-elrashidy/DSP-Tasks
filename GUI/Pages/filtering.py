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
            if(option=="Filtering"):
                st.write("Enter filtering parameters:")
                mode = st.selectbox("Filter Type", ["low-pass", "high-pass", "band-pass", "band-stop"])
                Fs  = st.number_input("Sampling Frequency (Fs)", value=8000)
                transition = st.number_input("transition band", value=500)
                StopBandAttenuation  = st.number_input("Stop Band Attenuation", value=50)
                fc = st.number_input("FC value",value=1500) 
                f1 = st.number_input("Band Start (f1)",value=150)
                f2 = st.number_input("Band End (f2)",value=250)
                    
            if(option=="Resampling"):
                l=st.number_input("Enter L")
                m=st.number_input("Enter M")

            submit=st.form_submit_button(label="Submit")
if submit:
                if not signal :
                    st.warning("Please Fill all Fields!")
                elif(option=="Filtering"):
                    NumOfSamples,index,value=pre.readFile(signal)
                    if mode in ["low-pass", "high-pass"]:
                        indx1, filtered = task8.filter(mode, Fs, transition, StopBandAttenuation, fc=fc)
                    else:   
                        indx1, filtered = task8.filter(mode, Fs, transition, StopBandAttenuation, f1=f1, f2=f2)
                    st.download_button(label="Download filtered signal",
                            data="\n".join(map(str, filtered.tolist())),
                            file_name="filtered.txt")
                elif(option=="Resampling"):
                       NumOfSamples,index,value=pre.readFile(signal)
                       indx,Resampled=task8.resampling(value,l,m)
                       st.download_button(label="Download filtered signal",
                            data="\n".join(map(str, Resampled.tolist())),
                            file_name="Resampled.txt")
                
               

               