class Persona:
    def __init__(self, nombre):
        self.nombre=nombre
    
    def avanza(self):
        print("Hola soy",self.nombre,",Ando caminando")

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print("Hola soy",self.nombre,", Ando moviéndome en bicicleta")

if __name__ == "__main__":
    persona=Persona("Tomás")
    persona.avanza()

    ciclista=Ciclista("Dario")
    ciclista.avanza()