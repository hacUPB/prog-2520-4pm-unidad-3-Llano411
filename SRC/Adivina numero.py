'''
Variable de entrada
nombre      tipo
numero      int

variable de salida
intentos    int     contador 

variable de control 
numero      int
'''


'''
#import random
from random import randint
num_aleatorio = randint(1,100)
numero = -1
intentos = 0
while numero != num_aleatorio:
    numero = int(input("Adivina el numero entre 1 y 100: "))
    intentos += 1 
    if num_aleatorio > numero:
        print("Busca un numero mayor")
    elif num_aleatorio < numero:
        print("Busca un numero menor")
    else:
        print(f"Felicidades, adivinaste en {intentos} intentos")
'''
numero = int(input("Ingrese un numero entero mayor que 1: ")) 
divisor = numero // 2 # division entera
cont = 0 
for i in range(2, divisor + 1):
    if numero % i == 0:
       cont += 1

if cont == 0:
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
    print(f"los divisores de {numero} son:")
    for i in range (1, numero + 1):
        if numero % i == 0:
            print(i)
        