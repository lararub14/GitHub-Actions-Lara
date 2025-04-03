def calculadora():
    print("Calculadora en Python")
    print("Elige una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    try:
        operacion = int(input("Selecciona una opción (1-4): "))
        if operacion not in [1, 2, 3, 4]:
            print("Operación no válida")
            return

        cantidad_numeros = int(input("¿Cuántos números quieres ingresar?: "))
        numeros = []
        for i in range(cantidad_numeros):
            num = float(input(f"Ingresa el número {i+1}: "))
            numeros.append(num)

        if operacion == 1:
            resultado = sum(numeros)
            print(f"Resultado de la suma: {resultado}")
        elif operacion == 2:
            resultado = numeros[0] - sum(numeros[1:])
            print(f"Resultado de la resta: {resultado}")
        elif operacion == 3:
            resultado = 1
            for num in numeros:
                resultado *= num
            print(f"Resultado de la multiplicación: {resultado}")
        elif operacion == 4:
            resultado = numeros[0]
            try:
                for num in numeros[1:]:
                    resultado /= num
                print(f"Resultado de la división: {resultado}")
            except ZeroDivisionError:
                print("Error: División por cero no permitida.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


if __name__ == "__main__":
    calculadora()
