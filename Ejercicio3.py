import math

peso = float(input("Introduce tu peso (Kg): "))
estatura = float(input('Introduce tu estatura (Metros): '))

IMC = round(peso/math.pow(estatura,2),2)

print('Tu masa corporal (IMC) es: ' + str(IMC))
