import math

def tiempo_para_temperatura(T_original, Ty):
    # Constantes y valores dados
    M_pequeño = 47  # masa para un huevo pequeño en gramos
    M_grande = 67  # masa para un huevo grande en gramos
    rho = 1.038  # densidad en g/cm^3
    c = 3.7  # capacidad calorífica específica en J/gK
    K = 5.4e-3  # conductividad térmica en W/cmK
    Tw = 100  # temperatura de ebullición del agua en °C
    
    # Selección de la masa del huevo según su tamaño
    M = M_pequeño if T_original < 20 else M_grande
    
    # Cálculo de la temperatura original en Kelvin
    To = T_original + 273.15
    
    # Cálculo del tiempo en segundos
    t = (M**(2/3) * c * rho**(1/3) * K * math.pi**2 * (4 * math.pi / 3)**(2/3) * math.log(0.76 * To - Tw / (Ty - Tw))) / 60
    
    return t

# Función principal
def main():
    T_original = float(input("Ingrese la temperatura original del huevo en grados Celsius: "))
    Ty = float(input("Ingrese la temperatura a la que desea cocinar la yema en grados Celsius: "))
    
    tiempo = tiempo_para_temperatura(T_original, Ty)
    
    print(f"El tiempo necesario para alcanzar {Ty}°C en el centro de la yema es de aproximadamente {tiempo:.2f} segundos.")

if __name__ == "__main__":
    main()
