import math

def tiempo_para_temperatura(T_original, Ty):
   
    M_pequeño = 47  
    M_grande = 67  
    rho = 1.038  
    c = 3.7 
    K = 5.4e-3  
    Tw = 100  
    
   
    M = M_pequeño if T_original < 20 else M_grande
    
   
    To = T_original + 273.15
    
  
    t = (M**(2/3) * c * rho**(1/3) * K * math.pi**2 * (4 * math.pi / 3)**(2/3) * math.log(0.76 * To - Tw / (Ty - Tw))) / 60
    
    return t


def main():
    T_original = float(input("Ingrese la temperatura original del huevo en grados Celsius: "))
    Ty = float(input("Ingrese la temperatura a la que desea cocinar la yema en grados Celsius: "))
    
    tiempo = tiempo_para_temperatura(T_original, Ty)
    
    print(f"El tiempo necesario para alcanzar {Ty}°C en el centro de la yema es de aproximadamente {tiempo:.2f} segundos.")

if __name__ == "__main__":
    main()
