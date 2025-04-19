### Módulos ###

import module

module.sum_value(5, 3, 5)
module.print_value("Hola Python")

from module import sum_value, print_value

sum_value(5, 3, 1)
print_value("Hola Python")

import math

print(math.pi)
print(math.pow(2, 2))
print(int(math.pow(2, 2)))

from math import pi as pi_value

print(pi_value)