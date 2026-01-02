from datetime import datetime
from carrito import Carrito
from excepciones import ArchivoSistemaError


class Usuario:
    """Clase base (herencia)."""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def rol(self) -> str:
        return "USUARIO"


class Admin(Usuario):
    def rol(self) -> str:
        return "ADMIN"


class Cliente(Usuario):
    def __init__(self, nombre: str) -> None:
        super().__init__(nombre)
        self.carrito = Carrito()  # composición: Cliente TIENE un Carrito

    def rol(self) -> str:
        return "CLIENTE"

    def registrar_compra(self, ruta_ordenes: str) -> None:
        # Escribe una orden simple con fecha/hora, items y total
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total = self.carrito.total()
        detalle = self.carrito.detalle()

        try:
            with open(ruta_ordenes, "a", encoding="utf-8") as f:
                f.write("=" * 50 + "\n")
                f.write(f"AZULIA | ORDEN | {ahora}\n")
                f.write(f"Cliente: {self.nombre}\n")
                for item in detalle:
                    f.write(
                        f"- {item['nombre']} ({item['categoria']}) x{item['cantidad']} "
                        f"@ ${item['precio_unitario']:.0f} = ${item['subtotal']:.0f}\n"
                    )
                f.write(f"TOTAL: ${total:.0f}\n")
        except OSError as e:
            raise ArchivoSistemaError(f"No se pudo registrar la compra: {e}")
