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
    diccionario = {}
    signos = ["¡", "!", "¿", "?", ".", ",", ";", ":", "(", ")", "\"", "'"]
    
    palabraLarga = ""
    sumaLongitudes = 0
    palabra_frecuente=""
    max_frecuencia= 0
   

    texto = texto.lower()

    for signo in signos:
        texto = texto.replace(signo,"")
    
    palabras = texto.split()

    num_palabras = len(palabras) # palabras totales
   
    
    for palabra in palabras: # media palabras
         sumaLongitudes+= len(palabra)

    mediaPalabras = sumaLongitudes / len(palabras)
    
    
    for palabra in palabras: # palabra mas larga
        if len(palabra) > len(palabraLarga):
            palabraLarga = palabra
    
    for palabra , frecuencia in diccionario.items(): # palabra frecuente
        if frecuencia > max_frecuencia:
            max_frecuencia = frecuencia
            palabra_frecuente = palabra

    return(num_palabras,mediaPalabras,palabraLarga, palabra_frecuente)







    
    

    

    
    
            







    






    






