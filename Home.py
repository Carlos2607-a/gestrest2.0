import streamlit as st
import pandas as pd

st.title("Gestión Luna Beach")
st.write("Bienvenido a la página principal de Gestrest2.0")

name = st.text_input("Introduce tu nombre")

password = st.password_input("Introduce tu contraseña")

st.write(f"Nombre ingresado: {name}")
st.write(f"Contraseña ingresada: {password}")