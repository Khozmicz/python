def suma(a, b):
    return a+b
def resta(a, b):
    return a-b
def multiplicacion(a, b):
    return a*b
def division(a, b):
    if b!=0:
        return a/b
    else: 
        print("ERROR, no se puede dividir por cero")
while True:
    n1=float(input("Cargue el valor del primer número o ingrese 0 para cerrar: "))
    if n1=="0":
        print("Calculadora cerrada")
        break

    n2=float(input("Cargue el valor del segundo número "))

    print("Entrea las opciones, elija la operación que desea realizar: ")
    print("Opción 1- Suma")
    print("Opción 2- Resta")
    print("Opción 3- Multiplicar")
    print("Opción 4- División ")
    print("Opción 5- Cerrar calculadora")

    opcion=input("Ingrese la opción de la operación a realizar: ")

    if opcion=="1":
        resultado=suma(n1,n2)
    elif opcion=="2":
        resultado=resta(n1,n2)
    elif opcion=="3":
        resultado=multiplicacion(n1,n2)
    elif opcion=="4":
        resultado=division(n1,n2)
    elif opcion=="0":
        print("Calculadora cerrada")
        break
    else:
        resultado="Opción no válida"
    
    print(f"Resultado {resultado}")
    