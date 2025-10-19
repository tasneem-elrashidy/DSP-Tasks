import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from Logic import signalOperations
 

st.title("Subtract")
with st.form(key="Sub_Form"):
    st.subheader("Upload Files")
    signal1=st.file_uploader("Upload the First Signal", type=["txt"])
    signal2=st.file_uploader("Upload the Second Signal", type=["txt"])
    choice=st.radio('Choose an Option',['Continuous','Discrete'])
    submit=st.form_submit_button(label="Submit")
    if submit:
        if not signal1 or not signal2 or not choice:
            st.warning("Please Fill all Fields!")
        else:
            # st.balloons()
            # st.snow()
            idx,out=signalOperations.oprations.sub(signal1,signal2)
            st.subheader("Subtraction plot")
            fig = go.Figure()
            if choice=='Continuous':
                fig.add_trace(go.Scatter(x=idx,y=out))
                fig.update_layout(title='Continuous Plot')
            else:
                fig.add_trace(go.Scatter(x=idx, y=out,mode='markers'))
                fig.update_layout(title='Discrete Plot')
            fig.update_layout(xaxis_title='Index', yaxis_title='Amplitude')
            
            st.plotly_chart(fig)
