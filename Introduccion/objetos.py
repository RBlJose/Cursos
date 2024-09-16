class persona:
  def __init__ (self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def presentarse (self):
    print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años')

individuo = persona('Domingo', 23)
individuo.presentarse()
