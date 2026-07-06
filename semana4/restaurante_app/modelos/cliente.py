class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.pedidos = []

    def agregar_pedido(self, producto):
        self.pedidos.append(producto)

    def mostrar_pedido(self):
        print(f"\nPedido de {self.nombre}:")
        total = 0

        for producto in self.pedidos:
            print(f"- {producto.nombre}: ${producto.precio:.2f}")
            total += producto.precio

        print(f"Total a pagar: ${total:.2f}")
