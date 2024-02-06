from abc import ABC, abstractclassmethod

class Persona(ABC):
    '''Clase que representa una persona'''

    @abstractclassmethod
    def __init__(self, cedula, nombre, apellido):
        self.cedula=cedula
        self.nombre=nombre
        self.apellido=apellido

    @abstractclassmethod
    def __str__(self):
        return "%s: %s, %s" % (str(self.cedula),self.apellido, self.nombre)
    
class Alumno(Persona):
    '''Clase que representa a un alumno'''
    
    def __init__(self, cedula: str, nombre: str, apellido: str, carrera: str):
        #llamar al constructor de Persona
        Persona.__init__(cedula, nombre, apellido )
        #agregamos el nuevo atributo
        self.carrera=carrera
    
    def __str__(self):
        return f"{Persona. __str__()}, Carrera: {self.carrera}"

if __name__=='__main__':
    #crear un objeto del tipo alumno
    alumno_prueba=Alumno("5864223", "Jose", "Rojas", "Contabilidad")
    print(alumno_prueba)