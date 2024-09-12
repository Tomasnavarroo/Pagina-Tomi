#crear una clase llamada calzado que tenga atributos tipo, numero, marca , origen, fechacreacion y que tenga una clase hija llamada zapatilla que tenga de atributos numero, modelo, material , stock 
class Calzado:
    def __init__(self, tipo, numero, marca, origen, fecha_creacion):
        self.tipo = tipo
        self.numero = numero
        self.marca = marca
        self.origen = origen
        self.fecha_creacion = fecha_creacion
    def mostrar_datos(self):
        print(f"Tipo:  {self.tipo}")
        print(f"numero:  {self.numero}")


class Zapatilla(Calzado):
    def __init__(self, numero, modelo, material, stock, tipo, marca, origen):
        super().__init__(tipo, numero, marca, origen,)
        self.modelo = modelo
        self.material = material
        self.stock = stock
        

