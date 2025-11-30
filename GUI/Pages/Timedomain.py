import streamlit as st
from Logic import pre
from Task7 import task7

st.title("Time Domain oprations")
with st.form(key="time_domain"):
    st.subheader("Upload a File")
    signal=st.file_uploader("Upload the Signal", type=["txt"])
    
    option = st.selectbox(
        "What Time Domain opration you would like t do?",
        ( "Smoothing","Sharpining","Shifting","Folding","Shifting a folded signal","RemoveDC component"),
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

                elif(option=="Shifting a folded signal"):
                    k=st.number_input("Enter shifting steps")
                    result=task7.Folding(value)
                    shifted=task7.shifting(result,k)
                    st.subheader("Shifting a folded signal Results")
                    st.write("**values:**", shifted)
                    st.write("**indices:**", result)

                elif(option=="RemoveDC component"):
                    result=task7.removeDcTimeDomain(value)
                    st.subheader("RemoveDC component Results")
                    st.write("**values:**", result) 