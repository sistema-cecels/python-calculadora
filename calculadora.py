def mostrar_menu():
    print("====== CALCULADORA ======")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def pedir_numeros():
    primer_numero = float(input("Escribe el primer numero:"))
    segundo_numero = float(input("Escribe el segundo numero:"))

    return primer_numero, segundo_numero

def calcular(operacion):
    try:
        primer_numero, segundo_numero = pedir_numeros()
        if operacion == "+":
            resultado = primer_numero + segundo_numero
        elif operacion == "-":
            resultado = primer_numero - segundo_numero
        elif operacion == "*":
            resultado = primer_numero * segundo_numero
        elif operacion == "/":
            resultado = primer_numero / segundo_numero

        print("El resultado es:", resultado)
        input("Presiona ENTER para continuar...")
    except ValueError: 
        print("Entrada inválida. Debes escribir un número.")
        input("Presiona ENTER para continuar...")
    except ZeroDivisionError:
        print("No puedes dividir por 0")
        input("Presiona ENTER para continuar...")
    

while True:
    mostrar_menu()

    opcion = input("Seleccione una opcion:")

    if opcion == "1":
        calcular("+")

    elif opcion == "2":
        calcular("-")

    elif opcion == "3":
        calcular("*")

    elif opcion == "4":
        calcular("/")
    elif opcion == "5":
        print("Hasta luego")
        break
    else:
        print("Opcion no valida")
