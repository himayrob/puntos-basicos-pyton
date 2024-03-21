def año_bisiesto(año):
    if año %4 ==0 and (año!=0 or año%400 ==0):
        return True
    else:
        return False
    
año =int(input("indique su año: "))
if año_bisiesto(año):
    print("es bisiesto")
else:
    print("no es bisiesto")
    #años bisiestos
    