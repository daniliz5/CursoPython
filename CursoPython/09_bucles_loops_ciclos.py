"""
loop y blucles es lo mismo
de los grandes mecanismos
es un mecanismo que nos ayuda a reiterar 
que es reiterar? nos sirve para pasar por el mismo codigo varias veces
nso da la opcion de repetir cuando nosotros queramos

"""
                                    #bucles/loops/ciclos

#WHILE
"tenemos que ponerle una condicion"
"mientras sea verdadero has algo"
my_condition = 0
"""
siempre imprime 0 finitas veces
while my_condicion < 10:
    print(my_condicion)
"""
"while es como un if infinito"
"si la condicion nunca cambia seria un bucle inifinito"
"si cambia esperemos que en algun momento la condicion se cumpla"
while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: #es opcional
    print("Mi condicion es mayor o igual que 10")

print("la ejecucion continua")

"nosotros podemos tener dentro de un while condiciones simples"
"el break nos va a permitir parar el programa si o si"
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break
    print(my_condition)

print("la ejecucion continua")

#FOR
"""
que se cumpla una condicion
nos sirve para iterar un listado de elementos
"""
my_list = [20, 21, 32, 21, 17]
"for se va a repetir tantas veces como los elementos que tenga"
"esta atado a un numero finito de datos"
"haber cuantos elementos le estamos indicando dentro de una iteracion"
for element in my_list:
    print(element)

my_tuple = (20, 1.69, "Dania", "Meza", "Didi")
for element in my_tuple:
    print(element)

my_other_set = {"Dania","Meza",20}
for element in my_other_set:
    print(element)

my_other_dict = {"Nombre":"Dania", "Apellido":"Meza", "Edad":20, 1:"Python"}
"cuando nosotros rompemos el bucle lo demas no se imprime"
for element in my_other_dict:
    print(element)
    if element == "Edad":
        break
    print("se ejecuta")
else:
    print("El bucle for para mi diccionario a finalizado")

my_other_dict = {"Nombre":"Dania", "Apellido":"Meza", "Edad":20, 1:"Python"}
"nos ayuda a continuar el programa/sea capas para hace algo que nosotros queremos"
"detiene la ejecucion a ese punto"
"vuelve al for sin ejecutar lo de abajo"
for element in my_other_dict:
    print(element)
    if element == "Edad":
        continue
    print("se ejecuta")
else:
    print("El bucle for para mi diccionario a finalizado")



