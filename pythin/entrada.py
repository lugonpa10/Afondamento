# nombre = input("Dime tu nombre:")
# input(nombre)

# Recuerda: No necesitamos declarar las variables
# Se podría hacer por separado (print y luego input)
nombre = input("Dime tu nombre: ")
# input siempre devuelve un String, por lo que hay que convertirlo a entero
edad = int(input("Ahora la edad: "))
temperatura = float(input("¿Qué temperatura e ºC hace ahora?\n"))
print() # deja una línea en blanco
print(nombre + ", Welcome\n to the Java World.\n\n")

from datetime import date as d
año_nacimiento = d.today().year - edad
print('Naciste en el año: ', año_nacimiento) # Se permite comilla simple para cadenas
letra = nombre[0] # Se indexa la cadena con []. Ojo, el carácter sigue siendo str.
print("la primera letra de tu nombre es %s porque tu nombre es %10s" % (letra,nombre)) # Cadena de formato con %