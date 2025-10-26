import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from Logic import signalOperations
from Logic import functions
 

st.title("Frequency Domain")
with st.form(key="FD_Form"):
    choice=st.radio('Choose an Option',['DFT','IDFT'])
    st.subheader("Upload a File")
    file=st.file_uploader("Upload the File", type=["txt"])
    fs=st.number_input("Enter a Sampling Frequency")

    st.subheader('Modify Amplitude & Phase')
    idx=st.number_input("Enter the index")
    new_amp=st.number_input("Enter a New Amplitude")
    new_phase=st.number_input("Enter a New Phase")
    submit=st.form_submit_button(label="Submit",key="main")
    if submit:
        if not choice or not file or not fs:
            st.warning("Please Fill all Fields!")
        else:
            # st.balloons()
            # st.snow()
            if(choice=="DFT"):
                amp,phase=dft(file) #dft ver
                if new_amp and new_phase:
                    amp,phase=functions.modifyAmpPhase(amp,phase,idx,new_amp,new_phase)
            else:
                sig=idft(file) #idft ver

            
            # st.subheader("plot")
            # fig = go.Figure()

            # if choice=='Continuous':
            #     fig.add_trace(go.Scatter(x=idx,y=out))
            #     fig.update_layout(title='Continuous Plot')
            # else:
            #     fig.add_trace(go.Scatter(x=idx,y=out,mode='markers'))
            #     fig.update_layout(title='Discrete Plot')

            # fig.update_layout(xaxis_title='Index',yaxis_title='Amplitude')
            
            # st.plotly_chart(fig)
            st.subheader("Dominant Frequencies:")
            st.write(functions.dominantFrequencies)
            
with st.form(key="DC_Form"):
    st.subheader("Remove DC Component")
    st.subheader("Upload a File")
    file=st.file_uploader("Upload the Signal File", type=["txt"])
    sub=st.form_submit_button(label="Submit",key="dc")
    if sub:
        if not file:
            st.warning("Please Fill all Fields!")
        else:
            i=functions.removeDC(file)
            st.write(i)
