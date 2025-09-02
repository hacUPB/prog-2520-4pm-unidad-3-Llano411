'''
# Solicitar al usuario un número entero
Imprimir("Ingrese un número entero para generar la serie de Fibonacci:")
Leer(num)

# Verificar si el número ingresado es válido
Si num <= 0, entonces:
    Imprimir("Por favor, ingrese un número entero positivo.")
Sino si num == 1, entonces:
    Imprimir("Serie de Fibonacci:")
    Imprimir(0)
Sino:
    # Inicializar los primeros dos términos de la serie
    a = 0
    b = 1
    contador = 2  # Iniciar en 2 debido a los dos primeros términos ya impresos

    # Imprimir los primeros dos términos
    Imprimir("Serie de Fibonacci:")
    Imprimir(a)
    Imprimir(b)

    # Calcular e imprimir los términos restantes
    Mientras contador < num, hacer:
        siguiente = a + b
        Imprimir(siguiente)
        a = b
        b = siguiente
        contador += 1
'''
'''
numero = int(input("Ingrese cantidad de terminos: "))
if numero <= 0:
    print("No se imprimen terminos")
elif numero == 1:
    print(0)
else:
    a = 0
    b = 1 
    print(a)
    print(b)
    m = 1 
    while m <= (numero - 2):
        c = a + b 
        print(c)
        a = b 
        b = c 
        m += 1 
'''
# Bucle For range (el de la izquierda es donde empieza, el del centro hasta donde va, el de la derecha es cada cuanto aumenta o decrece)
'''
mensaje = "Programacion en python"
numero = int(input("Ingrese el numero: "))
for i in range(numero):
    print(f"{i+1}. {mensaje}")
'''
'''
n = int(input("Ingresa un numero entero positivo: "))
for i in range (0,n+1):
    if n%2== 0:
        acumulador += i # tipo de variable: acumulador 
print(f"La suma de los numeros pares de 0 hasta {n} es: {acumulador}")
'''
numero = int(input("Ingrese un número entero: "))

for i in range(1, numero + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()