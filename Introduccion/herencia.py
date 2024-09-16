class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años')


class empleado(persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
    def mostrar_salario(self):
        print(f'Mi salario es {self.salario} USD')


empleado = empleado('Brenda', 25, 50000)
empleado.presentarse()
empleado.mostrar_salario()