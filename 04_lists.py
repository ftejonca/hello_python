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

age, height, name, surname = my_other_list # posible foco de errores
print(name)


name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] # posible foco de errores
print(name)

print(my_list + my_other_list)