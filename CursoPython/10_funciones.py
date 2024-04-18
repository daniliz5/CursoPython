"""
las funciones basicamente intentamos encapsular una logica muy concreta
evitar errores
el poder agarrar trocitos de codigo y agruparlos
una funcion en realidad puede devolver y recivir codigo
pasando valores concateados/tuplas
"""
                                        #Funciones
"todo lo que tenemos tabulado pertenece a esta funcion"
def my_function ():
    print("Esto es una funcion")
"he llamdo a mi funcion para que realize una tarea"
my_function ()
"nos permite hacer varias cosas"
"parametros de entrada/salida"
"la opcion se ejecuta pero no retorna ningun valor"
def sum_two_values (first_number, second_number):
    print(first_number + second_number)

sum_two_values (4,9)
sum_two_values (16482,16872987)
sum_two_values (1.57,6.7)

"nos indica que se ejecuta y retorna el resultado"
""
def sum_two_values_with_return (first_number, second_number):
    my_sum = first_number + second_number
    return my_sum

my_result = sum_two_values (1.57,6.7)
print(my_result)

my_result = sum_two_values_with_return (15,30)
print(my_result)

"se accede a los valores que se van a concatenar"
def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname="Meza", name="Dania" )

"parametros por defectos"
"un valor por defecto=puedo llamar con o sin parametro"
def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Dania","Meza")
print_name_with_default("Dania","Meza", "Didi" )

"con el asterisco yo le puedo pasar todo los parametros que yo quiera"
"numero de parametros dinamico"
"cuando tenemos un parametro del mismo tipo y se lo queremos pasar a un ciclo"
def print_texts(*texts):
    print(texts)
print_texts("Hola","python","Dania")
print_texts("Hola")

"imprimir textos con parametros arbritarios"
def print_texts(*texts):
    for text in texts:
        print(text)
print_texts("Hola","python","Dania")
print_texts("Hola")