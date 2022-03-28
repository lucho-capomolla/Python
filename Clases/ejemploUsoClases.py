class Vehiculo:
    
    # Constructor
    def __init__(self, color, velocidadMaxima, marca):
        self.color = color
        self.velocidadMaxima = velocidadMaxima
        self.velocidad = 0
        self.marca = marca
        self.encendido = False
    
    def arrancar(self):
        self.encendido = True
        print("Arrancando...")
        
    def acelerar(self):
        if self.encendido: 
            if self.velocidad == 0:
                self.velocidad = 10
            else:
                self.velocidad += 10
            print("Velocidad = " + str(self.velocidad))
        else:
            print("No se puede acelerar si no se ha arrancado.")
    
    def frenar(self):
        if self.encendido:
            if self.velocidad > 10:
                self.velocidad -= 10
            else:
                self.velocidad = 0
            print("Velocidad: " + str(self.velocidad))
        else:
            print("No se puede frenar si no se ha arrancado")
    def muestraEstado(self):
        print(f"Color: {self.color} \nMarca: {self.marca} \nVelocidadMáxima: {self.velocidadMaxima} \nVelocidadActual: {self.velocidad}")
    #pass // Para que no de error de atributos 


# Herencia
class Moto(Vehiculo):
    def __init__(self, color, velocidadMaxima, marca, ruedas=2):
        Vehiculo.__init__(self, color, velocidadMaxima, marca)
        self.ruedas = ruedas
        
    def muestraEstado(self):
        print(f"Color: {self.color} \nMarca: {self.marca} \nVelocidadMáxima: {self.velocidadMaxima} \nVelocidadActual: {self.velocidad} \nRuedas: {self.ruedas}")



class Coche(Vehiculo):
    def __init__(self, color, velocidadMaxima, marca, ruedas):
        Vehiculo.__init__(self, color, velocidadMaxima, marca)
        self.ruedas = ruedas
        
    def muestraEstado(self):
        print(f"Color: {self.color} \nMarca: {self.marca} \nVelocidadMáxima: {self.velocidadMaxima} \nVelocidadActual: {self.velocidad} \nRuedas: {self.ruedas}")





# Instancia de objetos
peugeot = Coche("Rojo", 120, "Peugeot", 4)
peugeot.arrancar()
peugeot.acelerar()
peugeot.muestraEstado()
print("\n")
renault = Coche("Verde", 130, "Renault", 4)
renault.muestraEstado()
renault.acelerar()
renault.muestraEstado()
yamaha = Moto("Azul", 140, "Yamaha", 2)
yamaha.arrancar()
yamaha.acelerar()
yamaha.acelerar()
yamaha.frenar()
yamaha.muestraEstado()


