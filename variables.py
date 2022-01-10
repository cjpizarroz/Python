print("Uso de variables")
print()
name = "Carlos Javier"
lastname = "Pizarro"
nickname = "Pichi"

print(name)
print(lastname)
print(nickname)

print(name + " " +lastname +" "+ nickname)

#--------------------------
x = 2
y = 5
h, nombre = ( 3, "Carlos")

c = x * y
print("valor de x: ", x)
print("valor de y: ", y)
print("valor de multiplicar x por y:", c)
print("valor de c:", h)
print("valor de nombre: ", nombre)


#------------------------------------
# CONVENCION PARA NOMBRAR VARIABLES

# Snake Case
book_name = "Pulgarcito" # en minuscula separado por GUION BAJO

# Camel Case
bookName ="Pulgarcito"  # Colocar la primera en mayuscula a partir de la segunda palabra

# Pasacl Case
BookName = "Pulgarcito"  #  Colocar las primeras letras de cada palabra en mayusculas

# Para nombrar variables se usa todo el nombre en mayusculas
PI = 3.1416
MY_NAME = "Carlos"
#-------------------------------------------

# PYTHON ES UN LENGUAJE DINAMICO. esto significa que una misma variable puede
# tomar valor de diferentes clases sin tener que hacer nada. Ejemplo

name = "Carlos Javier"  # aqui es un string
name = 2                # ahora es un entero
name = [10, "pucho", True]  # ahora es una lista
