import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from Logic import signalOperations
 

st.title("Square")
with st.form(key="Sq_Form"):
    st.subheader("Upload a File")
    signal1=st.file_uploader("Upload the Signal", type=["txt"])
    choice=st.radio('Choose an Option',['Continuous','Discrete'])
    submit=st.form_submit_button(label="Submit")
    if submit:
        if not signal1 or not choice:
            st.warning("Please Fill all Fields!")
        else:
            # st.balloons()
            # st.snow()
            idx,out=signalOperations.oprations.square(signal1)
            st.subheader("Squaring plot")
            fig = go.Figure()
            if choice=='Continuous':
                fig.add_trace(go.Scatter(x=idx,y=out))
                fig.update_layout(title='Continuous Plot')
            else:
                fig.add_trace(go.Scatter(x=idx, y=out,mode='markers'))
                fig.update_layout(title='Discrete Plot')

            fig.update_layout(xaxis_title='Index',yaxis_title='Amplitude')
            
            st.plotly_chart(fig)
