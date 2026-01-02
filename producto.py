class Producto:
    """Representa un producto del catálogo de Azulia."""

    def __init__(self, producto_id: int, nombre: str, categoria: str, precio: float) -> None:
        self.producto_id = producto_id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self) -> str:
        return f"[{self.producto_id}] {self.nombre} | {self.categoria} | ${self.precio:.0f}"

    def to_linea_archivo(self) -> str:
        # Formato simple tipo CSV con ; (más fácil que lidiar con comas)
        return f"{self.producto_id};{self.nombre};{self.categoria};{self.precio}"

    @staticmethod
    def desde_linea_archivo(linea: str) -> "Producto":
        partes = linea.strip().split(";")
        producto_id = int(partes[0])
        nombre = partes[1]
        categoria = partes[2]
        precio = float(partes[3])
        return Producto(producto_id, nombre, categoria, precio)
