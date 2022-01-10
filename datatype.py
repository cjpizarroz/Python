
# Distintas formas de declarar un string
# usando comillas dobles o simples
# o combinacion de tres comillas simples o dobles

print ("hola Javier")
print ('Como estas con Python')
print ("""Aprendiendo solito""")
print ('''Tenes que aprenderlo bien''')

#---------------------------------------
# Uso de la funcion Type

print (type("a ver que tipo de dato es esta cadena"))
# imprime tipo class 'str' (String)

print(type(125))
# imprime tipo class 'int' (Integer)

print(type(12.5))
# imprime tipo class 'float' (Float)

print(type(True))
# imprime tipo class 'bool' (Booleano)
#----------------------------------------
print()
# Concatenacion
print(" CONCATENACION --------------------------")
print("hola" + " Javier " + "3" + " Pizarro")
print()
#----------------------------------------------
# Listas
print(" LISTAS -- (pueden tener distintos tipos de datos y cambiar)------------------------")
print([10 , 15, 68])
print(["hola", 'ejemplo', "lista"]) 
print([12, "prueba", 25.6, True])
print(type([10 , 15, 68]))
print()
#----------------------------------------------
# Tuplas (listas que no pueden cambiar - simil Enum de JAVA)
print(" TUPLAS --(No pueden cambiar sus datos)------------------------")
print((1, 45))
print (type((1, 45)))
print()
#----------------------------------------------
# Dictionaries
print("Diccionarios ----(Entidad)------------------")
{
    "name":"Carlos Javier",
    "lastname":"Pizarro",
    "nickname":"Pichi"
}

print({
    "name":"Carlos Javier",
    "lastname":"Pizarro",
    "nickname":"Pichi"
})

print(type({
    "name":"Carlos Javier",
    "lastname":"Pizarro",
    "nickname":"Pichi"
}))
print()
#----------------------------------------------
# None (Tipo de dato simil Nulo)
print(" NONE --(Tipo de dato)------------------------")
print((None))
print (type((None)))
print()