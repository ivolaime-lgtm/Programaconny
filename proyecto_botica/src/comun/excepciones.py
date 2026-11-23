"""
MOD-00 · Excepciones del sistema  (VERSIÓN PROVISIONAL)
Los nombres y firmas son los definitivos del Excel. Se reemplazará por la versión final
sin que cambie cómo se usan.

Uso:
    from src.comun.excepciones import DatoInvalidoError
    raise DatoInvalidoError("El precio debe ser mayor a cero.")

    try:
        ...
    except BoticaError as error:
        print(error.mensaje_usuario)
"""


class BoticaError(Exception):
    """Error base: todas las excepciones del sistema heredan de esta."""

    def __init__(self, mensaje):
        super().__init__(mensaje)
        self.__mensaje_usuario = mensaje

    @property
    def mensaje_usuario(self):
        return self.__mensaje_usuario


# ---------- Base común (Integrante 1) ----------
class DatoInvalidoError(BoticaError):
    """Dato vacío, negativo, con letras donde van números, DNI mal escrito, etc."""


class PermisoDenegadoError(BoticaError):
    """El usuario en sesión no tiene el permiso necesario."""


class SinResultadosError(BoticaError):
    """Una búsqueda no encontró coincidencias."""


# ---------- MOD-01 (ya incluidas para que nadie edite este archivo a la vez) ----------
class CredencialesInvalidasError(BoticaError):
    """Usuario o contraseña incorrectos (Integrante 3)."""


class UsuarioBloqueadoError(BoticaError):
    """Usuario bloqueado por intentos fallidos (Integrante 2)."""
