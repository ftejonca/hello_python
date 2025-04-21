### Retos ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
#Primera forma de hacerlo(forma que yo implementé)
def fizz_buzz1():
    my_list_numbers = [i for i in range(1, 101)]

    for number in my_list_numbers:
        if (number % 3 == 0) and (number % 5 == 0):
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)
            
#fizz_buzz1()

#Segunda forma de hacerlo
def fizz_buzz2():
    for index in range(1, 101):
        if (index % 3 == 0) and (index % 5 == 0):
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

#fizz_buzz2()

#Forma de hacerlo con el condicional match/case
def fizz_buzz3():
    for index in range(1, 101):
        match (index % 3 == 0, index % 5 == 0):
            case (True, True):
                print("fizzbuzz")
            case (True, False):
                print("fizz")
            case (False, True):
                print("buzz")
            case (False, False):
                print(index)

#fizz_buzz3()


"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def anagrama(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())
        
#print(anagrama("roma", "amor"))

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
la que el siguiente siempre es la suma de los dos anteriores.
0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():
    prev = 0
    next = 1

    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib
        
        
fibonacci()