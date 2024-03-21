c1 = int(input("ingresa certamen 1:"))
c2 = int(input("ingrese certamen 2:"))
nl = int(input("ingrese laboratorio:"))


promedio = (60 -(nl *0.3))/(0.7)
nota_falt = round((promedio *3) -(c1 + c2),1)

print(f"esta es la nota: ",{nota_falt})

#que nota necesito
