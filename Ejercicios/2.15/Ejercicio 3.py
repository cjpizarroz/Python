# Escribe un programa para pedirle al usuario el número de
# horas y la tarifa por hora para calcular el salario bruto.

name = input("Nombre del empleado: ")
hours = input("Ingrese la cantidad de horas trabajadas:  ")
val_hour = input("Ingrese el valor en $$ de la hora: ")
salario = int(hours) * int(val_hour)

print("El empleado ",name,"trabajo :", hours, "hs")
print("al valor de $", val_hour, "por hora")
print("lo que da un salario de: $", salario)
