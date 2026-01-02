class ProductoNoEncontradoError(Exception):
    """Se lanza cuando no existe un producto con el ID solicitado."""


class CantidadInvalidaError(Exception):
    """Se lanza cuando la cantidad ingresada no es válida (<= 0)."""


class ArchivoSistemaError(Exception):
    """Se lanza cuando ocurre un problema leyendo/escribiendo archivos."""
