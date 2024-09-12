class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio
    def mostrar_datos(self):
        print(f"Llantas: {self.llantas}")
        print(f"Color: {self.color}")
        print(f"Precio: {self.precio}")
    def aplicar_descuento(self):
        if self.precio > 100000:
            self.precio *= 0.9
            print("Se ha aplicado un descuento del 10%")
        else:
            print("No se ha aplicado descuento")


class Moto(Fabrica):
    def __init__(self, llantas, color, precio, cilindrada):
        super().__init__(llantas, color, precio)
        self.cilindrada = cilindrada
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Cilindrada: {self.cilindrada}")



class Carro(Fabrica):
    def __init__(self, llantas, color, precio, puertas):
        super().__init__(llantas, color, precio)
        self.puertas = puertas
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Puertas: {self.puertas}")

# Crear objetos
moto = Moto(2, "Rojo", 80000, 250)
carro = Carro(4, "Azul", 150000, 4)
moto = Moto(2, "azul", 80000, 250)
carro = Carro(4, "verde", 150000, 4)

# Mostrar datos
moto.mostrar_datos()
print()
carro.mostrar_datos()
print()
# Aplicar descuento
moto.aplicar_descuento()
print(f"Precio final moto: {moto.precio}")
carro.aplicar_descuento()
print(f"Precio final carro: {carro.precio}")