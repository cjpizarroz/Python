print(type(10))
print(type(10.5))
print(2*9)

#-----------------------------
print("Division de 10/3: ",10/3)  # Muestra la DIVISION

print("parte ENTERA del resultado de la DIVISION de 10/3: ",10//3)  # Muestra la parte ENTERA del resultado de la DIVISION

print("MODULO o RESTO de la DIVISION de 10/3: ",10%3)   # MUestra el MODULO o RESTO de la DIVISION

#------------------------------------------------
print("Multiplicacion de 2*3: ", 2*3)   #Muestra el producto

print("Exponencial de 2 elevado a la 3: ", 2**3)  # Exponencial de el primer numero elevado al segundo

#------------------------------------------------
# Uso del INPUT
# todo los input tiene como typo de dato de ingreso el TIPO STRING
# Para uso de un valor numerico se debe castear al tipo requerido int() float()


age = input("Insert your age: ")    # Input 
print(type(age))                    # Muestra el tipo de dato ingresado
new_age = int(age) +5               # Castea el string a entero y lo qasigna a una variable
print(type(new_age))                # Muestra el tipo de dato de la nueva variable con el CAsteo
print(new_age)                      # Muestra el valor de la nueva variable



