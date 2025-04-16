### Variables ###

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 7
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea (no es muy buena práctica)
name, surname, alias, age = "Fernando", "Tejón", "ftejoncadev", 36
print("Me llamo", name, surname, ". Mi alias es:", alias, ". Y mi edad es:", age)

# Inputs
"""
name = input("What is your name?")
age = input("How old are you?")
print(name)
print(age)
"""

# Cambiamos su tipo
name = 36
age = "Nando"
print(name)
print(age)

# Forzamos el tipo???
address: str = "Mi dirección"
address = 32
print(address)
print(type(address))