import random
print("\n--------------------------")
print("RANDOM.RANDOM - elige un valor entre 0.0 y 0.1\n")

for i in range(10):
    x = random.random()
    print(x)
#----------------------
print("\n--------------------------")
print("RANDOM.RANDINT - elige un valor entero de un rango pasado\n")

print("numeros enteros aleatorios entre 5 y 20: ---->  ", random.randint(5,20))
print("numeros enteros aleatorios entre 0 y 11: ---->  ", random.randint(0,11))
print("numeros enteros aleatorios entre 1 y 100: ---->  ", random.randint(1,100))

#----------------------
print("\n--------------------------")
print("RANDOM.CHOICE - elige un valor de la lista pasada\n")
t = [1,4,8,"perro",9,15,"gato"]
print("lista", t)
print(random.choice(t))
print(random.choice(t))
print(random.choice(t))
print(random.choice(t))

#----------------------
print("\n--------------------------")
print("FUNCIONES ESTERILES -- sin retorno\n")    

def imprime_estribillo():
    print("que tendra el petiso")
    print("que a las mujeres vuelve locas\n")

def repite_estribillo():
    imprime_estribillo()
    imprime_estribillo()

print("--- Prueba de funciones definidas por el usuario")
imprime_estribillo()

print("--- Funcion que llama a otra funcion")
repite_estribillo()
print("------------------------------")
print(imprime_estribillo)
print(repite_estribillo)

#----------------------
print("\n--------------------------")
print("FUNCIONES PRODUCTIVAS -- con retorno\n")    

def suma_valores(a,b):
    suma = a + b
    return suma

try:
    val1 = input("ingrese el primer valor: ")
    val2 = input("ingrese el segundo valor: ")
    a = float(val1)
    b = float(val2)
    suma = suma_valores(a,b)
    print("la Suma de ",a, " + ",b, " es = ",suma)
except:
    print("Alguno de los valores es erroneo")