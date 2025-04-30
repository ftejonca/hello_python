### Manejo de paquetes ###

# PIP
    # pip --version -> para comprobar la versión instalada
    # pip install pip -> para instalar pip
    # pip install --upgrade pip -> para actualizar la versión de pip
    # pip install numpy -> para instalar por ejemplo la libreria numpy
    # pip install pandas -> para instalar por ejemplo la libreria pandas
    # pip list -> lista de instalaciones pip
    # pip uninstall pandas -> para desinstalar por ejemplo pandas
    # pip show pandas -> información sobre por ejemplo pandas

import numpy

print(numpy.version.version)

numpy_array = numpy.array([36, 31, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

import pandas


import requests  # libreria para hacer peticiones a un api

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())


# Paquete Arithmetics

from mypackage import arithmetics

print(arithmetics.sum_two_values(4, 9))

