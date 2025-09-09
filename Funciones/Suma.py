'''
def suma(a, b):
	resultado = a + b
	return resultado


#Llamando a la función

# Con variables
numero1 = 5
numero2 = 3
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")
# Con numeros 
print(suma(9898,564))
# No se debe hacer
suma(45, 78)
'''

'''
# crear una funcion que imprima cualquier numero - bucle for 

def tabla(num):
    for i in range(1,11):
        producto = i * num
        print(f"{num}x{i}={producto}")
	# esta funcion no tiene ningun retorno

# llamado a la funcion 

numero = int(input("Ingrese un valor: "))
tabla(numero)
'''