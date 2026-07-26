# Sistema de Gestión de Restaurante - POO en Python

**Estudiante:** Kerly Keila Salazar Franco
**Asignatura:** Programación Orientada a Objetos
**Tarea:** Semana 4 - Organización Modular

---

## Descripción del Sistema
Este software implementa una solución básica para administrar el consumo de clientes en un establecimiento gastronómico, desarrollado bajo el paradigma de **Programación Orientada a Objetos (POO)** en Python.

El sistema permite:
- Registrar y mantener un catálogo de productos (platos, bebidas, extras) con sus precios y características.
- Gestionar la información de cada cliente y registrar los productos que consumen.
- Calcular el total de la cuenta de forma automática.
- Emitir la factura o cierre de cuenta al finalizar el servicio.

Toda la lógica de negocio se centraliza en un servicio de control, facilitando actualizaciones y mantenimiento sin afectar las partes fundamentales del sistema.

---

## Estructura del Proyecto
```text
restaurante_app/
├── modelos/
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   └── restaurante.py
├── main.py
└── README.md
 
 
 
Reflexión
 
Dividir el código en módulos y asignar responsabilidades claras a cada archivo es fundamental en el desarrollo de software por estas razones:
 
- Mantenibilidad: Al separar los datos y entidades ( modelos/ ) de la lógica de operación ( servicios/ ), podemos modificar una parte sin dañar la otra. Por ejemplo, si cambian las reglas de facturación o impuestos, solo editamos el archivo correspondiente sin tocar la definición de Producto o Cliente.
- Legibilidad: Tener un archivo  main.py  limpio, sin mezclar definiciones de clases con ejecución, permite que cualquier persona que revise el código entienda rápidamente cómo funciona el flujo completo del sistema.
- Reutilización: Las clases que definen a los productos o clientes quedan independientes, por lo que más adelante podrían usarse en otros sistemas como una página web o aplicación móvil, sin tener que volver a escribirlas.
- Escalabilidad: Esta estructura nos permite agregar nuevas funcionalidades (como reservas, reportes o control de inventario) creando nuevos archivos o carpetas, sin desordenar lo que ya está funcionando.