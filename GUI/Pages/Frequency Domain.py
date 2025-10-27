import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from Logic import signalOperations
from Logic import functions
import numpy as np

st.title("Frequency Domain")
with st.form(key="FD_Form"):
    choice=st.radio('Choose an Option',['DFT','IDFT'])
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
            indx, originalsig, amp, phase = signalOperations.oprations.Fouriore(choice, file)

            # Modify amplitude & phase if values provided
            if new_amp != 0 or new_phase != 0:
                amp, phase = functions.modifyAmpPhase(amp, phase, int(idx), new_amp, new_phase)

            # If DFT → Normalize amplitude and plot
            if choice == "DFT":
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
            elif choice == "IDFT":
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
            st.write(result)



#chat 1////////////////////////////////////////////////////////////////////////////////////

# import streamlit as st
# import numpy as np
# import plotly.graph_objects as go
# from Logic import signalOperations, functions

# st.title("Frequency Domain")
# with st.form(key="FD_Form"):
#     choice = st.radio('Choose an Option', ['DFT', 'IDFT'])
#     st.subheader("Upload a File")
#     file = st.file_uploader("Upload the File", type=["txt"])
#     fs = st.number_input("Enter Sampling Frequency (Hz)", min_value=1)

#     st.subheader('Modify Amplitude & Phase (Optional)')
#     idx = st.number_input("Enter the index", min_value=0, step=1)
#     new_amp = st.number_input("Enter a New Amplitude", min_value=0.0, format="%.3f")
#     new_phase = st.number_input("Enter a New Phase (radians)", format="%.3f")

#     submit = st.form_submit_button(label="Submit")

#     if submit:
#         if not file:
#             st.warning("Please upload a file.")
#         else:
#             # Run Fourier Transform (Smart code for both DFT & IDFT)
#             indx, originalsig, amp, phase = signalOperations.oprations.Fouriore(choice, file)

#             # Modify amplitude & phase if values provided
#             if new_amp != 0 or new_phase != 0:
#                 amp, phase = functions.modifyAmpPhase(amp, phase, int(idx), new_amp, new_phase)

#             # If DFT → Normalize amplitude and plot
#             if choice == "DFT":
#                 amp = np.array(amp)
#                 phase = np.array(phase)

#                 indx,amp_norm =signalOperations.oprations.normZeroOne(amp)

#                 freqs = np.arange(len(amp)) * (fs / len(amp))

#                 # Plot Amplitude vs Frequency
#                 st.subheader("Amplitude Spectrum")
#                 fig1 = go.Figure()
#                 fig1.add_trace(go.Scatter(x=freqs, y=amp_norm, mode='lines+markers'))
#                 fig1.update_layout(
#                     xaxis_title='Frequency (Hz)',
#                     yaxis_title='Normalized Amplitude',
#                     title='Frequency vs Amplitude'
#                 )
#                 st.plotly_chart(fig1)

#                 # Plot Phase vs Frequency
#                 st.subheader("Phase Spectrum")
#                 fig2 = go.Figure()
#                 fig2.add_trace(go.Scatter(x=freqs, y=phase, mode='lines+markers'))
#                 fig2.update_layout(
#                     xaxis_title='Frequency (Hz)',
#                     yaxis_title='Phase (radians)',
#                     title='Frequency vs Phase'
#                 )
#                 st.plotly_chart(fig2)

#                 # Dominant Frequencies
#                 dom_freqs = functions.dominantFrequencies(amp_norm, fs)
#                 st.subheader("Dominant Frequencies (> 0.5):")
#                 st.write(dom_freqs)

#             # If IDFT → Reconstruct time-domain signal
#             elif choice == "IDFT":
#                 st.subheader("Reconstructed Signal")
#                 fig3 = go.Figure()
#                 fig3.add_trace(go.Scatter(x=indx, y=originalsig, mode='lines+markers'))
#                 fig3.update_layout(
#                     xaxis_title='Index',
#                     yaxis_title='Amplitude',
#                     title='Reconstructed Time Domain Signal'
#                 )
#                 st.plotly_chart(fig3)

