import streamlit as st
import pandas as pd
from datetime import date

ADMIN_USER = "Gloria"
ADMIN_PASSWORD = "654321"

EMPLOYEES = {
    "Carlos": "2421",
    "Nihad": "123456",
    "Celia": "123456",
    "Neiser": "123456"
}

try:
    data = pd.read_csv("data.csv", index_col=0)
except FileNotFoundError:
    data = pd.DataFrame(columns=list(EMPLOYEES.keys()))

def check_authentication():
    user = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        if user == ADMIN_USER and password == ADMIN_PASSWORD:
            st.session_state["authenticated"] = True
            st.session_state["role"] = "admin"
            st.session_state["user"] = user
        elif user in EMPLOYEES and password == EMPLOYEES[user]:
            st.session_state["authenticated"] = True
            st.session_state["role"] = "employee"
            st.session_state["user"] = user
        else:
            st.error("Credenciales incorrectas")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["role"] = None
    st.session_state["user"] = None

if st.session_state["authenticated"]:
    if st.session_state["role"] == "admin":
        st.write("¡Bienvenido, administrador!")
        st.dataframe(data)
    elif st.session_state["role"] == "employee":
        st.write(f"¡Bienvenido, {st.session_state['user']}!")
        horas_extras = st.number_input("Minutos extras", value=0, step=1)
        fecha = date.today()

        if st.button("Agregar horas extras"):
            empleado = st.session_state["user"]
            if empleado in data.columns:
                if fecha.strftime("%Y-%m-%d") in data.index:
                    data.loc[fecha.strftime("%Y-%m-%d"), empleado] += horas_extras
                else:
                   data.loc[fecha.strftime("%Y-%m-%d"), empleado] = horas_extras
            else:
                st.error("Empleado no encontrado en el DataFrame.")
            data.to_csv("data.csv")  # Guardar los cambios
            st.success("Horas extras agregadas correctamente.")
            st.dataframe(data)
else:
    check_authentication()