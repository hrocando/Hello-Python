### Classes ###

# Definición

class MyEmptyPerson:
    pass    # Comando del sistema para establecer una línea de código que no ejecuta una función directa.

print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y popiedades privadas y públicas

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name                              # Propiedad privada

    def get_name(self):
        return(self.__name)

    def walk(self):
        print(f"{self.full_name} está caminado!")

my_person = Person("Brais", "Moure")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de León (El Loco de los Perros)"
print(my_other_person.full_name)

my_other_person.full_name = 876
print(my_other_person.full_name)