# with st.form(key="DC_Form"):
#     st.subheader("Remove DC Component")
#     file = st.file_uploader("Upload a Signal File", type=["txt"], key="dc_file")
#     sub = st.form_submit_button(label="Remove DC")

#     if sub:
#         if not file:
#             st.warning("Please upload a file.")
#         else:
#             result = functions.removeDC(file)
#             st.subheader("Signal After Removing DC Component:")
#             st.write(result)


#chat 2////////////////////////////////////////////////////////////////////////////////////////////
# import streamlit as st
# import numpy as np   # added
# import matplotlib.pyplot as plt
# import plotly.graph_objects as go
# from Logic import signalOperations
# from Logic import functions
# from Logic import pre   # added (to read files if needed)

# st.title("Frequency Domain")

# with st.form(key="FD_Form"):
#     choice = st.radio('Choose an Option', ['DFT', 'IDFT'])
#     st.subheader("Upload a File")
#     file = st.file_uploader("Upload the File", type=["txt"])
#     fs = st.number_input("Enter a Sampling Frequency (Hz)", min_value=1.0, value=64.0, step=1.0)  # added default + label

#     st.subheader('Modify Amplitude & Phase')
#     idx = st.number_input("Enter the index", min_value=0, step=1)
#     new_amp = st.number_input("Enter a New Amplitude", min_value=0.0)
#     new_phase = st.number_input("Enter a New Phase (radians)", format="%.4f")

#     submit = st.form_submit_button(label="Submit", key="main")

#     if submit:
#         if not choice or not file or not fs:
#             st.warning("Please Fill all Fields!")
#         else:
#             if choice == "DFT":
#                 indx, originalsig, amp, phase = signalOperations.oprations.Fouriore("DFT", file)  # fixed: was IDFT
#                 # added normalize amplitude
#                 # amp = np.array(amp, dtype=float)
#                 phase = np.array(phase, dtype=float)
#                 indx,amp_norm =signalOperations.oprations.normZeroOne(values=amp) # added normalization

#                 if new_amp != 0 or new_phase != 0:  # added check
#                     amp, phase = functions.modifyAmpPhase(amp, phase, int(idx), new_amp, new_phase)

#                 # added frequency axis and plots
#                 freqs = np.arange(len(amp_norm)) * (fs / len(amp_norm))  # added
#                 st.subheader("Plots")
#                 fig = go.Figure()
#                 fig.add_trace(go.Scatter(x=freqs, y=amp_norm, mode='lines+markers', name="Amplitude"))
#                 fig.update_layout(title="Frequency vs Amplitude", xaxis_title="Frequency (Hz)", yaxis_title="Normalized Amplitude")
#                 st.plotly_chart(fig)

#                 fig2 = go.Figure()
#                 fig2.add_trace(go.Scatter(x=freqs, y=phase, mode='lines+markers', name="Phase"))
#                 fig2.update_layout(title="Frequency vs Phase", xaxis_title="Frequency (Hz)", yaxis_title="Phase (radians)")
#                 st.plotly_chart(fig2)

#                 # added dominant frequencies
#                 st.subheader("Dominant Frequencies (>0.5):")
#                 dom_freqs = functions.dominantFrequencies(amp_norm, fs)
#                 st.write(dom_freqs)

#             else:
#                 indx, originalsig, amp, phase = signalOperations.oprations.Fouriore("IDFT", file)  # fixed

#                 # added: reconstruct signal plot
#                 st.subheader("Reconstructed Signal (IDFT)")
#                 fig = go.Figure()
#                 fig.add_trace(go.Scatter(x=indx, y=originalsig, mode='lines+markers'))
#                 fig.update_layout(title="Reconstructed Time-Domain Signal", xaxis_title="Index", yaxis_title="Amplitude")
#                 st.plotly_chart(fig)


# with st.form(key="DC_Form"):
#     st.subheader("Remove DC Component")
#     file = st.file_uploader("Upload the Signal File", type=["txt"], key="dc_file")  # added unique key
#     sub = st.form_submit_button(label="Submit", key="dc")
#     if sub:
#         if not file:
#             st.warning("Please Fill all Fields!")
#         else:
#             i = functions.removeDC(file)
#             st.subheader("Signal After Removing DC Component:")
#             st.write(i)  # added label
