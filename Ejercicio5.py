# Nota: Un año es bisiesto si es divisible por 4.

def is_bisiesto(number):
    if (number % 4) == 0:
        return True
    else:
        return False


print("Introduce un año:")
year = int(input())
if is_bisiesto(year):
    print("El año", year, "es bisiesto.")
else:
    print("El año", year, "no es bisiesto.")
