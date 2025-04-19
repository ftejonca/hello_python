### Tuplas ###

""""
Las tuplas son inmutables,
se pueden guardar valores en ellas
pero no se pueden modificar una vez declaradas
"""

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (36, 1.80, "Fernando", "Tejón", "Fernando")
my_other_tuple = (36, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Fernando"))
print(my_tuple.index("Tejón"))
print(my_tuple.index("Fernando"))

#my_tuple[1] = 1.80 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(my_tuple)
print(type(my_tuple))
my_tuple[4] = "ftejoncadev"
my_tuple.insert(1, "Azul")

my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple #elimina la tupla al completo, no es propio de las tuplas
#print(my_tuple) NameError: name 'my_tuple' is not defined