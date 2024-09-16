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


class estudiante(persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
    def presentarse(self):
        print(f'Mi nombre es {self.nombre}, tengo {self.edad} años y soy estudiante')


empleado = empleado('Brenda', 25, 50000)
estudiante = estudiante ('Luis' , 20)
lista_objetos = [estudiante, empleado]

for persona in lista_objetos:
    persona.presentarse()


class persona:
    def __init__(self, nombre, edad):
        self._nombre= nombre
        self._edad= edad

        @property
        def nombre(self):
            return self.nombre

        @property
        def edad(self):
            return self.edad

        @nombre.setter
        def nombre(self):
            if not value:
                raise ValueError('El nombre no puede estar vacio')
            self._nombre= value

        @edad.setter
        def edad(self):
            if not value:
                raise ValueError('La edad no puede estar vacia')
            self._edad

individuo = persona('Juan', 25)
individuo.nombre = 'Pedro'
print(individuo.nombre)

