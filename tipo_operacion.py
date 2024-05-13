import os

def switch_case(opcion):
    return {
        1: "Suma",
        2: "Resta",
        3: "Multiplicación",
        4: "División"
    }.get(opcion, "Opción no válida, adiós!")

def operacion (opcion_elegida, n1, n2):
    match opcion_elegida:
        case "Suma":
            resultado = n1 + n2
            print(f'{n1} + {n2} =')
        case "Resta":
            resultado = n1 - n2
            print(f'{n1} - {n2} =')
        case "Multiplicación":
            resultado = n1 * n2
            print(f'{n1} * {n2} =')
        case "División":
            resultado = n1 / n2
            print(f'{n1} / {n2} =')
    return resultado

os.system('cls' if os.name == 'nt' else 'clear')
print("OPERACIONES DISPONIBLES")
print("-----------------------")
print("1: Suma")
print("2: Resta")
print("3: Multiplicación")
print("4: División")

opcion = int(input("Ingrese una opción: "))

opcion_elegida = switch_case(opcion)
os.system('cls' if os.name == 'nt' else 'clear')
print("--->",opcion_elegida)
n1 = float(input("Entre número 1: "))
n2 = float(input("Entre número 2: "))

final = operacion (opcion_elegida, n1, n2)
print (final)



