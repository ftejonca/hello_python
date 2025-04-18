### Bucles o loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15, se detiene la ejecución")
        break
        
    print(my_condition)
    
print("La ejecución continúa")
    
# For

my_list = [36, 31, 4, 2, 30, 30, 17, 62]
my_list.sort(reverse=True)

for element in my_list:
    print(element)
    
    
my_tuple = (36, 1.80, "Fernando", "Tejón", "Fernando")

for element in my_tuple:
    print(element)

my_set = {"Fernando", "Tejón", 36}

for element in my_set:
    print(element)

my_dict = {
    "Nombre":"Fernando",
    "Apellido":"Tejón",
    "Edad":36,
    "Lenguajes":{"Python", "JavaScript", "C#"},
    1:1.80
    }

for element in my_dict.values(): #para imprimir los valores, imprime las keys por defecto
    print(element)
    if element == 36:
        break
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")
    
print("La ejecución continúa")

for element in my_dict.values():
    print(element)
    if element == 36:
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")
    
    
    for i in range(5):
        print(i)