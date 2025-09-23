# import Modulo
# from Modulo import primo, fibonacci, triangulo
from modulo import * # el * significa importar todo
#Función principal
'''
def main():
    
    
    
 
# Verifica si existe una función llamada main()

'''
#Funcion principal 2
def main():
    while True:
        variable = menu()
        match variable: 
            case 1:
                print("calcula si un numero es primo: ")
                numero = int(input("Ingrese un número entero mayor que 1: "))
                primo(numero)
            case 2: 
                print("Imprime un numero de terminos de la serie de Fibonacci")
                numero = int(input("Ingrese el número de términos: "))
                fibonacci(numero)
            case 3: 
                print("Imprime un triangulo de numeros.")
                numero = int(input("Ingrese el número entero positivo: "))
                triangulo(numero)
            case 4: 
                break
            case _:
                print("Esta opcion no es valida")


if __name__ == "__main__":
    main()