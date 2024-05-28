import streamlit as st
import math

def BBO(wavelength):
    ao = 2.7359
    bo = 0.01878
    co = 0.01822
    do = 0.01354
    
    ae = 2.3753
    be = 0.01224
    ce = 0.01667
    de = 0.01516
    
    no = math.sqrt(ao + bo/((wavelength**2)-co) - do*wavelength**2)
    ne = math.sqrt(ae + be/((wavelength**2)-ce) - de*wavelength**2)
    
    return [no,ne]

st.title("BBO Refractive Index")
wavelength = st.text_input("Enter Wavelength", value = '0.405')
st.write(BBO(float(wavelength)))
