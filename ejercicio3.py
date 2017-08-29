

lista1 = []
lista2 = []
c = []

x = input ("valor spd")

while x != "spread":
    lista1.append(x)
    x = input("siguiente valor en lista1: ") 

z = input ("valor ttl")

while z != "total":
    lista2.append(z)
    z = input("siguiente valor en lista2: ") 

x1 = input ("search")

while x1 != "close":
    if x1 in lista1 and lista2:
        c.append(x1)
        x1= input("next search")
    else:
        x1= input("next search")

if x1 == "close":
    print(c[0:len(x1)])
