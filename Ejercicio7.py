# En este ejercicio, tendréis que crear un programa que tenga una clase
# llamada Alumno, que tenga como atributos su nombre y su nota.
# Deberéis definir los métodos para inicializar sus atributos,
# imprimirlos y mostrar un mensaje con el resultado de la nota
# y si ha aprobado o no.

class Alumno:
    def __init__(self):
        self.nombre = None
        self.nota = None

    def iniciar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobado(self):
        if self.nota >= 5:
            return True
        else:
            return False

    def to_string(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)
        if self.aprobado():
            print(self.nombre, "ha aprobado")
        else:
            print(self.nombre, "ha suspendido")


alumno = Alumno()
alumno.iniciar("David", 7)
alumno.to_string()
