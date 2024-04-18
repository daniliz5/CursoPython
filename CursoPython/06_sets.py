"""
python es dinamico
tiene una raiz y una lista
las palabras reservadas/una funcion que se va a construir 
set/tipo de dato
no son datos inmutables/se pueden agregar datos
en los set no se save donde se guardan los elementos, y no nos deja acceder a un elemento en concreto
elemtos o objetos que no se repitan
un set por dentro funciona con has mats
igual en lo que pasaba en los demas, los sets los podemos crear o cambiar a tipo lista
"""
                                    #SETS

my_set = set()
my_other_set = {}


print(type(my_set))
print(type(my_other_set)) #inicialmente es un diccionario


my_other_set = {"Dania","Meza",20}
print(type(my_other_set))

print(len(my_other_set))

"lo ordena por un hast interno"
"un set no es una estructura ordenada"
"no podemos acceder a un indice como tal"
my_other_set.add("daniameza")
print(my_other_set)
"un set no admite repetidos"
my_other_set.add("daniameza")
print(my_other_set)

"posibilidad de hacer consultas/busquedas/si esta o no esta"
print("daniameza" in my_other_set)
print("danyameza"in my_other_set)

"borrar registros"
my_other_set.remove("daniameza")
print(my_other_set)

"el clear acaba de borrar todo en nuestro set"
my_other_set.clear()
print(len(my_other_set))
"borrar objetos en concreto del objeto/nos cargamos el programa"
#del my_other_set()
#print(my_other_set)SyntaxError: cannot delete function call

my_other_set = {"Dania","Meza",20,1.69}
"porque no se dulican/no aceotan duplicados"
my_new_set = my_set.union(my_other_set)
print(my_new_set)

"le estamos encontrando la diferencia/"
print(my_new_set.difference(my_set))