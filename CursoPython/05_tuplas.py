"""
Que es una tupla?
una tupla es en realidad un conjunto de valores/elementos

las tuplas se pueden definir con su nombre reservado de la tupla
cuando escribimos tuple() es cuando le estamos diciendo que se esta haciendo una tupla
si se le llegara a escribir solo poniendo esto () no seria una tupla, seria una lista

los construcutores tambien llegan a llevar parentesis

cuando en las listas o en algun otro ponemos -1,-2,etc en realidad lo que se hace, es que 
el preograma empieze a contar al reves los valores, pues en vez de iniciar con el primero se inicia con el ultimo.

"""
                                #TUPLA

my_tuple = tuple()
"lista"
my_other_tuple = ()

my_tuple = (20, 1.69, "Dania", "Meza", "Didi")
print(my_tuple)
print(type(my_tuple))

my_other_tuple = ("Dania", "Meza", "Didi",30 , 25)
print(my_tuple)

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Dania"))
"nos dice donde esta el indice"
print(my_tuple.index("Meza"))

"en la lista lo que pasaba es que insertabamos, borrabamos, pero"
"una tupla es inmutable, guardabamos datos y va a ser cerrado"
#my_tuple[1] = 1.75 TypeError: 'tuple' object does not support item assignment
print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

"buscar estos indices completos"
print(my_sum_tuple[3:6])

my_tuple = list (my_tuple)
print(type(my_tuple))

my_tuple[4] = "BLack"
my_tuple.insert(1, "RED")
print(my_tuple)
print(tuple(my_tuple))

"para cambiar una tupla y poderla modificar lo que necesitamos de hacer es convertirla a lista"

"DEL es una herramienta proporcionada del sistema/realizar una tarea completa a lo que se encuentre ahi/calzarla/eliminarla y se acabo"

"no nos podemos cargar un elemento de un unico"
#del my_tuple[2]


#del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined

