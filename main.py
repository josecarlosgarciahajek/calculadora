#from division import dividir
#from multiplicacion import multiplicar
#from suma import suma
#from resta import resta
from factorial import factorial
from mediana import mediana
from primo import primo
from division_entera import division_entera
from menu import *

opciones = [1,2,3,4,5,6,7,8]

menu()

opc = int(input("Ingresa el número de la operación deseada: "))

if opc in opciones:
        if opc == 1:
            numero1 = int(input("Dame un número: "))
            numero2 = int(input("Dame otro número: "))
            print("El resultado es: ", suma(numero1, numero2))
        elif opc == 2:
            numero1 = int(input("Dame un número: "))
            numero2 = int(input("Dame otro número: "))
            print("El resultado es: ", resta(numero1, numero2))
        elif opc == 3:
            numero1 = int(input("Dame un número: "))
            numero2 = int(input("Dame otro número: "))
            print("El resultado es: ", multiplicar(numero1, numero2))
        elif opc == 4:
            numero1 = int(input("Dame un número: "))
            numero2 = int(input("Dame otro número: "))
            print("El resultado es: ", dividir(numero1, numero2))
        elif opc == 5:
             lista = []
             num_list = int(input("Dame un número para la primera lista: "))
             for num in range(num_list):
                num1 = int(input("Dame un número para la primera lista: "))
                lista.append(num1)
             print("El resultado es: ", mediana(lista))
        elif opc == 6:
             numero1 = int(input("Dame un número: "))
             print("El resultado es: ", factorial(numero1))
        elif opc == 7:
             numero1 = int(input("Dame un número: "))
             print("El resultado es: ", primo(numero1))
        elif opc == 8:
            numero1 = int(input("Dame un número: "))
            numero2 = int(input("Dame otro número: "))
            
            print("El cociente es: ", division_entera(numero1), "El resto es: ", division_entera(numero2))
        else:
             print("Opción no valida. Adios!!!")
