### Manejo de excepciones (o manejo de errores) ###

number_one = 5
number_two = 1
number_two = "1"

# try except

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")
    
# try except else finally

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")
    
# Excepciones por tipo de error

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")
    
# Captura de la información de la excepción

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError as error: # Para capturar el tipo de error en una variable y ver la información
    print(error)
except Exception as error: # Para capturar excepciones genéricas
    print(error)
