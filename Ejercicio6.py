# En este ejercicio vais a crear la clase Vehículo,
# la cual tendrá los siguientes atributos:
# - Color
# - Ruedas
# - Puertas
#
# Por otro lado, crearéis la clase Coche,
# la cual heredará de Vehículo y tendrá los siguientes atributos:
# - Velocidad
# - Cilindrada
#
# Por último, tendrás que crear un objeto de la clase Coche
# y mostrarlo por consola.

class Vehiculo:
    def color(self):
        return "Rojo"

    def ruedas(self):
        return 4

    def puertas(self):
        return 5


class Coche(Vehiculo):
    def velocidad(self):
        return 200

    def cilindrada(self):
        return 2000


c = Coche()
print("Color:", c.color())
print("Ruedas:", c.ruedas())
print("Puertas:", c.puertas())
print("Velocidad:", c.velocidad())
print("Cilindrada:", c.cilindrada())
