"""
los condicionales nos representa flujos de ejecucion de nuestro codigo
esto quiere decir si se ejecuta o no 
desiciones
si se cumple una condicion se ejecuta lo que esta dentro de la condicional
"""
                                        #CONDICIONALES

my_condition = False

"las dos lineas han funcionado y se han compilado"
"al momento que el if sea verdadera se ejecuta"
"quiere decir que debe de ser verdadera lo que tengamos dentro del if para poder compilarlo"
if my_condition: #es lo mismo poner/especificar if my_condition == True, funciona igual
    print("Se ejecuta la condicion del if")
#print("la ejecucion continua")
"no se ha imprimido porque mi condicion es falsa"
my_condition = 6 * 6
#"ahora aqui, se ha especificado la condicion "
if my_condition == 36: 
    print("Se ejecuta la condicion del segundo if")

#"toma el valor booleano si es true o false"
elif my_condition > 16 and my_condition < 20: 
    print("Es mayor que 36")

#if/elsi necesitan una condicion
#comprobacion
#si no se cumple esto, va a comprobar esto y si no se cumple esto va a comporbar esto
elif my_condition == 36:
    print("Es igual a 36")

#si algo, haz esto y si no haz lo que tengo aqui"
#si esto es igual que esto se cumple, si no, haz esto
else:
    print("Es menor o igual que 36 o mayor o igual que 20 o distinto de 36")


print("la ejecucion continua")

#si tenemos un valor vacio lo interpreta como false

my_string = ""

"si estamos negando que mi cadena de texto sea vacia, quiere decir que lo es"
if not my_string:
    print("Mi cadena de texto es vacia")
if my_string == "Mi cadena de textoooo":
    print("Estas cadenas de texto coinciden")



