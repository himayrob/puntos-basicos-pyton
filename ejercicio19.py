def calculadora(n1,n2, operador):
    if operador == '+':
        return n1 + n2
    elif operador == '-':
        return n1 - n2
    elif operador == '*':
        return n1 * n2
    elif operador == '**':
        return n1 ** n2
    elif operador == '/':
        if n2 != 0:
            return n1 /n2
        else:
            return "error: division por cero"
    else:
        return "operador no valido"    

def main():
    n1 = float(input("ingrese el primer nunero: "))
    n2 = float(input("ingrese el segundo numero"))
    operador = input("ingrese el operador")

    Resultado = calculadora(n1, n2, operador)
    print("resultado:" ,Resultado)

if __name__ == "__main__":
     main()


# def calcular(num1, num2, operador):
#     if operador == '+':
#         return num1 + num2
#     elif operador == '-':
#         return num1 - num2
#     elif operador == '*':
#         return num1 * num2
#     elif operador == '/':
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Error: división por cero"
#     else:
#         return "Operador no válido"

# def main():
#     num1 = float(input("Ingrese el primer número: "))
#     num2 = float(input("Ingrese el segundo número: "))
#     operador = input("Ingrese el operador (+, -, *, /): ")

#     resultado = calcular(num1, num2, operador)
#     print("Resultado:", resultado)

# if __name__ == "__main__":
#     main()
