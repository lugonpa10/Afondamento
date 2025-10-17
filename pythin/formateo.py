# # En Python clásico funciona prácticamente igual a Java, pero escrito así:
# # "Cadena de formato" % (elemento1, elemento2, …) ? Sí, son tuplas
# nombre = "Gollum"
# edad = 30
# peso = 34.341
# print("Se llama %s, tiene %d años y pesa %.1fKg.\n" % (nombre, edad, peso))
# print("%-10s%10s" % ("Personaje", "Peso (Kg)"))
# print("%-10s%10.2f" % (nombre, peso))
# print("%-10s%10.2f" % ("Gandalf", 78.2))
# print("\nLa edad de %s en los tres sistemas de numeración:" % nombre)
# print("Decimal: %d, Octal: %o, Hexadecimal: %04x" % (edad, edad, edad))

# Desde Python 3.6 en adelante se recomienda el uso de f-strings o cadenas iterpoladas
# ¿Sabes deducir cómo funcionan?
nombre = "Gollum"
edad = 30
peso = 34.341
print(f"Se llama {nombre}, tiene {edad} años y pesa {peso:.1f}Kg.\n")
print(f"{'Personaje':<10}{'Peso (Kg)':>10}")
print(f"{nombre:<10}{peso:>10.2f}")
print(f"{'Gandalf':<10}{78.2:>10.2f}")
print(f"\nLa edad de {nombre} en los tres sistemas de numeración:")
print(f"Decimal: {edad}, Octal: {edad:o}, Hexadecimal: {edad:04x}")