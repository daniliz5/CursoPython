"""
ya no es un tipo de base como tal
es que ya estamos hablando de una estructura
arrive/arrego
podemos formar pilas y colas
no es lo mismo un arreglo que una lista, pues los arreglos tienen menos aoperaciones
conjunto de elementos que entran por posciones
si tenemos una lista de alguna forma, significa que podemos acceder a estos datos de diferente forma
en el momento que vemos una lista es programacion orientada a objetos
una lista es mutable
esto es una lista "lista()"
esto es una dupal ()
"""
                                                    #Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [20, 21, 32, 21, 17]

print(my_list)
print(len(my_list))

my_other_list = [56, 1.69, "Dania", "Meza"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
"contar elementos de una misma lista"
"retorna el numero de ocurrencias de un valor"
print(my_list.count(21))
#print(my_other_list[4]) indexerror
#print(my_other_list[-5]) indexerror

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] 
print(age)

"ya hemos concatenado dos listas en el orden en que esta"
print(my_list + my_other_list)
#print(my_list * my_other_list)

"una operacion append se agrega el finanl"
my_other_list.append("didi")
print(my_other_list)
"tengo una forma de meter valores en las posiciones "
my_other_list.insert(1, "azul")
print(my_other_list)
"cambiar o modificar"
my_other_list[1] = "negro"
print(my_other_list)

"borra/para eliminar un elemento que nosotros conocemos"
my_other_list.remove("negro")
print(my_other_list)
"para eliminar un elemento que nosotros conocemos"
my_list.remove(21)
print(my_list)
"es el limite del elemento que yo quiero eliminar/desafilado"
print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(1)
print(my_pop_element)

"borrar elementos por posiciones/inidce"
del my_list[1]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)
"es una ordenacion de mayor a menor"
my_new_list.sort()
print(my_new_list)

"crear sublistas"
print(my_new_list[1:2])


my_new_list.reverse()
print(my_new_list)


"podemos trabajar con diferentes tipos de datos y cambiarlo"
"existen tipos de datos, constantes"
"no existe en realidad una constante"
my_list = "Hola mundo"
print(my_list)
print(type(my_list))