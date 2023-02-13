# Crea un script que le pida al usuario una lista de países (separados por comas).
# Estos se deben almacenar en una lista y no debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

print("Introduce una lista de paises separados por comas: ")
paises = input()

# Uso replace para quitar los espacios después de las comas, en caso de que los haya
# Ejemplo: "España, Paises Bajos,Ucrania,Africa, Portugal,Italia,España"
paises = paises.replace(', ', ',')

# Con split dividimos una cadena de texto por el carácter o los caracteres indicados
# y se lo asignamos a nuestro set para evitar duplicados
lista_paises = set(paises.split(','))

# Con sorted, ordenamos la lista de paises (en este caso es ascendente)
lista_paises_ordenada = sorted(lista_paises)

paises_ordenados_comas = ""

for pais in lista_paises_ordenada:
    # comprobamos que no sea el último valor de nuestro set, para no añadir la coma al final.
    if lista_paises_ordenada.index(pais) != len(lista_paises_ordenada)-1:
        paises_ordenados_comas += pais + ", "
    else:
        paises_ordenados_comas += pais + "."

print(paises_ordenados_comas)
