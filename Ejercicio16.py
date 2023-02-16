# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:
# la columna id de tipo entero,
# la columna nombre que será de tipo texto y
# la columna apellido que también será de tipo texto.
#
# Una vez generada la tabla, tenéis que insertarle datos,
# como mínimo tenéis que insertar 8 alumnos a la tabla.
#
# Por último, tienes que realizar una búsqueda de un alumno por nombre
# y mostrar los datos por consola.

import os
import sqlite3
from sqlite3 import Error

# Obtengo la ruta de trabajo actual y especifico el nombre de la base de datos:
file = f'{os.getcwd()}\\ejercicios.db'

# Creo unas variables con los query's a usar
query_create_table = "CREATE TABLE alumnos(id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL);"
query_check_table = "SELECT * FROM sqlite_master WHERE type='table' AND name='alumnos';"

cursor = None


def main():
    create_table(file, query_create_table)
    insert_data(file)
    get_data(file, "Nombre5")


# Buscamos en la base de datos el nombre indicado y lo imprimimos por pantalla.
def get_data(directory, name):
    global cursor
    conn = None
    try:
        conn = sqlite3.connect(directory)
        cursor = conn.cursor()
        query = f'SELECT * FROM alumnos WHERE nombre="{name}";'
        rows = cursor.execute(query)
        datos = rows.fetchone()
        print(datos)
    except Error as e:
        print(e)
    finally:
        if conn:
            cursor.close()
            conn.close()


# Agregamos los ides, nombres y apellidos a la base de datos
# No se comprueba si los ides ya existen. Si existen nos dara un aviso que ha fallado al añadir el id.
def insert_data(directory):
    global cursor
    conn = None
    i = 0
    try:
        conn = sqlite3.connect(directory)
        cursor = conn.cursor()
        query = '''INSERT INTO alumnos(id,nombre,apellido) VALUES(?,?,?)'''
        while i <= 8:
            datos = (i, f'Nombre{i}', f'Apellido{i}')
            cursor.execute(query, datos)
            i += 1
    except Error as e:
        print(e)
    finally:
        if conn and cursor:
            conn.commit()
            cursor.close()
            conn.close()


# Creamos la tabla alumnos
def create_table(directory, query):
    global cursor
    # si no existe la base de datos, la creamos
    if not os.path.isfile(directory):
        create_db(directory)
        print("Se ha creado la base de datos.")
    conn = None
    # si no existe la tabla, la creamos
    if not check_table(directory, query_check_table):
        try:
            conn = sqlite3.connect(directory, isolation_level=None)
            cursor = conn.cursor()
            cursor.execute(query)
        except Error as e:
            print(e)
        finally:
            if conn and cursor:
                cursor.close()
                conn.close()
            print("La tabla se ha creado")
    else:
        print("La tabla ya existía")


# comprobamos si existe la tabla
def check_table(directory, query):
    global cursor
    table_list = None
    conn = None
    try:
        conn = sqlite3.connect(directory)
        cursor = conn.cursor()
        table_list = cursor.execute(query).fetchall()
    except Error as e:
        print(e)
    finally:
        if conn and cursor:
            cursor.close()
            conn.close()

    if table_list:
        return True
    return False


# creamos la base de datos
def create_db(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    main()
