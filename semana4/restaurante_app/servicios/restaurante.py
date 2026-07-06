class Restaurante:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.menu = []
        self.clientes = []

    def agregar_al_menu(self, producto):
        self.menu.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_menu(self):
        print("\n--- MENÚ DEL RESTAURANTE ---")
        for producto in self.menu:
            producto.mostrar()

    def mostrar_clientes(self):
        print("\n--- CLIENTES REGISTRADOS ---")
        for cliente in self.clientes:
            print(f"{cliente.nombre} - Teléfono: {cliente.telefono}")
