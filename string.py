name = "Carlos Javier"

print(dir(name)) # Imprime todas las opciones para usar con los string
print(name.upper()) # Pasa a mayusculas todo el texto
print(name.lower()) # Pasa a minusculas todo el texto
print(name.capitalize()) # Pome mayuscula a la primera letra del texto
print(name.replace("Javier","Pizarro")) # Muestra por pantalla un reemplazo sin cambiar el valor en la variable
print(name) # Imprime la variable
name = name.replace("Javier","Pizarro Zubazu") # Reemplaza un texto por otro
print(name)
print(name.count("a")) # Cuenta las letras a
print("Termina con azu: ",name.endswith("azu")) # Devuelve False o True si termina con azu
print("Termina con a: ",name.endswith("a")) # Devuelve False o True si termina con a
print("Empieza con Car: ",name.startswith("Car")) # Devuelve False o True si empieza con Car
print("Empieza con c: ",name.startswith("c")) # Devuelve False o True si empieza con c
print("Empieza con C: ",name.startswith("C")) # Devuelve False o True si empieza con C

#----------------------
# split   (Separa el texto en elementos de una lista segun indicacion)
print(name.split()) # Separa el texto segun los espacios o el caracter que se indique dentro de split
                    # Devuelve una lista
lista = name.split()  #Asigna la ista creada a la variable lista                  
print(lista)  # Imprime la lista
print(type(lista))  # Indica el tipo de la variable lista
#------------------------------
nombre = "sanfntokjkjaiokjhaiuhdrealkjhda"
print(nombre.split("a"))  # Separa el texto cada vez que encuentra la letra a y crea una lista

#---------------------------------------------
# find   (Busca la primera coincidencia)
print("La Primer letra Z se encuentra en la posicion: ", name.find("Z")) # Indica la posicion donde encuentra la primer Z
print("La primer letra d se encuentra en la posicion: ",nombre.find("d")) # Indica la posicion donde encuentra la primer d

print("la cantidad de caracteres de: ", name, " es de: ", len(name))  # Cuenta la cantidad de caracteres
print("la cantidad de caracteres de: ", nombre, "es de: ", len(nombre))  # Cuenta la cantidad de caracteres

#---------------------------------------------
# index (Devuelve el indice de la primnera coincidencia segun dato de busqueda)

print("El indice de la posicion de Z es: ",name.index("Z"))
print("El indice de la posicion de d es: ", nombre.index("d"))

#---------------------------------------------
# isnumeric    (devuelve False o True si el valor es numerico)
# isalpha       (devuelve False o True si el valor es alfabetico)
print(name, "es numerico?: ", name.isnumeric())
print(nombre, "es alfabetico?: " , nombre.isalpha())

#------------------------------------
# Imprimir segun un indice
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
# Imprime de atras hacia adelante (comienza del -1 que seria la ultima posicion)
print(name[-1])
print(name[-2])
print(name[-3])

#*-----------------------------------------
# formas de imprimir un texto sumado a la variable

print("My name: ", name, "      Usando...print(""My name: "", name)")
print("My name: "+ name, "      Usando...print(""My name: +","name)")
print(f"My name: {name}","      Usando...print(f""My name:{","name }")
print("My name: {0}".format(name), "       Usando... print(""My name: {","0 }",".format(name)")
