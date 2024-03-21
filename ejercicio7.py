def calcular_hora_futura(hora_actual, horas_por_avanzar):

      hora_futura = (hora_actual + horas_por_avanzar) %24
      return hora_futura

def main():

    hora_actual =int(input("ingrese la hora actual(en formato 24 horas): "))
    horas_por_avanzar = int(input("ingrese el numero de horas a avanzar: "))

    hora_futura = calcular_hora_futura(hora_actual, horas_por_avanzar)

    print("la hora en", horas_por_avanzar, "horas sera", hora_futura)

if __name__ == "__main__":
        main()
        #hora futura