# ejemplo 1 Relacionales

print(10 > 5)
print("Hola" != "Mundo")
print(3.14 <= 4.5)
nombre = "Juan"
print(nombre == "Juan")
print (nombre == "Pedro")
print (54 < 3)

#ejemplo 2 if

envio = 0
compra = int(input("Ingrese el valor de la compra>> "))
if compra < 100000:
	envio = 9000
total = compra + envio
print(f"El total de la compra es {total}")

# ejemplo 3 if-else

n = int(input("Ingresa un número entero>> "))
r = n%2     #se calcula el residuo de la división entre 2
if r != 0:
	print(f"{n} es impar")
else:
	print(f"{n} es par")

#Ejemplo 4 

edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 0:
    if edad <= 5:
        etapa = "Primera Infancia"
    elif edad <= 11:
        etapa = "Infancia"
    elif edad <= 26:
         if edad <= 18:
            etapa = "Adolescencia"
         if edad >= 14:    
            etapa = "Juventud"
    elif edad <= 59:
        etapa = "Adultez"
    else:
        etapa = "Persona Mayor (Envejecimiento y Vejez)"
    
    print(f"Tu etapa del ciclo de vida es: {etapa}")
else:
    print("La edad ingresada no es válida.")

#Ejemplo 5 

print("ingrese la zona de envio. Elija el numero.")
zona = int(input("1. Norte america\n2. centroamerica\n3. suramerica\
                 \n4. Europa\n5. Asia\nElija un numero: "))
if zona >= 1 and zona <= 5:
    peso = int(input("ingrese el peso del paquete en gramos: "))
    if peso < 5000:
        if zona == 1:
            total = peso * 11
        elif zona == 2:
            total = peso * 10
        elif zona == 3:
            total = peso * 12
        elif zona == 4:
            total = peso * 24
        elif zona == 5:
            total = peso * 27
    else:
         print("no se puede enviar paquetes mayores a 5kg")
else:
    print("la zona ingresada no existe")
    total = 0       

print(f"el envio de su paquete cuesta ${total}")

#Ejemplo 6 

modo = 2

match modo:
    case 1:
        print("Modo 1 seleccionado: Alta Tensión")
    case 2:
        print("Modo 2 seleccionado: Media Tensión")
    case 3:
        print("Modo 3 seleccionado: Baja Tensión")
    case _:
        print("Modo no válido")

#Tarea: Cambiar el ejemplo 5 de if a match 

print("ingrese la zona de envio. Elija el numero.")
zona = int(input("1. Norte america\n2. centroamerica\n3. suramerica\
                 \n4. Europa\n5. Asia\nElija un numero: "))
total = 0
if 1 <= zona <= 5:
    peso = int(input("ingrese el peso del paquete en gramos: "))
    if peso < 5000:
        match zona:
            case 1:
                total = peso * 11
            case 2:
                total = peso * 10
            case 3:
                total = peso * 12
            case 4:
                total = peso * 24
            case 5:
                total = peso * 27
    else:
         print("no se puede enviar paquetes mayores a 5kg")
else:
    print("la zona ingresada no existe")

print(f"el envio de su paquete cuesta ${total}")

#Bucles o ciclos 

# Se recomienda usar el "for" cuando se sabe la cantidad de veces que se repetira el bucle y si la cantidad de repeticiones depende de una condicion se recomiendo usar "while"
# While es una variable Boleana (true or false)

# Ejemplo 1 
numero = 1 
while numero <= 5:
    print(numero)
    numero += 1     #numero = numero + 1

# imprimir los numeros pares entre el 20 y el 80 

numero = 20
while 20 <= numero <= 80:
    if numero % 2 == 0:
        print(numero)
    
    numero += 1 

# imprimir los impares entre 99 y 61

numero = 99
while 99 >= numero >= 61:
    if numero % 2 != 0:
        print(numero)
    
    numero -= 1

# solicitar 2 numeros al usario e imprimir los numeros impares entre ellos 

numero1 = int(input("ingrese un primer numero: "))
numero2 = int(input("ingrese un segundo numero: "))

if numero1 > numero2:
    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1 

while menor <= mayor:
    if menor % 2 == 1:
        print(menor)
    menor += 1 

# Imprimir los multiplos de 7 entre 0 y 100

Numero = 0 
while 0 <= Numero <= 100:
    if Numero % 7 == 0:
        print(Numero)
    Numero += 1

# Solicitar un numero al usuario e imprimir su tabla de multiplicar hasta 15 

valor = int(input("ingrese un numero: "))
num = 1 
while num <= 15:
    result = valor * num
    print (f"{num} x {valor} = {result}")
    num += 1 

# Menu 2

# utilizando una variable tipo booleana -> una bandera 
control = True 
while control == True:
    print("1. Entradas\n2. Platos fuertes\n3. Bebidas\n4. Postres\n5. Salir")
    opcion = int(input("elija una opcion: "))
    match opcion:
        case 1: 
            print("1. Patacon con hogao\n2. Dedos de queso\n3. Papas fritas")
            print()
        case 2:
            print("1. Solomito\n2. Spaghetti napolitano\n3. tamal")
            print()
        case 3:
            print("1. Cerveza\n2. Jugo natural\n3. limonadas")
            print()
        case 4:
            print("1. Torta\n2. Muffin\n3. Dulce de leche")
            print()
        case 5: 
            control = False
        case _:
            print("Opcion no valida") 
            print()

# utilizando una variable tipo booleana -> una bandera 
# control = True 
while True: #Bucle infinito
    print("1. Entradas\n2. Platos fuertes\n3. Bebidas\n4. Postres\n5. Salir")
    opcion = int(input("elija una opcion: "))
    match opcion:
        case 1: 
            print("1. Patacon con hogao\n2. Dedos de queso\n3. Papas fritas")
            print()
        case 2:
            print("1. Solomito\n2. Spaghetti napolitano\n3. tamal")
            print()
        case 3:
            print("1. Cerveza\n2. Jugo natural\n3. limonadas")
            print()
        case 4:
            print("1. Torta\n2. Muffin\n3. Dulce de leche")
            print()
        case 5: 
            break
        case _:
            print("Opcion no valida") 
            print()

# Proxima clase traer los 3 problemas textuales que vamos a resolver 