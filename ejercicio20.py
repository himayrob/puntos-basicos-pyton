#triangulos
def verificar_triangulo():
    a=float(input("ingrese lado a"))
    b=float(input("ingrese lado b"))
    c=float(input("ingrese lado c"))

    def triangulo(a, b, c):

        if a >= b*2 or a >= c*2:
            return "triangulo invalido"
        elif b>= a*2 or b>=c*2:
            return "triangulo invalido"
        elif c>= a*2 or c>=b*2:
            return "triangulo invalido"
        else:
            return "operacioninvalida"
        
    print(triangulo(a, b, c))

while True:
    verificar_triangulo()
    respuesta = input("¿Desea verificar otro conjunto de lados? (s/n): ")
    if respuesta.lower() != 's':
        break