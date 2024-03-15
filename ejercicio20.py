from time import localtime

def calcular_edad(dia_nacimiento, mes_nacimiento, anno_nacimiento):
    t = localtime()
    dia_actual = t.tm_mday
    mes_actual = t.tm_mon
    anno_actual = t.tm_year

    edad = anno_actual - anno_nacimiento

    if(mes_actual, dia_actual) < (mes_nacimiento, dia_nacimiento):
        edad -=1

    return edad

def main():

    dia_nacimiento = int(input("ingrese el dia de su fecha de nacimiento: "))
    mes_nacimiento = int(input("ingrese el mes de nacimiento: "))
    anno_nacimiento = int(input("ingrese el año de su fecha de naciemiento: "))

    edad = calcular_edad(dia_nacimiento, mes_nacimiento, anno_nacimiento)
    print(f"usted tiene {edad} años.")

if __name__ == "__main__":
    main()    
    # date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1]) 