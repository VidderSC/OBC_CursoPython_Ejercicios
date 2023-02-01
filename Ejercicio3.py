# Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase 
# "Tu índice de masa corporal es " donde es el índice de masa corporal calculado redondeado con dos decimales.

import math

peso = float(input("Introduce tu peso (Kg): "))
estatura = float(input('Introduce tu estatura (Metros): '))

IMC = round(peso/math.pow(estatura,2),2)

print('Tu masa corporal (IMC) es: ' + str(IMC))
