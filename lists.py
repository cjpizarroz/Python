demo_list = [1,2,3,5,'casa',7,8,9, ['a','b','c']]    # Lista de numeros y tiene otra lista se string como elementos
print(type(demo_list), " ", demo_list)

colors = ['red','blue', 'yelow', 'white']
print(type(colors), " ", colors)

numbers_list = (1,2,5,6,8)                          # Asignacion de una TUPLA a number_list
print(type(numbers_list), "  ", numbers_list)       
numbers_list = list(numbers_list)                   # Castea a LISTA una TUPLA
print(type(numbers_list), "  ", numbers_list)

#--------------------------------------------------
# Crear una lista a partir de la funcion RANGE

r = list(range(1,10))   # Solo llega al segundo numero menos 1 
print("Lista de valores del 1 al 10 ", r)

r = list(range(1,11))   # Solo llega al segundo numero menos 1 
print("Lista de valores del 1 al 10 ", r)

#----------------------------------------------------
# Saber que se puede hacer con LISTAS
print(dir(colors))
print(len(colors))
print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])
print(colors[-1])
#---------------------------------

print("Red esta en la lista? : ", "red" in colors)
print("Black esta en la lista? : ", "Black" in colors)

#-----------------------------------
# Cambios de valores en una lista
print(colors)
colors[2] = "violet"  # Reemplaza en la lista segun el indice y el valor
print(colors)

colors.append("brown")  # Agrega al final de la lista el nuevo elemento
print(colors)

#colors.append(("pink", "ligt blue")) # Agrega al final de la lista la TUPLA con su elementos

#print(colors)

colors.extend(("pink", "ligt blue", "blue", "red", "blue"))  # Agrega al final de la lista cada uno de los elementos de la TUPLA (x,x,x) o LISTA [x,x,x]
print(colors)

colors.insert(3,"gris") # Inserta en el indice 3 el valor gris
print(colors)

colors.insert(len(colors), "dorado") # Inserta en la ultima posicion (dado por el valor Len de Colors), el valor dorado
print(colors)

colors.pop()        # Elimina el ultimo valor de la lista
print(colors)

colors.pop(2)        # Elimina el valor del indice de la lista
print(colors)

colors.remove("blue")  # Elimina solo el primer valor que coincide con el indicado
print(colors)

colors.sort()  # Ordena alfabeticamente de menor a mayor la lista
print(colors)

colors.sort(reverse=True)  # Ordena alfabeticamente de mayor a menor la lista
print(colors)
print(colors.index("pink"))  # Indica la posicion donde se encuentra el color indicado
print(colors.count("red"))      # Cuenta la cantidad de veces que se encuentra el color indicado


#colors.clear()      # Elimina toda la lista

#print(colors)