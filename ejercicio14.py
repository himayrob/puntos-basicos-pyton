def palabra_larga(p1, p2):
    lp1 = len(p1)
    lp2 = len(p2)

    if lp1 > lp2:
        diferencia = lp1 - lp2
        return p1,diferencia
    elif lp2 > lp1:
        diferencia = lp2 - lp1
        return p2,diferencia
    else:
        return "ambas son iguales", 0

p1 = input("ingrese palabra 1: ")
p2 = input("ingrese palabra 2: ")

palabra_larga, diferencia = palabra_larga(p1, p2)

print(f"la palabra mas larga es '{palabra_larga}' y tiene diferencia de {diferencia} letras.")
#palabra mas larga
