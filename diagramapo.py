from abc import ABC, abstractmethod
class Persona(ABC):
    nombre=None
    edad=None
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    @abstractmethod

    def mostrar(self):
        return f"Nombre:{self.nombre}, edad: {self.edad}"

class Cliente(Persona):
    telefono_de_contacto=None

    def __init__(self, nombre, edad, telefono):
        super(). __init__(nombre,edad)
        self.telefono_de_contacto=telefono

    def mostrar(self):
        return super().mostrar(),f"Teléfono: {self.telefono_de_contacto}"

class Empleado(Persona):
    sueldo_bruto=None
    
    
    def __init__(self,nombre,edad,telefono,sueldo):
        super(). __init__(nombre, edad, telefono)
        self.sueldo_bruto=sueldo

    def calcular_salario(self):
        return self.sueldo_bruto*0.9 
    
    def mostrar(self):
        return super.mostrar(), f"Sueldo: {self.calcular_salario()}"
    
class Empresa:
    nombre=None
    empleado=None
    cliente=None

    def __init__(self):
        self.nombre="Mi Empresa"
        self.empleado=[]
        self.cliente=[]
        
    def set_nombre(self,nombre):
        self.nombre=nombre

    def agregar_empleado(self,Empleado):
        self.empleado.append(Empleado)    
    
    def agregar_cliente(self,Cliente):
        self.cliente.append(Cliente)

    def mostrar(self,nombre):
        self.nombre=nombre

class Directivo:
    categoria=None
    empleados=None

    def __init__(self,nombre,edad,sueldo_bruto,categoria):
        super().__init__(nombre,edad,sueldo_bruto)
        self.categoria=categoria
        self.empleados=[]
    
    def mostrar(self):
        return super().mostrar(),f"Soy el director de: {self.categoria}"

    def agregar_empleado(self,Empleado):
        self.empleados.append(Empleado)


mi_empresa=Empresa()
mi_empresa.set_nombre("Soluciones Python S.A.")

person=Cliente("Tomás", 27, "374017")

mi_empresa.agregar_cliente(person)

print(mi_empresa.nombre)
print(mi_empresa.cliente[0].mostrar())