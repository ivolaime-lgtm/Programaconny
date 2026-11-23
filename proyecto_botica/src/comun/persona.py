"""
MOD-00 · Clase abstracta Persona  (VERSIÓN PROVISIONAL)
Madre de UsuarioInterno (Avance 1) y de Cliente (Avance 3).

Uso desde una clase hija:
    from src.comun.persona import Persona

    class UsuarioInterno(Persona):
        def __init__(self, ..., nombres, apellidos, dni, ...):
            super().__init__(nombres, apellidos, dni)
            ...
        def mostrar_datos(self):          # obligatorio (método abstracto)
            return f"{self.nombre_completo} - DNI {self.dni_enmascarado}"
"""
from abc import ABC, abstractmethod

from src.comun.excepciones import DatoInvalidoError


class Persona(ABC):

    def __init__(self, nombres, apellidos, dni):
        # Se asigna mediante los setters para que validen al crear el objeto
        self.nombres = nombres
        self.apellidos = apellidos
        self.dni = dni

    # ---------- nombres ----------
    @property
    def nombres(self):
        return self._nombres

    @nombres.setter
    def nombres(self, valor):
        if not str(valor).strip():
            raise DatoInvalidoError("Los nombres no pueden estar vacíos.")
        self._nombres = str(valor).strip()

    # ---------- apellidos ----------
    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, valor):
        if not str(valor).strip():
            raise DatoInvalidoError("Los apellidos no pueden estar vacíos.")
        self._apellidos = str(valor).strip()

    # ---------- dni ----------
    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        valor = str(valor).strip()
        if len(valor) != 8 or not valor.isdigit():
            raise DatoInvalidoError("El DNI debe tener exactamente 8 dígitos.")
        self._dni = valor

    # ---------- propiedades calculadas ----------
    @property
    def nombre_completo(self):
        return f"{self._nombres} {self._apellidos}"

    @property
    def dni_enmascarado(self):
        return "****" + self._dni[-4:]

    # ---------- contrato para las clases hijas ----------
    @abstractmethod
    def mostrar_datos(self):
        """Cada clase hija devuelve sus datos en texto."""
