### Lambdas ###

# Son como funciones anónimas, no tienen nombre y se pueden usar para crear funciones de una sola línea,
#  se pueden almacenar en variables.

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 3))

multiply_values = lambda first_value, second_value: first_value * second_value -3
print(multiply_values(2, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))