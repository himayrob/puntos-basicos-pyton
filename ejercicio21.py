#indice de masa corporal
p =float(input("ingrese peso"))
a =float(input("ingrese altura"))
e= int(input("ingrese edad"))

def imcEdad(p, a, e):
    imc =p/(a**2)
    if imc <22.0 and e <45:
        return "el riesgo es bajo"
    elif imc >= 22.0 and e <45:
        return "el riesgo es medio"
    elif imc <22.0 and e >=45:
        return "el riesgo es medio"
    elif imc >= 22.0 and e >=45:
        return "el riesgo es alto"
    
print(imcEdad(p, a, e)) 