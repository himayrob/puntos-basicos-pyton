def par(numero):
    if numero %2 == 0:
        return True
    else: 
        return False
        
numero = int(input("ingrese su numero: "))
if par(numero):
     print("es par")
else:
     print("es impar")     
     