#FUNCIONES

def suma(a,b): 
    return a + b 

def resta(a,b): 
    return a - b 

def multi(a,b): 
    return a * b 

def divi(a,b):
    if b == 0:
      return "No se puede dividir por 0"
    else:
     return a / b 



#MENU
print("\n********MENU********")
print("\n1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicación (*)")
print("4. División (/)")
opcion = input("\nElige una opción: ")


a = int(input("\nDigite el primer numero: "))
b = int(input("Digite el segundo numero: "))

#CONDICINALES 

if opcion == "1": 
    resultado = suma(a,b)
    print("La suma es: ",resultado)

elif opcion == "2": 
    resultado = resta(a,b)
    print("La resta es",resultado)

elif opcion == "3": 
    resultado = multi(a,b)
    print("La multiplicacion es: ",resultado)

elif opcion == "4": 
    resultado = divi(a,b)
    print("La divison es: ",resultado)

else: 
    print("Opcion Invalida")








