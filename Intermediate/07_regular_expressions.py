### Expresiones regulares ###

import re

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_second_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_second_string)
#if not(match == None):
#if match != None:
if match is not None:
    print(match)
    start, end = match.span()
    print(my_second_string[start:end])


#print(re.match("Expresiones Regulares", my_string))


# search

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I)
print(findall)

# split

print(re.split(":", my_string))

# sub

#print(re.sub("lección|Lección", "LECCIÓN", my_string))
print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))


# patrones

