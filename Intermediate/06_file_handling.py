### Manejo de ficheros ###

import os # con esto podemos eliminar ficheros
import json

# Fichero .txt

#txt_file = open("Intermediate/file.txt", "r+") # r+ para leer y escribir
txt_file = open("Intermediate/file.txt", "w+") #  w+ para escribir y leer (pero sobreescribe el contenido del fichero)
txt_file.write("Mi nombre es Fernando \nMi apellido es Tejón\nTengo 36 años\nY mi lenguaje preferido es Python")

# print(txt_file.read())
print(txt_file.read(10)) #lee y printea los 10 primeros caracteres
print(txt_file.readline()) # lee línea a línea
print(txt_file.readline())
# print(txt_file.readlines()) # lo lee como un array de elementos de cada línea
for line in txt_file.readlines():
    print(line)

txt_file.write("\nY mi videojuego favorito es el expedition 33")
print(txt_file.readline())

txt_file.close()

#os.remove("Intermediate/file.txt")


# Fichero .json

json_file = open("Intermediate/file.json", "w+")

json_test = {
    "nombre":"Fernando",
    "apellido":"Tejon",
    "edad":35,
    "lenguajes":["Python", "JavaScript", "C#"],
    "videojuego": "expedition 33"}

json.dump(json_test, json_file, indent= 4)

for line in json_file.readlines():
    print(line)