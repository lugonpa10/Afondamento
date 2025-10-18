frutas = {"manzana", "naranja", "plátano", "uva", "manzana"} # manzana duplicada
citricos = set(["limón", "naranja", "lima", "naranja", "pomelo"]) # Desde lista con duplicados
vacio = set()
print(f"Frutas: {frutas}") # ¡manzana aparece solo una vez!
print(f"Cítricos: {citricos}") # Los duplicados se eliminan
print(f"Set vacío: {vacio}")
print(f"Tipo: {type(frutas)}")