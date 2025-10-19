import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from Logic import GenerateSignals


st.title("Generate a Signal")
values={
        'type':None,
        'amp': None,
        'frq':None,
        'fs':None,
        'theta':None
    }
with st.form(key='Gen_form'):
    values['type']=st.selectbox("Type of Signal",['sin','cos'])
    values['amp']=st.number_input('Enter the Amplitude: ')
    values['frq']=st.number_input('Enter the Frequency: ')
    values['fs']=st.number_input('Enter the Sampling Frequency: ')
    values['theta']=st.number_input('Enter the Shift Angle: ', format='%20f')
    choice=st.radio('Choose an Option',['Continuous','Discrete'])
    submit=st.form_submit_button(label="Submit")
    if submit:
        if not all(values.values()) or not choice:
            st.warning("Please Fill all Fields!")
        else:
            # st.balloons()
            # st.snow()
            idx,out=GenerateSignals.SignalGenerator.generate(values['type'],values['amp'], values['frq'],values['fs'],values['theta'])
            st.subheader("The Signal Generated")
            fig = go.Figure()
            if choice=='Continuous':
                fig.add_trace(go.Scatter(x=idx, y=out))
                fig.update_layout(title='Continuous Plot')
            else:
                fig.add_trace(go.Scatter(x=idx,y=out,mode='markers'))
                fig.update_layout(title='Discrete Plot')

            fig.update_layout(xaxis_title='Index', yaxis_title='Amplitude')
            
            st.plotly_chart(fig)

