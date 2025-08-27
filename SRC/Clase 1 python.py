nombre = input("¿Cómo te llamas? ")
print(f"¡Hola, {nombre}!")


#Calcular el IMC : peso / altura^2
#IMC : peso / altura^2

#Leer Estatura
estatura = input ("ingrese su estatura en metros:  ")
estatura = float (estatura)
#Leer peso
peso = input ("ingrese su peso en kilos:  ")
peso = int (peso)
#calcular IMC
imc = peso / estatura ** 2
#Mostrar imc
print ("su imc = ", imc) 

#Se hace la tabla del IMC

if imc < 18.49:
    mensaje = "Su peso es bajo"
elif 18.5 < imc < 24.9:
    mensaje = "Su peso es normal"
elif 25 < imc < 29.9:
    mensaje = "usted tiene sobrepeso"
elif 30 < imc < 39.9:
    mensaje = "usted tiene obesidad"
else:
    mensaje = "usted tiene obesidad extrema"

print(f"{nombre}, su imc es {imc:0.2f} y su condicion es que {mensaje}")