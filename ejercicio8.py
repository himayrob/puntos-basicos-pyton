num = float(input("ingrese un numero: "))

if num <= 0:
    abs_numero = abs(num)
    parte_decimal = abs_numero + int(num)
else:
    parte_decimal = num - int(num) 

numaprox=round(parte_decimal,2)

print("el decimal es", numaprox)

#parte decimal