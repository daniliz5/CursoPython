"""
para realizar tareas concretas
realizar de principio a fin un objeto
tiene que responder de una cierta logica
calsificar
identificar nuestro codigo dentro de una clase de actuacion
"""
                                            #Clases
"los nombres de la clases deben de ser con la primera palabra con mayuscula y sin espacios "
class Person:
    pass 
print(Person)
print(Person())

"palabra reservada del sistema para construir un construcutor de clase"
"establecer ciertos valores asociados a"
"el constructor de clase no es inmutable"
""
class MyPerson:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" #propiedad publica
        self.__name = name #propiedad privada

    def get_name (self):
        return self.__name


    def walk (self):
        print(f"{self.full_name} esta caminando")

my_person = MyPerson("Lizeth","Hernandez")
print(my_person.full_name)
my_person.walk()

my_other_person = MyPerson("Maria", "Lopez", "Mari")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Patroclo (falta Patroclo, donde esta?) "
print(my_other_person.full_name)