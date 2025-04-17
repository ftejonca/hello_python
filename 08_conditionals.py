### Condicionales ###

my_condition = False

if my_condition: # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")
    
my_condition = 1 * 1
    
if my_condition == 10:
    print("Se ejecuta la condición del segundo if")
    
if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 1:
    print("Es igual a 1")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecución continúa")