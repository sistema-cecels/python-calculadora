print("====== CALCULADORA ======")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")

opcion = input("Seleccione una opcion:")

if opcion == "1":
    primer_numero = float(input("Escribe el primer numero:"))
    segundo_numero = float(input("Escribe el segundo numero:"))
    resultado = primer_numero + segundo_numero
    print("El resultado es:",resultado)

elif opcion == "2":
    print("Elegiste restar")
elif opcion == "3":
    print("Elegiste multiplicar")
elif opcion == "4":
    print("Elegiste dividir")
elif opcion == "5":
    print("Hasta luego")

else:
    print("Opcion no valida")
