### Clases ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
my_person = Person("Fernando", "Tejón")
print(f"{my_person.name} {my_person.surname}")

class PersonTwo:
    def __init__(self, name, surname, alias = "sin alias"):
        self.full_name = f"{name} {surname} ({alias})" # Propiedad pública
        self.__name = name # Propiedad privada
        self.__surname = surname
        
    def get_name(self):
        return self.__name
        
    def walk (self):
        print(f"{self.full_name} está caminando")
    
my_person_two = PersonTwo("Fernando", "Tejón")
print(my_person_two.full_name)
print(my_person_two.get_name())
my_person_two.walk()

my_other_person = PersonTwo("Yaiza", "Sánchez", "Trimami")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Ariadna Tejón Sánchez (frasquita)"
print(my_other_person.full_name)