def resultado_set(m, n):

    if abs(m - n) > 2 or (m > 7 or n > 7) or (m ==7 and n==7):
        return "resultado invalido"
    
    elif m < 6 and n <6:
        return "el set no ha terminado"
    
    elif m >= 6 and m - n >=2:
        return "el jugador A gano el juego"
    
    elif n >= 6 and m - n >=2:
        return "el jugador B gano el set"
    
    elif m == n == 6:
        return "el set se define en un ultimo juego (7-6)"
    
    else:
        return "resultado invalido"
    
m = int (input("cantidad de juegos A :"))
n = int(input("cantidad de juegos B :"))

print (resultado_set(m, n))
#set  de tenis
