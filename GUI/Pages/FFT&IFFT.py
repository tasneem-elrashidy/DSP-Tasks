import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from Logic import signalOperations
from Logic import functions
from Logic import pre
import numpy as np

st.title("Frequency Domain")
with st.form(key="FD_Form"):
    choice=st.radio('Choose an Option',['FFT','IFFT'])
    st.subheader("Upload a File")
    file=st.file_uploader("Upload the File", type=["txt"])
    fs=st.number_input("Enter a Sampling Frequency")

    st.subheader('Modify Amplitude & Phase (Optional)')
    idx = st.number_input("Enter the index", min_value=0, step=1)
    new_amp = st.number_input("Enter a New Amplitude", min_value=0.0, format="%.3f")
    new_phase = st.number_input("Enter a New Phase (radians)", format="%.3f")
    submit=st.form_submit_button(label="Submit",key="main")
    if submit:
        if not choice or not file or not fs:
            st.warning("Please Fill all Fields!")
        else:
            # st.balloons()
            # st.snow()
            NumOfSamples,indx,value=pre.readFile(file)
            indx, originalsig, amp, phase,X = signalOperations.oprations.FFT_IFFT(choice, value)

            # Modify amplitude & phase if values provided
            if new_amp != 0 or new_phase != 0:
                amp, phase = functions.modifyAmpPhase(amp, phase, int(idx), new_amp, new_phase)

            # If DFT → Normalize amplitude and plot
            if choice == "FFT":
                amp = np.array(amp)
                phase = np.array(phase)

                indx,amp_norm =signalOperations.oprations.normZeroOne(values=amp)

                freqs=functions.calcOmega(fs,len(amp))

            
                st.subheader("Amplitude Spectrum")
                fig1 = go.Figure()
                fig1.add_trace(go.Scatter(x=freqs, y=amp_norm, mode='lines+markers'))
                fig1.update_layout(
                    xaxis_title='Frequency (Hz)',
                    yaxis_title='Normalized Amplitude',
                    title='Frequency vs Amplitude'
                )
                st.plotly_chart(fig1)

                # Plot Phase vs Frequency
                st.subheader("Phase Spectrum")
                fig2 = go.Figure()
                fig2.add_trace(go.Scatter(x=freqs, y=phase, mode='lines+markers'))
                fig2.update_layout(
                    xaxis_title='Frequency (Hz)',
                    yaxis_title='Phase (radians)',
                    title='Frequency vs Phase'
                )
                st.plotly_chart(fig2)

                # Dominant Frequencies
                dom_freqs = functions.dominantFrequencies(amp_norm, fs)
                st.subheader("Dominant Frequencies (> 0.5):")
                st.write(dom_freqs)

            # If IDFT → Reconstruct time-domain signal
            elif choice == "IFFT":
                st.subheader("Reconstructed Signal")
                fig3 = go.Figure()
                fig3.add_trace(go.Scatter(x=indx, y=originalsig, mode='lines+markers'))
                fig3.update_layout(
                    xaxis_title='Index',
                    yaxis_title='Amplitude',
                    title='Reconstructed Time Domain Signal'
                )
                st.plotly_chart(fig3)
            
with st.form(key="DC_Form"):
    st.subheader("Remove DC Component")
    file = st.file_uploader("Upload a Signal File", type=["txt"], key="dc_file")
    sub = st.form_submit_button(label="Remove DC")

    if sub:
        if not file:
            st.warning("Please upload a file.")
        else:
            result = functions.removeDC(file)
            st.subheader("Signal After Removing DC Component:")

            fig2 = go.Figure()
            # fig2.add_trace(go.Scatter(x=result, y=indx, mode='lines+markers'))
            # fig2.update_layout(
            #      xaxis_title='index',
            #      yaxis_title='values ',
            #      title='indx vs values'
            #  )
            
            # st.plotly_chart(fig2)
            st.write(result)
