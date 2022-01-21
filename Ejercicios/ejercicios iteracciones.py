print("-- Este programa imprime el texto al reves")
cadena = input("Ingrese texto: ")
cont = 0
while cont < len(cadena):
    if cont == (len(cadena)-1):
        print(cadena[len(cadena)-(cont+1)], end='-chauuuuu\n')    # end=' ' elimina el salto de linea y coloca el texto ingresado entre la comilla
    else:
        print(cadena[len(cadena)-(cont+1)], end='')    # end='' elimina el salto de linea
    cont = cont +1


#-------------------------
def recuento(cadena_1,cond):
    cont = 0
    for letra in cadena_1:
        if letra == cond:
            cont = cont + 1
    print(" la cantidad de veces que se repite ", cond," es: ", cont)
    

while True:
    cadena = input("Ingrese cadena: ")
    if cadena == "fin":
        break
    
    caracter = input("ingrese letra: ")
    if caracter =='fin':
        break
    letra = caracter[0]
    print(type(letra))
    recuento(cadena,letra)
    print(" func COUNT -- la cantidad de veces que se repite ",letra," es: ", cadena.count(letra))
