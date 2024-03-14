def determinarc(caracter):
    if caracter.isalpha():
        if caracter:isupper():
        print("es una letra mayucula.")
        else:
        print("es una letra minuscula")
    elif caracter.isdigit():
        print("es un numero.")
    else:
        print("no es ni letra ni numero.")

caracter = input("ingrese un caracter")  
determinarc(caracter)



