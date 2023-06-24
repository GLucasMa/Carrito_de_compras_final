"""
Crear un carrito de compras en Python que funcione únicamente en la consola. 

El programa debe presentar un menú con las siguientes opciones:Mostrar productos en detalle: 
Muestra el código del producto, nombre, marca, precio, stock, color y características de cada producto en la tienda.

Mostrar información breve del producto: Muestra el código del producto, nombre, precio y cantidad
disponible de cada producto en la tienda.

Buscar producto por código: Permite al usuario ingresar un código de producto y muestra la información detallada
de ese producto.

Realizar compra: Permite al usuario agregar productos al carrito de compras.
Se generará un nuevo diccionario con el nombre del producto, la cantidad comprada, 
el precio unitario y el costo total por cada item añadido.

Finalizar compra: Cierra la compra y muestra un detalle de los productos comprados, incluyendo el nombre, 
la cantidad, el precio unitario y el costo total.

Salir: Permite al usuario salir del programa.

El programa debe mostrar al usuario un diccionario con la información de los productos disponibles en la tienda.
Debe validar las opciones seleccionadas por el usuario en el menú.
Mientras el usuario esté navegando en el carrito de compras, los datos deben permanecer disponibles. 
Deberá contar el programa con una visualización previa de los productos añadidos en el carrito en la cual
se le consulte al usuario si está conforme o no con los productos añadidos , teniendo en cuenta el desarrollo 
que pueda desencadenar si el usuario desea MODIFICAR lo que tiene en el carrito , es decir que si desea modificar 
lo que tiene en el carrito pueda modificar la cantidad de un producto determinado , para aumentar o disminuir 
la cantidad o eliminar del carrito completamente algún producto.
El programa debe incluir una opción en el menú para cerrar la compra y mostrar un detalle de los productos comprados.
Además, se debe actualizar permanentemente el stock de los productos y validar la existencia de la cantidad de 
productos antes de realizar una compra. 
También se debe validar que el resultado total de la compra pueda incluir números decimales.
Para buscar productos, se debe validar el ingreso del ID del producto.
Por cada acción que el usuario seleccione, se debe validar si la respuesta es 'SI' o 'NO'."
Se validará todos los ingresos y egresos de información del sistema.
Este programa debe ser una réplica de  todas las aplicaciones de compras en línea conocidas. 
"""

