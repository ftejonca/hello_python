### Tipos de errores ###

# SyntaxError -----------------------------------------------------------------------------------------------------

# print "Hola comunidad!" # Error
print ("Hola comunidad!")

# NameError -----------------------------------------------------------------------------------------------------
language = "Spanish" # Comentar esta declaración para forzar error
print(language)

# IndexError -----------------------------------------------------------------------------------------------------

my_list = ["Python", "JavaScript", "C#", "Java", "SQL"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # Descomentar para error

# ModuleNotFoundError -----------------------------------------------------------------------------------------------------

#import maths # Descomentar para error
import math

# AttributeError

#print(math.PI) # Descomentar para error
print(math.pi)

#KeyError -----------------------------------------------------------------------------------------------------

my_dict = {"Nombre":"Fernando", "Apellido":"Tejón", "Edad":35, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apelido"]) # Descomentar para error
print(my_dict["Apellido"])

# TypeError -----------------------------------------------------------------------------------------------------

# print(my_list["0"]) # Descomentar para error
print(my_list[0])
print(my_list[False]) # False siempre vale 0, mala práctica hacer esto
print(my_list[True]) # True siempre vale 1,  mala práctica hacer esto

# ImportError -----------------------------------------------------------------------------------------------------

#from math import PI # Descomentar para error
from math import pi
print(pi)

# ValueError -----------------------------------------------------------------------------------------------------

#my_int = int("10 anios") # Descomentar para error
my_int = int("10")
print(type(my_int))

# ZeroDivisionError -----------------------------------------------------------------------------------------------------

#print(4/0) # Descomentar para error
print(4/2)