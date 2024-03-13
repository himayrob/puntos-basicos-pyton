#quise hacerlo de otra manera
n1 = int(input("ingrese numero 1"))
n2 = int(input("ingrese numero 2"))
n3 = int(input("ingrese numero 3"))
n4 = int(input("ingrese numero 4"))
numeros ={
   "numero1" :n1,
   "numero2" :n2,
   "numero3" :n3,
   "numero4" :n4
       }
numo = dict(sorted(numeros.items(), key=lambda item:item[1]))
print(numo)
#descubri el origen del universo en este ejercicio ajajjajajajajj