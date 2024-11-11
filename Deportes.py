class Deportes: 
    def__init__(self, Equipo, jugadores, cancha, pelota):
    self.Equipo = Equipo
    self.jugadores = jugadores
    self.cancha = cancha
    self.pelota = pelota
    
    def mostrar(self):
        print("Equipo", self.Equipo, "jugadores", self.jugadores, "cancha", self.cancha, "pelota", self.pelota)
        
Deportes = Deportes("futbol",11,1,20)
Deportes = Deportes("Beisbol",2,9)
Deportes = Deportes("Basquet",12,5,5)