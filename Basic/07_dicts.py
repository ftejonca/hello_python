### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Fernando", "Apellido":"Tejón", "Edad":35, 1:"Python"}

my_dict = {
    "Nombre":"Fernando",
    "Apellido":"Tejón",
    "Edad":35,
    "Lenguajes":{"Python", "JavaScript", "C#"},
    1:1.80
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Yaiza"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Maestra Ángeles Díaz"
print(my_dict)

del my_dict["Calle"] #forma de eliminar un solo elemento de un diccionario
print(my_dict)

print("Yaiza" in my_dict)
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys()) #retorna todas las claves
print(my_dict.values()) #retorna todos los valores

my_list = ["Nombre", 1, "Piso"]
print(my_list)

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict["Nombre"] = "Eizan"
my_new_dict[1] = 4
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "FtejoncaDev")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))