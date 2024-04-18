"""
podemos operar operaciones matematicas
con todo tipo de numeros

hay operadores que no necesariamente deben de ser de operaciones basicas
la forma mas facil de ver operadores porbablemnete sea con numeros
"""

                        #Operadores Aritmeticos

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
#operador de modulo
"""nosotros establescamos una division/para saver si de verdad ahi un multiplo o lo que sobra"""
print(10 % 3)
#flor division
"""que nostros al final hagamos una divisio y es ta division este aproximada a un numero entero"""
print(10 // 3)
#calcular un exponente
"""multiplicar pero con dos o parecido a la potencia"""
print(2 ** 3)
"""todos los signos se pueden combinar entre ellos"""
print(2 ** 3 + 3 - 7 / 1 // 4)


print("hola "+"python")
print("hola "+ str(5))
print("hola " * 5)
print("hola " * (2 ** 3))
"""eran dos cadenas de texto que termina concatenado
estos signos no solo sirve para calcular numero, si no tambien a cadenas de texto
pero no podemos pempezar a combinar enteros con string, pues entre tipos diferentes no se puede trabajar, para hacer eso 
necesitariamos del STR que nos ayuda a trabsformarlos a tipos string

tipado dinamico/los datos pueden ir variando
"""
my_float = 2.5 * 2
print("hola " * int(my_float))
"""el int me ayuda a transformar lo decimal para poder cambiar su valor y correr el programa"""

                                #Operadores Comparativos
"""operadores para decirnos si son valores verdaderos o falsos"""
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 > 4 ==2)
"""se esta comprobando es uan ordenacion alfabetica cual es mayor de los dos
es a orden en funcion por ASCII"""
print("hola " > "python")
print("hola " < "python")
print("hola " >= "python")
print("hola " <= "python")
print("hola " == "python")
print("hola " != "python")


                                        #Operadores Logicos
"""
la logica booleana rige toda la programacion

"""
print(3 > 4 and "Hola " > "Python")
print(3 > 4 or "Hola " > "Python")
print(3 < 4 and "Hola " < "Python")
"""esta comparando toda la logica booleana """
print(3 < 4 or ("Hola " > "Python" and 4 == 4))
"""el not es para negar toda la condicion/si alguno de los dos es verdadero lo demas se combierte en verdadero"""
print(not(3 > 4))
