"""
los string pueden llevar ciertos caracteres
crear scripts

"""
                                    #String

my_string = "mi string"
my_other_string = "mi Otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\n escapiado"
print(my_scape_string)

                        #formateo
"""
internacionando texto
concatenando
si estamos tirando/formateando datos
{} se usa para imprimir tal cual el objeto
%s%d%f si en realidad estamos trabajando con el numero formateado
"""
name, surname, age = "Dania", "Meza", 20

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(surname, name, age))
"""una forma en la que vemos tal cual donde queremos los datos "f" sirve para formatear"""
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

                        #Desenpaquetado de caracteres
"dependiendo el texto vamos a poner la cantidad de palabras"
language = "python"
a, b, c, d, e, f= language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

                        #Division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-1]
print(language_slice)
"""evitar datos que no queremos"""
language_slice = language[1:2:4]
print(language_slice)


                        #Reverse 

reverse_language = language[::-1]
print(reverse_language)


                        #Funciones del sistema

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("py"))
print("py" == "Py")