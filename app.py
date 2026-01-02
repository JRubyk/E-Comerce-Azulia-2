from catalogo import Catalogo
from producto import Producto
from usuarios import Admin, Cliente
from excepciones import (
    ProductoNoEncontradoError,
    CantidadInvalidaError,
    ArchivoSistemaError,
)


class TiendaApp:
    """Coordina la ejecución y menús (controlador principal)."""

    def __init__(self) -> None:
        self.catalogo = Catalogo()
        self.ruta_catalogo = "catalogo.txt"
        self.ruta_ordenes = "ordenes.txt"

    def iniciar(self) -> None:
        # Intentar cargar catálogo desde archivo; si no existe, cargar inicial
        try:
            cargo = self.catalogo.cargar_desde_archivo(self.ruta_catalogo)
            if not cargo:
                self.catalogo.cargar_inicial()
        except ArchivoSistemaError as e:
            print(f"[ERROR] {e}")
            print("Se cargará un catálogo inicial por seguridad.")
            self.catalogo.cargar_inicial()

        while True:
            print("\n=== AZULIA | Joyería por consola ===")
            print("Elige tu rol:")
            print("1) ADMIN")
            print("2) CLIENTE")
            print("0) Salir")

            opcion = input("Opción: ").strip()
            if opcion == "1":
                self.menu_admin()
            elif opcion == "2":
                self.menu_cliente()
            elif opcion == "0":
                print("¡Gracias por visitar Azulia!")
                break
            else:
                print("Opción inválida. Intenta de nuevo.")

    # ---------------- ADMIN ----------------

    def menu_admin(self) -> None:
        admin = Admin("Admin Azulia")
        while True:
            print(f"\n--- Menú {admin.rol()} ---")
            print("1) Listar productos")
            print("2) Crear producto")
            print("3) Actualizar producto")
            print("4) Eliminar producto")
            print("5) Guardar catálogo en archivo")
            print("0) Volver")

            opcion = input("Opción: ").strip()

            if opcion == "1":
                self.imprimir_catalogo()

            elif opcion == "2":
                self.admin_crear_producto()

            elif opcion == "3":
                self.admin_actualizar_producto()

            elif opcion == "4":
                self.admin_eliminar_producto()

            elif opcion == "5":
                try:
                    self.catalogo.guardar_en_archivo(self.ruta_catalogo)
                    print(f"Catálogo guardado en '{self.ruta_catalogo}'.")
                except ArchivoSistemaError as e:
                    print(f"[ERROR] {e}")

            elif opcion == "0":
                break
            else:
                print("Opción inválida.")

    def admin_crear_producto(self) -> None:
        try:
            producto_id = int(input("ID (entero): "))
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            precio = float(input("Precio (>0): "))

            if precio <= 0:
                raise ValueError("El precio debe ser mayor que 0.")
            if nombre == "" or categoria == "":
                raise ValueError("Nombre y categoría no pueden estar vacíos.")

            nuevo = Producto(producto_id, nombre, categoria, precio)
            self.catalogo.agregar(nuevo)
            print("Producto creado:", nuevo)

        except ValueError as e:
            print(f"[ERROR] Datos inválidos: {e}")

    def admin_actualizar_producto(self) -> None:
        try:
            producto_id = int(input("ID del producto a actualizar: "))
            producto = self.catalogo.obtener_por_id(producto_id)
            print("Producto actual:", producto)
            print("Deja vacío para no cambiar un campo.")

            nombre = input("Nuevo nombre: ")
            categoria = input("Nueva categoría: ")
            precio_txt = input("Nuevo precio: ").strip()

            precio = None
            if precio_txt != "":
                precio = float(precio_txt)

            self.catalogo.actualizar(producto_id, nombre, categoria, precio)
            print("Producto actualizado:", self.catalogo.obtener_por_id(producto_id))

        except ProductoNoEncontradoError as e:
            print(f"[ERROR] {e}")
        except ValueError as e:
            print(f"[ERROR] Datos inválidos: {e}")

    def admin_eliminar_producto(self) -> None:
        try:
            producto_id = int(input("ID del producto a eliminar: "))
            self.catalogo.eliminar(producto_id)
            print("Producto eliminado.")
        except ProductoNoEncontradoError as e:
            print(f"[ERROR] {e}")
        except ValueError:
            print("[ERROR] Debes ingresar un ID válido (entero).")

    # ---------------- CLIENTE ----------------

    def menu_cliente(self) -> None:
        nombre = input("Nombre del cliente: ").strip()
        if nombre == "":
            nombre = "Cliente Anónimo"
        cliente = Cliente(nombre)

        while True:
            print(f"\n--- Menú {cliente.rol()} | {cliente.nombre} ---")
            print("1) Ver catálogo")
            print("2) Buscar por nombre o categoría")
            print("3) Agregar producto al carrito")
            print("4) Ver carrito y total")
            print("5) Confirmar compra")
            print("0) Volver")

            opcion = input("Opción: ").strip()

            if opcion == "1":
                self.imprimir_catalogo()

            elif opcion == "2":
                texto = input("Buscar (nombre o categoría): ")
                resultados = self.catalogo.buscar(texto)
                if len(resultados) == 0:
                    print("No se encontraron productos.")
                else:
                    print("\nResultados:")
                    for p in resultados:
                        print("-", p)

            elif opcion == "3":
                self.cliente_agregar_al_carrito(cliente)

            elif opcion == "4":
                self.imprimir_carrito(cliente)

            elif opcion == "5":
                self.cliente_confirmar_compra(cliente)

            elif opcion == "0":
                break
            else:
                print("Opción inválida.")

    def cliente_agregar_al_carrito(self, cliente: Cliente) -> None:
        try:
            producto_id = int(input("ID del producto: "))
            cantidad = int(input("Cantidad (>0): "))

            producto = self.catalogo.obtener_por_id(producto_id)
            cliente.carrito.agregar(producto, cantidad)

            print("Agregado al carrito:", producto, f"x{cantidad}")

        except ProductoNoEncontradoError as e:
            print(f"[ERROR] {e}")
        except CantidadInvalidaError as e:
            print(f"[ERROR] {e}")
        except ValueError:
            print("[ERROR] Debes ingresar números válidos (ID y cantidad enteros).")

    def imprimir_carrito(self, cliente: Cliente) -> None:
        if cliente.carrito.esta_vacio():
            print("Tu carrito está vacío.")
            return

        print("\n--- Carrito ---")
        detalle = cliente.carrito.detalle()
        for item in detalle:
            print(
                f"- {item['nombre']} | {item['categoria']} | "
                f"x{item['cantidad']} | ${item['precio_unitario']:.0f} c/u | "
                f"Subtotal: ${item['subtotal']:.0f}"
            )
        print(f"TOTAL A PAGAR: ${cliente.carrito.total():.0f}")

    def cliente_confirmar_compra(self, cliente: Cliente) -> None:
        if cliente.carrito.esta_vacio():
            print("[AVISO] No puedes confirmar compra: el carrito está vacío.")
            return

        self.imprimir_carrito(cliente)
        confirmar = input("¿Confirmar compra? (s/n): ").strip().lower()
        if confirmar != "s":
            print("Compra cancelada.")
            return

        try:
            cliente.registrar_compra(self.ruta_ordenes)
            cliente.carrito.vaciar()
            print("¡Compra confirmada! Se registró en 'ordenes.txt' y el carrito se vació.")
        except ArchivoSistemaError as e:
            print(f"[ERROR] {e}")

    # ---------------- Utilidades ----------------

    def imprimir_catalogo(self) -> None:
        print("\n--- Catálogo Azulia ---")
        productos = self.catalogo.listar()
        if len(productos) == 0:
            print("(Catálogo vacío)")
        else:
            for p in productos:
                print("-", p)
