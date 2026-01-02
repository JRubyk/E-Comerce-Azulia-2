from excepciones import CantidadInvalidaError


class Carrito:
    """Contiene ítems (producto + cantidad)."""

    def __init__(self) -> None:
        # key: producto_id -> value: {"producto": Producto, "cantidad": int}
        self._items: dict[int, dict] = {}

    def esta_vacio(self) -> bool:
        return len(self._items) == 0

    def agregar(self, producto, cantidad: int) -> None:
        if cantidad <= 0:
            raise CantidadInvalidaError("La cantidad debe ser un entero mayor que 0.")

        if producto.producto_id in self._items:
            self._items[producto.producto_id]["cantidad"] += cantidad
        else:
            self._items[producto.producto_id] = {"producto": producto, "cantidad": cantidad}

    def vaciar(self) -> None:
        self._items.clear()

    def total(self) -> float:
        total = 0.0
        for data in self._items.values():
            producto = data["producto"]
            cantidad = data["cantidad"]
            total += producto.precio * cantidad
        return total

    def detalle(self) -> list[dict]:
        # Devuelve items listos para imprimir: nombre, cantidad, precio, subtotal
        salida: list[dict] = []
        for data in self._items.values():
            producto = data["producto"]
            cantidad = data["cantidad"]
            salida.append(
                {
                    "nombre": producto.nombre,
                    "categoria": producto.categoria,
                    "cantidad": cantidad,
                    "precio_unitario": producto.precio,
                    "subtotal": producto.precio * cantidad,
                }
            )
        return salida
