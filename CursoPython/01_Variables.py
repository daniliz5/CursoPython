"""
hay funciones que son capaces de hacer algo
en python la forma en que estamos trabajando para nombrar o crear variabales es simplemente con texto

nosotros para definir una variable

camel cates=siguiendo un camello, es decir, cada vez que tenemos la primera letra de una palabra lo habitual es empezarlo miniscula

las variables las podemos nombrar de cuaquier forma, pero ahi algunas combenciones, suelen ser "escribir en minusculas y en snetcase _"
    no queremos hacer variables largas porque nos hace perder tiempo.

esta haciendo una especie de intrepetado para irnos diciendo donde estan los errores

una variable puede mutar su valor


"""
                            #VARIABLES

my_variable = 'my string variable'
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))
#acabamos transformandolo en una cadena de texto

my_bool_variable = False
print(my_bool_variable)

"""
print puede llevar diferentes argumentos/tipos/es capas de tomar todas las variables y 
convertirlas en una cadena de texto, con la coma es pasarle diferentes tipos en una misma y separarlos
tambien puede recibir parametros
puede ayudarnos a ver datos en consola
"""
# Concatenacion de variables en print/cadenas
print(my_variable, my_int_to_str_variable, my_bool_variable)
print("Este es mi valor de:", my_bool_variable)

# Funciones del sistema
"""
la funcion len lo que hace es contar
es para calcular la longitud de una cadena de texto
"""
print(len(my_variable))

#Variables en una sola linea
"""podemos definir variables en una sola linea, pero no es lo mas correcto o lo ideal"""

name, surname, alias, age = "Dania", "Hernandez", "d", 20
print("me llamo:", name, surname, "mi edad es:", age, "Y mi alias es:", alias)

#input
"""esto se puede llegar a utilizar en la terminal/aplicaciones"""

name = input('What is your name? ')
age = input('How old are you? ')

print(name)
print(age)

# cambiar su tipo
name = 20
age = 'dania'
print(name)
print(age)

#forzamos el tipo
#especificamos que solo o que queremos que sea string
address: str = "Mi direccion"
address = True
address = 5
address = 2
print(type(address))
