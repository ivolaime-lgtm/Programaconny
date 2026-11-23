"""
MOD-00 · Enumeraciones compartidas  (VERSIÓN PROVISIONAL)

Uso:
    from src.comun.enums import Clasificacion, Rol
    if medicamento.clasificacion == Clasificacion.CON_RECETA: ...

En la base de datos se guarda el NOMBRE (ej. 'CON_RECETA') y se convierte así:
    Clasificacion['CON_RECETA']   ->  Clasificacion.CON_RECETA
    Clasificacion.CON_RECETA.name ->  'CON_RECETA'
    Clasificacion.CON_RECETA.value -> 'Con receta'   (texto para mostrar)
"""
from enum import Enum


class Clasificacion(Enum):
    VENTA_LIBRE = "Venta libre"
    CON_RECETA = "Con receta"
    RECETA_ESPECIAL = "Receta especial"
    BLOQUEADO = "Bloqueado"


class Rol(Enum):
    QUIMICO_FARMACEUTICO = "Químico farmacéutico"
    ADMINISTRADOR = "Administrador"
