import streamlit as st
import os

ADMIN_USER = "ADMIN_USER"
ADMIN_PASSWORD = "123456"

def check_authentication():
    user = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        if user == ADMIN_USER and password == ADMIN_PASSWORD:
            st.session_state["authenticated"] = True
        else:
            st.error("Credenciales incorrectas")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if st.session_state["authenticated"]:
    st.write("¡Bienvenido, administrador!")
    # Aquí irían las funciones exclusivas de administrador
else:
    check_authentication()