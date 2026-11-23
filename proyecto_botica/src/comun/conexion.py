"""
MOD-00 · Conexión única a SQLite  (VERSIÓN PROVISIONAL)

Uso (en un DAO):
    from src.comun.conexion import ConexionSQLite

    bd = ConexionSQLite()          # por defecto usa botica.db
    bd.conectar()
    cursor = bd.conexion.cursor()
    cursor.execute("SELECT * FROM medicamento WHERE nombre LIKE ?", ("%para%",))
    filas = cursor.fetchall()
    bd.cerrar()

Mientras no llegue el botica.db definitivo, si el archivo no existe, SQLite crea uno vacío:
pueden crear ahí sus propias tablas de prueba.
"""
import sqlite3

from src.comun.excepciones import BoticaError


class ConexionSQLite:

    def __init__(self, ruta_bd="botica.db"):
        self.__ruta_bd = ruta_bd
        self.__conexion = None

    def conectar(self):
        try:
            self.__conexion = sqlite3.connect(self.__ruta_bd)
            self.__conexion.execute("PRAGMA foreign_keys = ON")
        except sqlite3.Error:
            raise BoticaError("No se pudo conectar con la base de datos.")

    @property
    def conexion(self):
        if self.__conexion is None:
            raise BoticaError("La base de datos no está conectada. Llame primero a conectar().")
        return self.__conexion

    def cerrar(self):
        if self.__conexion is not None:
            self.__conexion.close()
            self.__conexion = None
