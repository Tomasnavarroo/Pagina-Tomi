# Crear un programa que permita llevar un control stock de equipos deportivos donde todos tendran una fecha de creación, un precio, una descripción. precio_costo,precio_venta y cantidad en stock. 
# Deberá tener una función donde se pueda ingresar para un objeto una determinada cantidad vendida la cual deberá ser descontada de la cantidad en stock. 
# El programa, deberá imprimir los datos de cada clase creada y si hubo ventas de uno o varios objeto en particular fueron vendidos, deberá mostrar la cantidad original y la cantidad luego de ejetura venta.
class equipo:
    def __init__(self, nombre, precio_costo, precio_venta, descripcion, fecha_creacion):
        self.nombre = nombre
        self.precio_costo =  precio_costo
        self.precio_venta = precio_venta
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.cantidad_stock = 0
        def vender(self, cantidad):
            self.cantidad_stock -= cantidad
            return self.cantidad_stock
        class control_stock:
            def __init__(self):
                self.equipos = []
                def agregar_equipo(self, equipo):
                    self.equipos.append(equipo)
                    def imprimir_datos(self):
                        for equipo in self.equipos:
                            print(f"Nombre: {equipo.nombre}")
                            print(f"Precio de costo: {equipo.precio_costo}")
                            print(f"Precio de venta: {equipo.precio_venta}")
                            print(f"Descripción: {equipo.descripcion}")
                            print(f"Fecha de creación: {equipo.fecha_creacion}")
                            print(f"Cantidad en stock: {equipo.cantidad_stock}")
                            print(f"Cantidad vendida: {equipo.vender(1)}")
                            print("\n")
                            return self.equipos
                        control_stock = control_stock()
                        equipo1 = equipo("Pelota", 10, 20, "Pelota de futbol")
                        equipo2 = equipo("Balón", 15, 30, "Balón de basquet")
                        control_stock.agregar_equipo(equipo1)
                        control_stock.agregar_equipo(equipo2)