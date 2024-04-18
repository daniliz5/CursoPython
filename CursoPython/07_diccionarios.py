"""

es lo que conocemos como json

una estrucutura para realcionar datos
de que tipo va a hacer la clave y el valor
podria tener dentro de un diccionario otro diccionario
dato asociado con un valor
la facilidad que tenemos al acceder a un elemento
"""
                                                #DICCIONARIOS

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

"es un tipo de esctructura que podemos almacenar datos de clave valor"
my_other_dict = {"Nombre":"Dania", "Apellido":"Meza", "Edad":20, 1:"Python"}
"es un tipo de esctructura que podemos almacenar datos de clave valor"
my_dict = {
    "Nombre":"Dania",
    "Apellido":"Meza",
    "Edad":20,
    "Languages":{"Python","Swift","Kotlin"},
    1:1.77
}

print(my_dict)
print(my_other_dict)

"por elementos"
print(len(my_other_dict))
print(len(my_dict))

"nos imprime el valor que se guarda en esa clave"
print(my_dict["Nombre"])

"se cambia o actualiza la clave con el valor"
my_dict["Nombre"] = "pedro"
print(my_dict["Nombre"])

"se agregan nuevas claves/campos al diccionario"
my_dict["Calle"] = "20 de noviembre#406"
print(my_dict)

"poder eliminar elementos de nuestros diccionarios"
del my_dict["Calle"]
print(my_dict)

"porque en realidad nostros estamos buscando por clave no por valor=falso"
print("Meza" in my_dict)
"estamos comprovando que esta por valor"
print("Apellido" in my_dict)

#no somos capaces de sacar informacion como tal
print(my_dict.items) 
print(my_dict.keys)
print(my_dict.values)
print(my_dict.fromkeys)

print(my_dict.items()) #listado con cada uno de los sitios
print(my_dict.keys())#solo nos retorna un listado de las keys"claves"/con corchetes en lista
print(my_dict.values())#nos retorna todos los valores

my_lista = ["Nombre", 1, "piso"]
#creamos un lista que pasamos a que imprima un diccionario


#a este puedo pasarle diferentes claves
#crear diccionario en base a ese
my_new_dict = dict.fromkeys((my_lista))
print(my_new_dict)#los que hacemos es crear un diccionario nuevo pero que no tiene valores

#solo se enfoca en las claves
my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)

#no tiene sentido porque todo tendria el mismo valor
my_new_dict = dict.fromkeys(my_dict, "Li")
print(my_new_dict)
