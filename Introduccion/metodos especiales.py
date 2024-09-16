class vector:
    def __init__(self, x, y):
        self.x= x
        self.y= y
    def __str__(self):
        return f'{self.x}, {self.y}'
    def __add__(self, otro_vector):
        return vector(self.x + otro_vector.x, self.y + otro_vector.y)
    def __sub__(self, otro_vector):
        return vector(self.x - otro_vector.x, self.y - otro_vector.y)


vector1 = vector(2,3)
vector2 = vector(4,1)
print(vector1)
print(vector1 + vector2)
print(vector1 - vector2)