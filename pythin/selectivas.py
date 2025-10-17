numero = int(input("dame un nº"))

if numero > 0:
    print("es positivo")
    if numero > 10:
        print("mayor que 10")
    print("dentro del primer if")
print("fuera")


if numero > 0:
    print("El número es positivo.")
    print("Esto también está dentro del if.")
elif numero == 0:
    print("El número es el cero.")
else:
    print("El número es negativo")
print("Esto ya está fuera de la estructura por la identación.")

respuesta = input("¿Deseas continuar?\n")
# Las cadenas sí se pueden comparar con ==
# Las operaciones lógicas son and, or y not
if respuesta =="si" or respuesta == "Si" or respuesta == "SI":
    print("Pues lo lamento porque por ahora voya a parar")
print("Fin del ejemplo")