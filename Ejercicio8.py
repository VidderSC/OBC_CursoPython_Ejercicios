# En este ejercicio tendréis que crear un módulo que contenga
# las operaciones básicas de una calculadora:
# sumar, restar, multiplicar y dividir.
# Este módulo lo importaréis a un archivo python y llamaréis
# a las funciones creadas.
# Los resultados tenéis que mostrarlos por consola.

import calculadora

a = 10
b = 2

suma = calculadora.sumar(a, b)
resta = calculadora.restar(a, b)
multiplicacion = calculadora.multiplicar(a, b)
division = calculadora.dividir(a, b)

print("La suma de", a, "y", b, "es:", suma)
print("La resta de", a, "y", b, "es:", resta)
print("La multiplicación de", a, "y", b, "es:", multiplicacion)
print("La división de", a, "y", b, "es:", division)