import os
class CarritoCompras:
    def __init__(self):
        self.diccionario_de_productos = {
            "1000": {
                "Nombre": "Motorola Moto G52",
                "Marca": "Motorola",
                "Precio": 93599,
                "Stock": 15,
                "Color": "Azul",
                "Caracteristicas": """
                # Visión ultra wide, con un campo de visión de 123 grados, cuenta con sonido multidimensional 
                # Pantalla ultra amplia, full HD, de 6,5 pulgadas. cámara gran angular y sistema de triple lente. 
                # Batería de 5000 mAh.  6 GB de memoria RAM, 128 GB de almacenamiento interno 
                # Procesador Octa Core ultra veloz. Sistema operativo Android 12.\n"""
            },
            "1001": {
                "Nombre": "Motorola Moto E13",
                "Marca": "Motorola",
                "Precio": 46900,
                "Stock": 15,
                "Color": "Violeta",
                "Caracteristicas": """
                # Pantalla (720 x 1600) HD+. Procesador Octa core 1.6 GHz. Sistema operativo Android Go 13. 
                # Almacenamiento 64Gb Expandible hasta 512Gb. RAM 2Gb. Tarjeta de Memoria Micro SD. Tarjeta nano SIM. 
                # Bateria 5000mAh. Carga turbo 10w. Camara principal 13Mp. Frontal 5Mp. Camara rapida. 
                # Sensores: acelerometro, sensor de proximidad, luz ambiente y desbloqueo facial.\n"""
            },
            "1002": {
                "Nombre": "Motorola Moto G32",
                "Marca": "Motorola",
                "Precio": 88999,
                "Stock": 23,
                "Color": "Gris",
                "Caracteristicas": """
                # Pantalla IPS de 6.49. Relacion aspecto 20:9. Resolucion 1080 x 2400
                # Procesador Qualcomm Snapdragon 680 Octa core (2.4GHz). Capacidad 128 Gb (expandible hasta 1Tb)/RAM 4Gb. 
                # Camara Principal: 50MP (74.26)F1.8Gran Angular: 8MP (118) F2.2Macro: 2MP (88) F2.2.  
                # Lector de tarjetas micro SD. Sistema operativo Android 12. Bateria de 5000 mAh. 
                # Huella dactilar, Luz ambiente. Desbloqueo facial.\n"""
            },
            "1003": {
                "Nombre": "Samsung Galaxy A04e",
                "Marca": "Samsung",
                "Precio": 52000,
                "Stock": 8,
                "Color": "Rojo",
                "Caracteristicas": """
                # Pantalla PLS de 6.5". Tiene 2 cámaras traseras de 13Mpx/2Mpx.Cámara delantera de 5Mpx.
                # Procesador MediaTek Helio P35 Octa-Core de 2.3GHz con 3GB de RAM. Batería de 5000mAh.
                # Memoria interna de 64GB. Con reconocimiento facial.
                # 64GB de memoria y 3GB de memoria RAM.\n"""
            },
            "1004": {
                "Nombre": "Xiaomi Redmi Note 11",
                "Marca": "Xiaomi",
                "Precio": 109000,
                "Stock": 2,
                "Color": "Negro",
                "Caracteristicas": """
                # Pantalla de 6.43". Procesador Snapdragon 680 8ta Core. Capacidad 128 Gb / RAM 4 Gb. 
                # Camara Principal 50MP+ Ultra Gran Angular 8MP + Macro 2MP + Profundidad 2MP / Frontal 13 mp. 
                # Slot para tarjetas micro sd extensible 1T. Sistema operativo Android 11 / MIUI 13. Bateria de 5000 mAh.\n"""
            }

        }

        self.carrito = {}

    def mostrarProductos(self):
        print("==================================================================================================================\n")
        for codigo, producto in self.diccionario_de_productos.items():
            print("Código:", codigo)
            print("Nombre:", producto["Nombre"])
            print("Marca:", producto["Marca"])
            print("Precio:", producto["Precio"])
            print("Stock:", producto["Stock"])
            print("Color:", producto["Color"])
            print("Características:", producto["Caracteristicas"])
            print("==================================================================================================================\n")


    def mostrarInfoBreve(self):
        print("==================================================================================================================\n")
        for codigo, producto in self.diccionario_de_productos.items():
            print("Código:", codigo)
            print("Nombre:", producto["Nombre"])
            print("Precio:", producto["Precio"])
            print("Cantidad Disponible:", producto["Stock"])
            print("==================================================================================================================\n")


    def buscarPorCodigo(self, codigo):
        producto = self.diccionario_de_productos.get(codigo)
        if producto:
            print("Detalles del producto (Código:", codigo, "):")
            print("Nombre:", producto["Nombre"])
            print("Marca:", producto["Marca"])
            print("Precio:", producto["Precio"])
            print("Stock:", producto["Stock"])
            print("Color:", producto["Color"])
            print("Características:", producto["Caracteristicas"])
        else:
            print("Producto no encontrado.")

    def realizarCompra(self):
        codigo = input("Ingrese el código del producto que desea comprar: ")

        producto = self.diccionario_de_productos.get(codigo)
        if producto:
            try:
                cantidad = int(input("Ingrese la cantidad que desea comprar: "))
            except ValueError:
                print("Esta cantidad no puede ser agregada al carrito, o introdujo un valor inválido.")
                cantidad = int(input("Intente de nuevo: "))

            if cantidad <= producto["Stock"]:
                nombre = producto["Nombre"]
                precio_unitario = producto["Precio"]
                costo_total = precio_unitario * cantidad

                self.carrito[codigo] = {
                    "Nombre": nombre,
                    "Cantidad": cantidad,
                    "Precio Unitario": precio_unitario,
                    "Costo Total": costo_total
                }

                print("Producto agregado al carrito.")
                producto["Stock"] -= cantidad
            else:
                print("No hay suficiente stock.")
        else:
            print("Producto no encontrado.")

    def mostrarCarrito(self):
        print("Productos en el carrito de compras:")
        for codigo, producto in self.carrito.items():
            print("Código:", codigo)
            print("Nombre:", producto["Nombre"])
            print("Cantidad:", producto["Cantidad"])
            print("Precio Unitario:", producto["Precio Unitario"])
            print("Costo Total:", producto["Costo Total"])
            print("\n")

    def modificarCarrito(self):
        while True:
            self.mostrarCarrito()
            opcion = input("¿Desea modificar el carrito de compras? (SI/NO): \n")
            if opcion.upper() == "NO":
                break

            codigo = input("Ingrese el código del producto que desea modificar: \n")
            producto = self.carrito.get(codigo)
            if producto:
                cantidad_actual = producto["Cantidad"]
                cantidad_nueva = int(input("Ingrese la nueva cantidad (actual: {}): ".format(cantidad_actual)))

                if cantidad_nueva == 0:
                    del self.carrito[codigo]
                    print("Producto eliminado del carrito de compras.")
                else:
                    producto["Cantidad"] = cantidad_nueva
                    producto["Costo Total"] = producto["Precio Unitario"] * cantidad_nueva
                    print("Cantidad modificada.")

                producto_disponible = self.diccionario_de_productos.get(codigo)
                if producto_disponible:
                    cantidad_disponible = producto_disponible["Stock"]
                    producto_disponible["Stock"] += cantidad_actual - cantidad_nueva
            else:
                print("Producto no encontrado.")

    def finalizarCompra(self):
        print("Detalle de los productos comprados:")
        for codigo, producto in self.carrito.items():
            print("Código:", codigo)
            print("Nombre:", producto["Nombre"])
            print("Cantidad:", producto["Cantidad"])
            print("Precio Unitario:", producto["Precio Unitario"])
            print("Costo Total:", producto["Costo Total"])
            print()

        total = sum(producto["Costo Total"] for producto in self.carrito.values())
        print("Total a pagar:", total)

    def Menu(self):
        while True:
            print("""Bienvenido a multicompras, seleccione con un numero la opcion que desea:

1) Mostrar productos en detalle 
2) Mostrar información breve del producto
3) Buscar producto por codigo
4) Realizar compra  
5) Modificar carrito
6) Finalizar compra 
7) Salir
""")

            opcion = input("Seleccione una opción: ")
            print()

            if opcion == "1":
                print("Usted se encuentra en el apartado de detalles del producto\n")
                self.mostrarProductos()
            elif opcion == "2":
                print("Usted se encuentra en el apartado de información breve del producto\n")
                self.mostrarInfoBreve()
            elif opcion == "3":
                print("Estas en nuestro motor de busqueda, el cual funciona por código.\n")
                codigo = input("Ingrese el código del producto: ")
                self.buscarPorCodigo(codigo)
            elif opcion == "4":
                print("En este apartado podras realizar la compra ¿que fué lo que te interesó?\n")
                self.realizarCompra()
            elif opcion == "5":
                self.modificarCarrito()
            elif opcion == "6":
                print("Ya casi es tuyo! estas por finalizar la compra\n")
                self.finalizarCompra()
                print("¡Muchas gracias! vuelva pronto\n")
                break
            elif opcion == "7":
                print("¡Muchas gracias! vuelva pronto\n")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.\n")
            print()

carrito = CarritoCompras()
carrito.Menu()
