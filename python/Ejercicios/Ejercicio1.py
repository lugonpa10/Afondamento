import math

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
    
    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    if num1 > num2:
         print(f"{num1} es mayor que {num2}\n")
       
    else:
         print(f"{num2} es mayor que {num1}\n")
         
   


         
     
     
     





print("1-Division con decimales")
print("2-Potencia")
print("3-Rango")
print("4-Listas")
opcion = int(input("Introduce una opcion: "))

if opcion == 1:
      divisiones()
elif opcion == 2:
     potencia()
elif opcion == 3:
     rango()
     
     
     

 






    


       
    

    



