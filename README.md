
# Azulia 💎 — Ecommerce CLI (POO + Roles)

Azulia es una **tienda de joyería por consola** desarrollada en **Python** usando **Programación Orientada a Objetos (POO)**.  
El sistema incluye **dos roles** (ADMIN y CLIENTE), **manejo de excepciones** y **persistencia básica con archivos de texto**.

---

## ✨ Funcionalidades

### Rol ADMIN
El ADMIN puede:
- **Listar** productos del catálogo.
- **Crear** productos (id, nombre, categoría, precio).
- **Actualizar** productos (nombre / categoría / precio).
- **Eliminar** productos.
- **Guardar** el catálogo en un archivo de texto (`catalogo.txt`).

### Rol CLIENTE
El CLIENTE puede:
- **Ver** el catálogo.
- **Buscar** productos por nombre o categoría.
- **Agregar** productos al carrito (por ID y cantidad).
- **Ver carrito** con subtotales y **total a pagar**.
- **Confirmar compra**:
  - No permite compra si el carrito está vacío.
  - **Registra la compra** en `ordenes.txt` con fecha/hora, detalle y total.
  - **Vacía el carrito** después de confirmar.

---

## 🧠 Conceptos aplicados (POO)

- **Clases, atributos y métodos** para modelar la app.
- **Herencia**:
  - `Usuario` (clase base)
  - `Admin` y `Cliente` (heredan de `Usuario`)
- **Composición**:
  - `Catalogo` contiene muchos `Producto`
  - `Cliente` contiene un `Carrito`
- **Excepciones**:
  - Manejo con `try/except` y uso de excepciones estándar.
  - Excepciones personalizadas para validaciones específicas.

---

## 🧯 Manejo de errores implementado

Se controlan casos como:
- **ID de producto inexistente** → `ProductoNoEncontradoError`
- **Cantidad menor o igual a 0** → `CantidadInvalidaError`
- **Errores de lectura/escritura de archivos** → `ArchivoSistemaError`
- Errores estándar como `ValueError`, `FileNotFoundError`, `OSError`

---

## 📁 Estructura del proyecto

```text
azulia_ecommerce/
├── main.py
├── app.py
├── producto.py
├── catalogo.py
├── carrito.py
├── usuarios.py
├── excepciones.py
├── catalogo.txt      # (opcional) se crea/actualiza al guardar catálogo
└── ordenes.txt       # (obligatorio) se crea al confirmar compras
```


## Descripción de archivos
```
├── main.py        : punto de entrada de la aplicación.
├── app.py         : app.py: clase TiendaApp que coordina menús y flujo general.
├── producto.py    : clase Producto + conversión a/desde línea de archivo.
├── catalogo.py    : clase Catalogo (CRUD de productos + guardar/cargar archivo).
├── carrito.py     : clase Carrito (agregar ítems, calcular total, listar detalle).
├── usuarios.py    : clases Usuario, Admin, Cliente + registro de compras.
├── excepciones.py : excepciones personalizadas del sistema.
├── catalogo.txt      # (opcional) se crea/actualiza al guardar catálogo
└──
```
## ▶️ Cómo ejecutar
 - Abre una terminal y entra a la carpeta del proyecto:
 - cd azulia_ecommerce

## Ejecuta la app:
 - python main.py

## 📝 Formato de archivos
- catalogo.txt (opcional)

Se guarda en formato simple con separador ;:
```
==================================================
id;nombre;categoria;precio
1;Aros Luna;aros;7990
2;Collar Estrella;collares;12990
...
==================================================

Si catalogo.txt no existe, el sistema carga un catálogo inicial desde el código.

ordenes.txt (obligatorio)

Cada compra se registra con fecha/hora, cliente, detalle y total:

==================================================
AZULIA | ORDEN | 2026-01-02 12:34:56
Cliente: Jeimy
- Aros Luna (aros) x2 @ $7990 = $15980
TOTAL: $15980
==================================================
```
✅ Requisitos cumplidos (según pauta)
- App ejecutable por consola en Python.
- Roles ADMIN / CLIENTE con menús claros.
- Diseño OO con herencia + composición.
- Manejo de errores con try/except + excepciones personalizadas.

Uso de archivos:
- Guardado/carga de catálogo (recomendado).
- Registro de compras (obligatorio).
- Código legible: snake_case, indentación correcta, comentarios breves.

📌 Nota personal
Este proyecto fue desarrollado como entrega final del Módulo 4 (Programación Avanzada en Python), 
reforzando el uso de POO, excepciones y persistencia básica con archivos de texto.
