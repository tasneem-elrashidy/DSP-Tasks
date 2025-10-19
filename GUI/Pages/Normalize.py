import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from Logic import signalOperations
 

st.title("Normalize")
with st.form(key="Norm_Form"):
    st.subheader("Upload a File")
    signal1=st.file_uploader("Upload the Signal", type=["txt"])
    type=st.selectbox("Normalization Range",['-1 - 1', '0 - 1'])
    choice=st.radio('Choose an Option',['Continuous','Discrete'])
    submit=st.form_submit_button(label="Submit")
    if submit:
        if not signal1 or not type or not choice:
            st.warning("Please Fill all Fields!")
        else:
            # st.balloons()
            # st.snow()
            if type=='-1 - 1':
                idx,out=signalOperations.oprations.normOneToOne(signal1)
            else:
                idx,out=signalOperations.oprations.normZeroOne(signal1)
            st.subheader("Normalization plot")
            fig = go.Figure()
            if choice=="Continuous":
                fig.add_trace(go.Scatter(x=idx,y=out))
                fig.update_layout(title='Continuous Plot')
            else:
                fig.add_trace(go.Scatter(x=idx,y=out,mode='markers'))
                fig.update_layout(title='Discrete Plot')

            fig.update_layout(xaxis_title='Index',yaxis_title='Amplitude')
            
            st.plotly_chart(fig)
