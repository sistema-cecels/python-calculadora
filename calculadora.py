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

def sumar():      
        try:
            primer_numero, segundo_numero = pedir_numeros()
            resultado = primer_numero + segundo_numero

            print("El resultado es:",resultado)
            input("Presiona ENTER para continuar...")

        except ValueError: 
            print("Entrada inválida. Debes escribir un número.")
def resta():
        try:
            primer_numero, segundo_numero = pedir_numeros()
            resultado = primer_numero - segundo_numero

            print("El resultado es:",resultado)
            input("Presiona ENTER para continuar...")

        except ValueError: 
            print("Entrada inválida. Debes escribir un número.")
def multiplicar():
        try:
            primer_numero, segundo_numero = pedir_numeros()
            resultado = primer_numero * segundo_numero

            print("El resultado es:",resultado)
            input("Presiona ENTER para continuar...")

        except ValueError: 
            print("Entrada inválida. Debes escribir un número.")
    
def dividir():
        try:
            primer_numero, segundo_numero = pedir_numeros()
            resultado = primer_numero / segundo_numero

            print("El resultado es:",resultado)
            input("Presiona ENTER para continuar...")

        except ValueError: 
            print("Entrada inválida. Debes escribir un número.")
    

while True:
    mostrar_menu()

    opcion = input("Seleccione una opcion:")

    if opcion == "1":
        sumar()

    elif opcion == "2":
        resta()

    elif opcion == "3":
        multiplicar()

    elif opcion == "4":
        dividir()
    elif opcion == "5":
        print("Hasta luego")
        break
    else:
        print("Opcion no valida")
