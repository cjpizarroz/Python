total = 0
contador = 0
mayor = None
menor = None
while True:
    linea = input('Ingrese valor: ')
    if linea == 'fin':
        print("Ingreso terminado")
        break
    try:
        valor = float(linea)
        if mayor == None and menor == None:
            mayor = valor
            menor = valor
        if valor > mayor:
            mayor = valor
        if valor < menor:
            menor = valor

        total = total + valor
        contador = contador + 1
            
    except:
        print("Ingreso Erroneo")
        continue
    

print("Cantidad total de valores ingresados: ", contador)
print("Suma Total de valores: ", total) 
print("Promedio general: ", total/contador)
print("El valor mas grande es: ", mayor, " y el menor es: ", menor)