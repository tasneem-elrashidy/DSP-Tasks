import numpy as np
import streamlit as st
from Logic import pre
from Task7 import task7
import plotly.graph_objects as go

st.title("Time Domain oprations")
with st.form(key="time_domain"):
    st.subheader("Upload a File")
    signal=st.file_uploader("Upload the Signal", type=["txt"])
    
    option = st.selectbox(
        "What Time Domain opration you would like t do?",
        ( "Smoothing","Sharpining","Shifting","Folding","Shifting & folding","RemoveDC component"),
    )
    submit=st.form_submit_button(label="Submit")
    if submit:
            if not signal :
                st.warning("Please Fill all Fields!")
            else:
                NumOfSamples,index,value=pre.readFile(signal)
                if(option=="Smoothing"):

                    k=st.number_input("Enter the window size to Multiply")
                    result,ind=task7.movingAvg(value,k)
                    st.subheader("Smoothing Results")
                    st.write("**values:**", result)

                elif(option=="Sharpining"):
                    firstDir,secDir=task7.sharpening(value)
                    st.subheader("Sharpining Results")
                    st.write("**first dirivative:**", firstDir)
                    st.write("**second dirivative:**", secDir)

                elif(option=="Shifting"):

                    k=st.number_input("Enter shifting steps")
                    result=task7.shifting(value,k)
                    st.subheader("Shifting Results")
                    st.write("**values:**", result)

                elif(option=="Folding"):
                    result=task7.Folding(value)
                    st.subheader("Folding Results")
                    st.write("**values:**", result)

                elif(option=="Shifting & folding"):
                    k=st.number_input("Enter shifting steps")
                    result=task7.Folding(value)
                    shifted=task7.shifting(index,k)
                    st.subheader("Shifting a folded signal Results")
                    st.write("**values:**", result)
                    st.write("**indices:**", shifted)

                elif(option=="RemoveDC component"):
                    result=task7.removeDcTimeDomain(value)
                    st.subheader("RemoveDC component Results")
                    st.write("**values:**", result) 

with st.form(key="time_domain2"):
    st.subheader("Convolution")
    user_input1 = st.text_input("Enter a list of first signal indices separated by commas:")

    # Convert input to a list if not empty
    if user_input1:
        try:
            user_list1 = [int(x.strip()) for x in user_input1.split(",")]
        except ValueError:
            st.error("Please enter valid numbers separated by commas.")
    user_input2 = st.text_input("Enter a list of first signal samples separated by commas:")

    # Convert input to a list if not empty
    if user_input2:
        try:
            user_list2 = [int(x.strip()) for x in user_input2.split(",")]
        except ValueError:
            st.error("Please enter valid numbers separated by commas.")
    user_input3 = st.text_input("Enter a list of second signal indices separated by commas:")

    # Convert input to a list if not empty
    if user_input3:
        try:
            user_list3 = [int(x.strip()) for x in user_input3.split(",")]
        except ValueError:
            st.error("Please enter valid numbers separated by commas.")
    user_input4 = st.text_input("Enter a list of second signal samples separated by commas:")

    # Convert input to a list if not empty
    if user_input4:
        try:
            user_list4 = [int(x.strip()) for x in user_input4.split(",")]
        except ValueError:
            st.error("Please enter valid numbers separated by commas.")
    submit=st.form_submit_button(label="Submit")
    if submit:
            # if not user_list1 or user_list2 or user_list3 or user_list4 :
            #     st.warning("Please Fill all Fields!")
            # else:
                res_idx, res_smp=task7.convolveSignals(user_list1,user_list2,user_list3,user_list4)
                st.write("The result indices:", res_idx)
                st.write("The result samples:", res_smp)

with st.form(key="time_domain3"):
    st.subheader("Upload Files")
    signal1=st.file_uploader("Upload the Signal 1", type=["txt"])
    signal2=st.file_uploader("Upload the Signal 2", type=["txt"])
    
    option1 = st.selectbox(
        "What Time Domain opration you would like to do?",
        ( "cross-correlation / autocorrelation","cross-correlation of periodic signals")
    )
    submit=st.form_submit_button(label="Submit")
    if submit:
            if not signal1:
                st.warning("Please Fill all Fields!")
            else:
                if(option1=="cross-correlation / autocorrelation"):
                    st.subheader("cross-correlation / autocorrelation")
                    idx,smp=task7.correlation(sig1=signal1,sig2=signal2)
                    st.subheader("Signal")  
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=idx,y=smp,mode='lines+markers'))
                    fig.update_layout(
                        xaxis_title='Index',
                        yaxis_title='Samples',
                    )
                    st.plotly_chart(fig)

                elif(option1=="cross-correlation of periodic signals"):
                    st.subheader("cross-correlation of periodic signals")
                    idx,smp=task7.periodic_normalized_correlation(sig1=signal1,sig2=signal2)
                    st.subheader("Signal")
                    fig2 = go.Figure()
                    fig2.add_trace(go.Scatter(x=idx,y=smp,mode='lines+markers'))
                    fig2.update_layout(
                        xaxis_title='Index',
                        yaxis_title='Samples',
                    )
                    st.plotly_chart(fig2)

with st.form(key="time_domain4"):
    st.subheader("Upload Files of signals for time analysis")
    signal1=st.file_uploader("Upload the Signal 1", type=["txt"])
    signal2=st.file_uploader("Upload the Signal 2", type=["txt"])
    fs = st.number_input("Enter Sampling period", format="%.3f")
    
    submit=st.form_submit_button(label="Submit")
    if submit:
            if not signal1 or not signal2 or not fs:
                st.warning("Please Fill all Fields!")
            else:
                t=task7.time_delay(signal1,signal2,fs)
                st.write("The delay time is: ", t)

               

               