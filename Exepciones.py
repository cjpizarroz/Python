try:
    msj = "Ingrese cantidad de horas trabajadas:\n"
    x = input(msj)
    val_x = int(x)
    msj = "Ingrese el importe por hora trabajada:\n"
    y = input(msj)
    val_y = float(y)
    salario = val_x * val_y
    print("El salario que le corresponde por lo trabajado es de: ", salario)
    h=1
except:
    print("El dato ingresado no es un numero")
    h=2

if h==1:
    print("Programa terminado OK")
elif h==2:
        print("El Programa termino por un error de ingreso")


print("Chauuuuuuuuu "*3)


