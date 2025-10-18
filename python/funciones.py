import math
# Funciones
# Sin parámetro ni return
def nombre_funcion():
 print("Solo muestro en pantalla")
def separador():
 print("\n-------------------\n")
# Parámetros y valor devuelto
def area_cilindro(radio, altura):
 area_base = math.pi * radio ** 2
 area_lateral = 2 * math.pi * radio * altura
 area_total = 2 * area_base + area_lateral
 return area_total
# Devolver varios valores
def calcular_todas_areas_cilindro(radio, altura):
 area_base = math.pi * radio ** 2
 area_lateral = 2 * math.pi * radio * altura
 area_total = 2 * area_base + area_lateral
 return area_total, area_lateral, area_base
# Opcionalmente se pueden indicar tipos de parámetros y valor devuelto,
# pero no se exige el cumplimiento. Solo es informativo.
def suma(a:int, b:int)-> int:
 return a+b
# nombre_funcion()
# separador()
# print(f"Area: {area_cilindro(3,4):.2f}")
# separador()
# total, lateral, base = calcular_todas_areas_cilindro(3, 7)
# print(f"Área total: {total:.2f}")
# print(f"Área lateral: {lateral:.2f}")
# print(f"Área de una base: {base:.2f}")
# separador()
print(suma("33","w")) # En teoría deberían ser int, pero el tipado no impone.