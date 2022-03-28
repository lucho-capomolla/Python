# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. 
# Definir los métodos y atributos, para mostrar los datos y un mensaje con el resultado de la nota.

class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
    def valoracion(self):
        if self.nota < 6:
            print(f"{self.nombre} no ha aprobado.")
        else:
            print(f"{self.nombre} ha aprobado.")


if __name__ == "__main__":
    alumnos = []
    alumno1 = Alumno("Pepe", 8)
    alumnos.append(alumno1)
    alumno2 = Alumno("Juan Carlos", 4)
    alumnos.append(alumno2)
    alumno3 = Alumno("Maripan", 7)
    alumnos.append(alumno3)

    for alumno in alumnos:
        alumno.mostrar()
        alumno.valoracion()
        print("\n")
    