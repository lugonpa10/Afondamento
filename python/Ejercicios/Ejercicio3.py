import math

def pide_entero_positivo():
        while True:
                try:   
                    num = int(input("Introduce un numero positivo: "))
                    if num > 0:
                        return num
                    else:
                        print("Error: El numero debe de ser positivo")
                except ValueError:
                      print("Error: Debes ingresar un numero")

def comprueba_isbn(isbn):
    signos = ["-"," "]
    for signo in signos:
        isbn= isbn.replace(signo,"")

    if len(isbn)!=10:
         print("El isbn no se ajusta al tamaño permitido")
         return False
    
    for i in range(9):
         if not isbn[i].isdigit():
              print("No todos los caracteres son digitos")
              return False
    
    if not (isbn[i].isdigit() or isbn[9] == 'X'):
         print("El ultimo caracter no es valido")
         return False
    
    print("El isbn es valido")
    return True

def pide_libro():
    titulo = input("Introduce el titulo del libro: ") 
    autor = input("Introduce el autor: ")
    while True:
        try:
            isbn = input("Introduce el ISBN: ")
            if comprueba_isbn(isbn):
               break
            else:
                print("Isbn No valido")
        except ValueError:
             print("Debe ingresar un ISBN: ")

    num_pag = pide_entero_positivo()

    return (
         (f"{titulo}"),
         (f"{autor}"),
         (f"{isbn}"),
         (f"{num_pag}")
    )

libros =[]
try:
     with open("GuardaDatos.txt","r") as archivo_guarda_datos:
          for linea in archivo_guarda_datos:
               linea = linea.strip()
               datos = linea.split(",")
               if len(datos) == 4:
                    titulo = datos[0]
                    autor = datos[1]
                    isbn = datos[2]
                    num_pag = int(datos[3])
                    libros.append((titulo,autor,isbn,num_pag))
except FileNotFoundError:
     print("No se ha encontrado el archivo")

opcion = 0
while opcion != 4:
    print("1.Añadir libro")
    print("2.Mostrar Lista")
    print("3.Eliminar un libro")
    print("4.Salir y guardar datos")
    opcion = int(input("Elige una Opcion: "))

    if opcion == 1:
        libro = pide_libro()
        libros.append(libro)
    if opcion == 2:
        print(f"{'Título':<20} {'Autor':<20} {'ISBN':<15} {'Páginas':<7}")
        for libro in libros:
            titulo,autor,isbn,num_pag = libro
            print(f"{titulo:<20} {autor:<20} {isbn:<20} {num_pag:<20}")
    if opcion == 3:
        titulo_borrar = input("Introduce el titulo del libro a eliminar: ")

        titulo = False

        libros_no_borrados = []

        for libro in libros:
            if libro[0] != titulo_borrar:
                  libros_no_borrados.append(libro)
            else:
                 titulo = True
                 
        libros = libros_no_borrados
        
        if titulo:
             print("Libro eliminado")
        else:
             print("No se ha encontrado el titulo")

    if opcion == 4:
        with open("GuardaDatos.txt","w") as archivo_guarda_datos:
             for libro in libros:
                  linea = libro[0] + "," + libro[1] + "," + libro[2]+","+str(libro[3])
                  archivo_guarda_datos.write(f"{linea}\n")
        print("Datos guardados")

        
              
         


             
             

        
      
                 
         
            

              




            
    
 
        
            
        



     
    
    
    
         
    
         
    
    
      
       
                

        
                
      
        

    





    
       

