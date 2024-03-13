def divi_ex(div,divs):
    co = div//divs
    res = div % divs
    return co, res

div = int(input("dividendo: "))
divs = int(input("divisor: "))

co, res =divi_ex(div, divs)

if res == 0:
    print("la division es exacta. ")
else:
    print("la division no es exacta. ")
print("cociente", co)
print("resto", res)        