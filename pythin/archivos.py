import math
# Archivos
# Apertura: open(nombre, modo)
# modo:
# r: read (lectura)
# w: write (escritura)
# a: append (añadir)
# Escritura
# write : escribe un string en el archivo.
archivo_escritura=open("prueba.txt","w")
archivo_escritura.write("Prueba de archivos\n")
archivo_escritura.write("Valor de PI: %.4f\n"%(math.pi))
for i in range(10,21):
 archivo_escritura.write(f"{i:>4}")
archivo_escritura.close()
# Con cierre automático (append en este caso)
with open("prueba.txt","a") as f:
 f.write("\nOtra linea\n")
# Lectura
print("\nLectura tras añadir")
archivo_lectura=open("prueba.txt","r")
linea = archivo_lectura.readline()
while (linea):
 print(linea, end="") # linea ya tiene retorno de carro.
 linea = archivo_lectura.readline()
archivo_lectura.close()
# Con with y for
print("-------------------------")
with open("prueba.txt","r") as archivo:
 for linea in archivo:
    print(linea.strip()) # strip elimina retornos de carro
 # del archivo (pues el print ya mete uno)