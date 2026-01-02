from producto import Producto
from excepciones import ProductoNoEncontradoError, ArchivoSistemaError


class Catalogo:
    """Contiene y gestiona muchos Producto (composición)."""

    def __init__(self) -> None:
        self._productos: dict[int, Producto] = {}

    def cargar_inicial(self) -> None:
        # Catálogo base Azulia (si no existe archivo aún)
        productos = [
            Producto(1, "Aros Luna", "aros", 7990),
            Producto(2, "Collar Estrella", "collares", 12990),
            Producto(3, "Anillo Aurora", "anillos", 9990),
            Producto(4, "Pulsera Brisa", "pulseras", 10990),
            Producto(5, "Tobillera Mar", "tobilleras", 8990),
        ]
        for p in productos:
            self._productos[p.producto_id] = p

    def listar(self) -> list[Producto]:
        return list(self._productos.values())

    def existe_id(self, producto_id: int) -> bool:
        return producto_id in self._productos

    def obtener_por_id(self, producto_id: int) -> Producto:
        if producto_id not in self._productos:
            raise ProductoNoEncontradoError(f"No existe producto con ID {producto_id}.")
        return self._productos[producto_id]

    def agregar(self, producto: Producto) -> None:
        if self.existe_id(producto.producto_id):
            raise ValueError(f"Ya existe un producto con ID {producto.producto_id}.")
        self._productos[producto.producto_id] = producto

    def actualizar(self, producto_id: int, nombre: str | None, categoria: str | None, precio: float | None) -> None:
        producto = self.obtener_por_id(producto_id)
        if nombre is not None and nombre.strip() != "":
            producto.nombre = nombre.strip()
        if categoria is not None and categoria.strip() != "":
            producto.categoria = categoria.strip()
        if precio is not None:
            if precio <= 0:
                raise ValueError("El precio debe ser mayor que 0.")
            producto.precio = precio

    def eliminar(self, producto_id: int) -> None:
        # Reutilizamos la validación del obtener
        self.obtener_por_id(producto_id)
        del self._productos[producto_id]

    def buscar(self, texto: str) -> list[Producto]:
        texto = texto.lower().strip()
        resultados: list[Producto] = []
        for p in self._productos.values():
            if texto in p.nombre.lower() or texto in p.categoria.lower():
                resultados.append(p)
        return resultados

    def guardar_en_archivo(self, ruta: str) -> None:
        # Usamos try/except/else/finally (como pide la guía)
        archivo = None
        try:
            archivo = open(ruta, "w", encoding="utf-8")
            for p in self.listar():
                archivo.write(p.to_linea_archivo() + "\n")
        except OSError as e:
            raise ArchivoSistemaError(f"No se pudo guardar el catálogo: {e}")
        else:
            # Si todo salió bien
            pass
        finally:
            if archivo is not None:
                archivo.close()

    def cargar_desde_archivo(self, ruta: str) -> bool:
        archivo = None
        try:
            archivo = open(ruta, "r", encoding="utf-8")
            self._productos.clear()
            for linea in archivo:
                if linea.strip() == "":
                    continue
                producto = Producto.desde_linea_archivo(linea)
                self._productos[producto.producto_id] = producto
            return True
        except FileNotFoundError:
            return False
        except (OSError, ValueError) as e:
            raise ArchivoSistemaError(f"No se pudo cargar el catálogo: {e}")
        finally:
            if archivo is not None:
                archivo.close()
