### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente indica que es un dict (diccionario)

my_other_set = {"Fernando", "Tejón", 36}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("ftejoncadev")
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("ftejoncadev") # Un set no admite repetidos
print(my_other_set)

print("Tejón" in my_other_set) #para comprobar si un valor existe o no dentro de un set
print("Tejín" in my_other_set)

my_other_set.remove("Tejón")
print(my_other_set)

my_other_set.clear() #vacía todos los datos elementos del set
print(len(my_other_set))

del my_other_set #elimina la variable directamente por completo
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Fernando", "Tejón", 36}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Python", "JavaScript", "C#"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Japón", "Tokyo"}))

print(my_new_set.difference(my_set))