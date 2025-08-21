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
    print ("Su peso es bajo")
elif 18.5 < imc < 24.9:
    print ("Su peso es normal")
elif 25 < imc < 29.9:
    print ("usted tiene sobrepeso")
elif 30 < imc < 39.9:
    print ("usted tiene obesidad")
else:
    print ("usted tiene obesidad extrema")