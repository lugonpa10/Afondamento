print("hello world") # end para marcar finalizacion
print("adios")



entero = 10
real = 12.1
string = "Hola" # También vale 'Hola', no hay char
booleano = True # Empieza por mayúscula, ojo.
# Con type() conozco el tipo
print(type(entero))
print(type(real))
print(type(string))
print(type(booleano))


# Conversión de tipos
# int(), float(), str(), bool()
dato = int(real) + 3
print("El numero",dato,"es de tipo", type(dato))
print(float("231.33") + 3.1)
print(str(dato) + "222")
