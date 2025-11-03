def contar_palabras(texto):
    diccionario = {}
    signos = ["¡", "!", "¿", "?", ".", ",", ";", ":", "(", ")", "\"", "'"]
    texto = texto.lower()

    for signo in signos:
         texto = texto.replace(signo,"")

    palabras = texto.split() 
    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra]+=1
        else:
            diccionario[palabra]=1   

          
    return diccionario

def estadisticas_texto(texto):
    diccionario = contar_palabras(texto)
    signos = ["¡", "!", "¿", "?", ".", ",", ";", ":", "(", ")", "\"", "'"]
    
    palabraLarga = ""
    sumaLongitudes = 0
    palabra_frecuente=""
    max_frecuencia= 0
   

    texto = texto.lower()

    for signo in signos:
        texto = texto.replace(signo,"")
    
    palabras = texto.split()

    num_palabras =  len(palabras) # palabras totales

   
    
    for palabra in palabras: # media palabras
         sumaLongitudes+= len(palabra)

    mediaPalabras =  sumaLongitudes / len(palabras)
    
    
    for palabra in palabras: # palabra mas larga
        if len(palabra) > len(palabraLarga):
            palabraLarga = palabra
    
    for palabra , frecuencia in diccionario.items(): # palabra frecuente
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            palabra_frecuente = palabra

    return(
        ("Numero total de palabras",num_palabras),
        ("Longitud media",mediaPalabras),
        ("La palabra mas larga es ",palabraLarga),
        ("Palabra mas frecuente ", palabra_frecuente)
        )


archivo = input("Introduce el nombre de un archivo: ")

with open(archivo,"r") as archivo_lectura:
    texto = archivo_lectura.read()

frecuencias = contar_palabras(texto)

for palabra, frecuencia in frecuencias.items():
    print(f"{palabra:<15}: {frecuencia}")

print()

for tag,valor in estadisticas_texto(texto):
    print(f"{tag}:{valor}")











    
    

    

    
    
            







    






    






