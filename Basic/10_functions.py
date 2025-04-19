### Funciones ###

def my_function ():
    print("Esto es una función")
    
my_function()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(1231513413614, 6878434251462)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")
    
print_name(surname = "Tejón", name = "Fernando")

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Yaiza", "Sánchez", "Trimami")
print_name_with_default("Yaiza", "Sánchez")

def print_texts(*text): # el * sirve para pasar todos los parámetros que queramos de ese tipo de dato
    print(text)
    
print_texts("Hola", "Python", "ftejoncadev")
print_texts("Hola")

def print_upper_texts(*texts):
    for text in texts:
        print(type(texts))
        print(text.upper())
        
    
print_upper_texts("Hola", "Python", "ftejoncadev")
print_upper_texts("Hola")


