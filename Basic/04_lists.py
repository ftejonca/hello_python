### Listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [36, 31, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [36, 1.80, "Fernando", "Tejón"]
print(my_other_list)
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count(36))
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

print(my_other_list.index("Fernando"))

age, height, name, surname = my_other_list # posible foco de errores
print(name)


name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] # posible foco de errores
print(name)

print(my_list + my_other_list)
#print(my_list - my_other_list) no funciona, solo se puede concatenar

my_other_list.append("Ftejoncadev") #para insertar al final de la lista
print(my_other_list)

my_other_list.insert(1, "Rojo") #para insertar en la posición elegida pasándola por parámetro
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul") #para eliminar la primera ocurrencia de lo que se quiera eliminar
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop()) #elimina el último valor y lo devuelve
print(my_list)

my_pop_element = my_list.pop(2) #elimina la posición pasada por parámetro y la devuelve
print(my_pop_element) 
print(my_list)

del my_list[2] #elimina el valor elejido en los []
print(my_list)

my_new_list = my_list.copy() #copia todos los valores

my_list.clear() #elimina todos los valores de la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() #da la vuelta a la lista
print(my_new_list)

my_new_list.sort() #ordena de menor a mayor por defecto
print(my_new_list)

print(my_new_list[1:2])

my_list = "Hola Python"
print(my_list)
print(type(my_list)) # tipado débil y dinámico, se puede cambiar el tipo de una variable