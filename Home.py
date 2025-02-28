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


import streamlit as st
import sqlite3

# Conexión a la base de datos (SQLite)
conn = sqlite3.connect("horas_extras.db")
cursor = conn.cursor()

# Creación de tablas (si no existen)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        usuario TEXT,
        contrasena TEXT,
        rol TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS horas_extras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        empleado_id INTEGER,
        fecha TEXT,
        horas INTEGER,
        estado TEXT,
        FOREIGN KEY (empleado_id) REFERENCES empleados (id)
    )
""")
conn.commit()

# Ejemplo de función para agregar horas extras
def agregar_horas_extras(empleado_id, fecha, horas):
    cursor.execute("INSERT INTO horas_extras (empleado_id, fecha, horas, estado) VALUES (?, ?, ?, ?)",
                   (empleado_id, fecha, horas, "pendiente"))
    conn.commit()

# Ejemplo de función para obtener horas extras pendientes
def obtener_horas_extras_pendientes():
    cursor.execute("""
        SELECT horas_extras.id, empleados.nombre, horas_extras.fecha, horas_extras.horas
        FROM horas_extras
        JOIN empleados ON horas_extras.empleado_id = empleados.id
        WHERE horas_extras.estado = 'pendiente'
    """)
    return cursor.fetchall()
#resto de funciones.

# Ejemplo de la pagina de Streamlit.
st.title("Gestión de Horas Extras")

# Ejemplo de como llamar a la función.
if st.button("Agregar horas"):
    agregar_horas_extras(1,"2024-01-01", 5)

# Ejemplo de como mostrar los datos de la base de datos.
pendientes = obtener_horas_extras_pendientes()
st.write(pendientes)

conn.close()