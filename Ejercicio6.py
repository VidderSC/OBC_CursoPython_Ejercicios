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
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Car(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "Color {}, {} ruedas y {} puertas. Velocidad: {} Km/h, {} cc.".format(self.color, self.ruedas, self.puertas, self.velocidad, self.cilindrada)


coche = Car("Rojo", 4, 5, 180, 2000)
print(coche)
