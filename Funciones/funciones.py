'''
funcion: menu
parametros de entrada: Ninguno
Ejecucion: Imprimir en pantalla 4 opciones diferentes. Solicitar que se elija una opcion y la guarda en una variable.
Valor de retorno: opcion elejida.
'''

def menu():
    print("1. Encabezado\n2. Porcentaje\n3. Mensaje\n4. salir")
    opcion = int(input("Elija un opcion: "))
    return opcion

def encabezado(Mensaje):
    print("Id: 000540191\nNombre: Alejandro LLano\nCarrera: Aeronautica")
    print(Mensaje)

def Porcentaje(valor_total,porcentaje):
    Valor_porcentaje = valor_total * porcentaje
    return Valor_porcentaje

def Mensaje():
    print("cerrando el programa")


i = True
while i == True:
    eleccion = menu()
    match(eleccion):
        case 1:
            mensaje = input("Ingresa un mensaje: ")
            encabezado(mensaje)
            #imprimir informacion sobre ustedes. 
            # Parametro:Mensaje que se imprime (3 lineas de texto)
        case 2:
            Valor= float(input("Ingresa un valor"))
            Percent = float(input("Ingresa un porcentaje como numero sin el %"))
            print(Porcentaje(Valor,Percent))
            # parametro 1: Valor total
            # parametro 2: Porcentaje
            # Retorno: Valor del porcentaje  
        case 3:
            Mensaje()
            # No recibe ningun parametro ni devuelve ningun resultado
            # Imprime en pantalla un mensaje de cierre de programa 
        case 4: 
            i == False

