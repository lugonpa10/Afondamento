# Crear una lista de 20 números
numeros = list(range(1, 21)) # [1, 2, 3, ..., 20]
print(f"Lista original: {numeros}")
print(f"Longitud: {len(numeros)}")
print()

# 1. ÍNDICES POSITIVOS (de izquierda a derecha)
print("=== ÍNDICES POSITIVOS ===")
print(f"numeros[0] -> {numeros[0]}") # Primer elemento
print(f"numeros[5] -> {numeros[5]}") # Sexto elemento
print()
# 2. ÍNDICES NEGATIVOS (de derecha a izquierda)
print("=== ÍNDICES NEGATIVOS ===")
print(f"numeros[-1] -> {numeros[-1]}") # Último elemento
print(f"numeros[-2] -> {numeros[-2]}") # Penúltimo elemento
print(f"numeros[-5] -> {numeros[-5]}") # Quinto desde el final
print(f"numeros[-20] -> {numeros[-20]}") # Primer elemento
print()

# 3. SLICING (REBANADOS) BÁSICO [inicio:final]
print("=== SLICING BÁSICO ===")
print(f"numeros[2:7] -> {numeros[2:7]}") # Elementos 2 al 6
print(f"numeros[:5] -> {numeros[:5]}") # Primeros 5 elementos
print(f"numeros[15:] -> {numeros[15:]}") # Desde el 15 hasta el final
print()
# 4. SLICING CON PASO (STEP) [inicio:final:paso]
print("=== SLICING CON PASO ===")
print(f"numeros[::2] -> {numeros[::2]}") # Cada 2 elementos
print(f"numeros[1::2] -> {numeros[1::2]}") # Cada 2 elementos empezando en 1
print(f"numeros[2:15:3] -> {numeros[2:15:3]}") # Cada 3 elementos del 2 al 14
print(f"numeros[::-1] -> {numeros[::-1]}") # Lista invertida
print()