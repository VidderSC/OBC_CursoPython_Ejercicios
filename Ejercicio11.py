#!/usr/bin/python
# -*- coding: latin-1 -*-


# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis
# una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo
# y luego lo cargamos.

import pickle


class Vehiculo:
    marca = ""
    modelo = ""

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}'


coche = None
cargado = None


def guardar():
    f = open('vehiculo.dat', 'w+b')
    pickle.dump(coche, f)
    f.close()


def cargar():
    global cargado
    f = open('vehiculo.dat', 'rb')
    cargado = pickle.load(f)
    f.close()


def main():
    global coche
    coche = Vehiculo("Seat", "Leon")
    print(coche)
    guardar()
    cargar()
    print(cargado)


if __name__ == '__main__':
    main()
