# Restaurante App

Aplicación simple en Python para modelar un restaurante con:
- Menú (lista de productos)
- Registro de clientes
- Pedidos por cliente
- Activación/desactivación de productos (Disponible/Agotado)

---

## Estructura del proyecto

- `main.py`: Script principal que crea el restaurante, productos, clientes y simula pedidos.
- `modelos/producto.py`: Clase `Producto`.
- `modelos/cliente.py`: Clase `Cliente`.
- `servicios/restaurante.py`: Clase `Restaurante`.

---

## Cómo funciona

### 1) Producto
Un `Producto` tiene:
- `codigo`
- `nombre`
- `precio`
- `activo` (True/False)

Métodos:
- `desactivar_producto()`: marca el producto como no disponible.
- `mostrar()`: imprime el producto indicando si está `Disponible` o `Agotado`.

### 2) Cliente
Un `Cliente` tiene:
- `nombre`
- `telefono`
- `pedidos` (lista de productos)

Métodos:
- `agregar_pedido(producto)`: agrega un producto al pedido.
- `mostrar_pedido()`: imprime el pedido y el total a pagar.

### 3) Restaurante
Un `Restaurante` tiene:
- `nombre`
- `direccion`
- `menu` (lista de productos)
- `clientes` (lista de clientes)

Métodos:
- `agregar_al_menu(producto)`
- `registrar_cliente(cliente)`
- `mostrar_menu()`
- `mostrar_clientes()`

---

## Ejecución

Desde la carpeta del proyecto `restaurante_app/` ejecuta:

```bash
python main.py
```

---

## Ejemplo de salida (resumen)

- Imprime restaurante y dirección.
- Muestra el menú con productos y su estado.
- Muestra clientes registrados.
- Muestra los pedidos de cada cliente y el total.

---

## Notas

- En el `main.py` se usa `papas.desactivar_producto()` para cambiar el estado del producto antes de mostrar el menú.

