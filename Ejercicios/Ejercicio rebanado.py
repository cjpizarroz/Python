# Rebanado: extrae de una cadena, una cadena segun el rango establecido
import random
cadena = input("Ingrese cadena: ")
print("el largo de la cadena es = ", len(cadena))
x = random.randint(0,len(cadena))
print("x = ",x)
print(type(x))
y = int(random.randint(x,len(cadena)))
print("y = ",y)
print(type(y))
sub_cad = cadena[x:y]
print(sub_cad)
print("-------------------------------\n")

print(cadena[x:],"\n")

print(cadena[:x],"\n")

print(cadena[:])