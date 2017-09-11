n0 = int(input("ingrese el nivel inferior"))
nx = int(input("ingrese el nivel superior"))

cuenta = n0
while cuenta<=nx:
        print (cuenta,end=',')
        cuenta=cuenta+1
print("")
print("fin")

intervalo = nx-n0

def espacio():
    if n0<=nx :
        print ("el intervalo del conjunto x es: ",intervalo)
    else:
        print ("solo imprime listas positivas")
espacio()

