### Funciones de orden superior ###

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def  sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))


### Closures ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))

print(sum_ten(5)(1))

### Funciones de orden superior del propio lenguaje de Python ###

numbers = [2, 5, 10, 21, 3, 30]

# Map, recorre todos los valores y ejecuta una función sobre ellos para modificar su valor

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter, recorre todos los valores y ejecuta una función que retorna True o False para saber como filtrar los valores del iterable

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

def filter_smaller_than_ten(number):
    if number < 10:
        return True
    else:
        return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))
print(list(filter(filter_smaller_than_ten, numbers)))
print(list(filter(lambda number: number < 10, numbers)))

# Reduce, opera entre los valores que va recorriendo, va operando con los valores que va teniendo en cada caso a medida que se recorre el iterable

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value


print(reduce(sum_two_values, numbers))