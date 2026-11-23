"""Comprueba que el proyecto y botica.db funcionan en tu computadora.
Ejecutar desde la carpeta proyecto_botica:   python prueba_conexion.py
"""
from src.comun.conexion import ConexionSQLite

bd = ConexionSQLite("botica.db")
bd.conectar()

cursor = bd.conexion.cursor()
cursor.execute("SELECT username, rol FROM usuario_interno")
for fila in cursor.fetchall():
    print(fila)

bd.cerrar()
print("Conexión correcta.")
