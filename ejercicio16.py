def determinarc(escribir):
    if escribir.isalpha():
        if escribir.isupper():
            print("es una letra mayucula.")
        else:
            print("es una letra minuscula")
    elif escribir.isdigit():
        print("es un numero.")
    else:
        print("no es ni letra ni numero.")

escribir = input("ingrese un escribir")  
determinarc(escribir)

#letra o numero

# def determinarc(caracter):
#     if caracter.isalpha():
#         if caracter.isupper():
#             print("Es una letra mayúscula.")
#         else:
#             print("Es una letra minúscula.")
#     elif caracter.isdigit():
#         print("Es un número.")
#     else:
#         print("No es ni una letra ni un número.")

# caracter = input("Ingrese un caracter: ")  
# determinarc(caracter)
