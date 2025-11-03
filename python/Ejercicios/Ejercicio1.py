import random

def divisiones():
    num1 = float(input("Introduce el dividendo: "))
    num2 = float(input("Introduce el divisor: "))
    while num2 == 0:
        print("El divisor no puede ser 0")
        num2 = float(input("Introduce un numero valido"))
    print("Resto: ", num1 % num2)
    print("Division con decimales:%.2f " % (num1 / num2))
    print("Division: ", num1 // num2)

def potencia():
     base = float(input("Introduce la base: "))
     exponente = int(input("Introduce el exponente: "))
     print(f"La base {base} con exponente {exponente} da como resultado: { base**exponente:.2f}")

def rango():
    cont = 0
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    if num1 > num2:

         for i in range(num2,num1 + 1):
              cont+=i
         print(f"{num1} es mayor que {num2} y la suma de todos los numeros entre ellos es {cont}\n")

    elif num1 == num2:
         print("Los numeros son iguales")   

    else:
         for i in range(num1,num2 +1):
            cont+=i
         print(f"{num2} es mayor que {num1} y la suma de todos los numeros entre ellos es {cont}\n")
            
def listas():
     tamanho =int(input("Dime el tamaño para las listas: "))
     lista1 =[random.randint(1,50) for i in range(tamanho)]
     lista2 =[random.randint(1,50) for i in range(tamanho)]

     print("Lista 1: \n",lista1)
     print("Lista 2: \n",lista2)

     sumalistas = [lista1[i] + lista2[i] for i in range(tamanho)]
     print("La suma es: ",sumalistas)


opcion = 0
while opcion != 5:
     print("1-Division con decimales")
     print("2-Potencia")
     print("3-Rango")
     print("4-Listas")
     print("5-Salir")
     opcion = int(input("Introduce una opcion: "))

     if opcion == 1:
          divisiones()
     elif opcion == 2:
          potencia()
     elif opcion == 3:
          rango()
     elif opcion == 4:
          listas()
     elif opcion == 5:
          print("Saliendo..")
     
     
     
     

 






    


       
    

    



