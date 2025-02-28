import streamlit as st

ADMIN_USER = "ADMIN_USER"
ADMIN_PASSWORD = "123456"

EMPLOYEES = {
    "Carlos": "2421",
    "Nihad": "123456",
    "Celia": "123456",
    "Neiser": "123456"
}

def check_authentication():
    user = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        if user == ADMIN_USER and password == ADMIN_PASSWORD:
            st.session_state["authenticated"] = True
            st.session_state["role"] = "admin" #asignamos el rol de admin
        elif user in EMPLOYEES and password == EMPLOYEES[user]:
            st.session_state["authenticated"] = True
            st.session_state["role"] = "employee" #asignamos el rol de empleado
        else:
            st.error("Credenciales incorrectas")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["role"] = None #agregamos el rol al estado de la session.

if st.session_state["authenticated"]:
    if st.session_state["role"] == "admin":
        st.write("¡Bienvenido, administrador!")
        # Aquí irían las funciones exclusivas de administrador
    elif st.session_state["role"] == "employee":
        st.write("¡Bienvenido, empleado!")
        # Aquí irían las funciones exclusivas de empleado
else:
    check_authentication()