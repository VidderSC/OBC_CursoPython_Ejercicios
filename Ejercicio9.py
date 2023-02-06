# En este segundo ejercicio tendréis que crear un script que nos diga
# si es la hora de ir a casa.
# Tendréis que hacer uso del módulo time.
# Necesitaréis la fecha del sistema y poder comprobar la hora.
#
# En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario,
# haréis una operación para calcular el tiempo que queda de trabajo.

import time

hora = time.localtime()
if hora[3] >= 19 and hora[4] >= 0:
    print("Son más de las 7 de la tarde, hora de irse a casa!")
else:
    if 19 - hora[3] > 1:
        print("Faltan", (19 - hora[3]), "horas y", (60 - hora[4]), "minutos para irse a casa")
    else:
        print("Falta", (19 - hora[3]), "hora y", (60 - hora[4]), "minutos para irse a casa")
