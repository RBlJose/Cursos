import json

datos = {
    'Nombre' : 'Domingo',
    'edad' : 23,
    'Trabajo' : 'Quant Developer'
}

print(datos, type(datos))

with open('data.txt', 'w') as f:
    json.dump(datos, f)

with open('data.txt', 'r') as f:
    datos_recuperados = json.loads(f.read())
print(datos_recuperados, type(datos_recuperados))

import pickle

with open('datos.pickle', 'wb') as f:
    pickle.dump(datos, f)
with open('datos.pickle', 'rb') as f:
    pickle_file = pickle.load(f)

print(pickle_file, type(pickle_file))

import csv

datos = [
    ['nombre', 'edad', 'ciudad'],
    ['Juan', 30, 'Madrid'],
    ['Ana', 25, 'Barcelona']
]

with open('datos.csv', 'w', newline= "") as f:
    writer_csv = csv.writer(f)
    writer_csv.writerow(datos)

with open('datos.csv', 'r') as f:
    reader_csv = csv.reader(f)
    for file in reader_csv:
        print(file, type(file))