"""
manejo de errores
bloque de codigo/try
si este codigo contiene un error se va a ir a un bloque de excepcion y si no se va a un else para despues finalizar
tipado dinamico/donde un tipo sea un string como sea lo podemos pasar a numero
python no es capas de sumar una cadena de texto / numberTwo = "8"
si hay un try debe de haber un except/obligatorio
"""
                                    #excepciones

numberOne = 6 
numberTwo = 7
numberTwo = "8"

"esto solo es para condiciones de true o false"
"estoy asegurandome de que sea entero"
"si estoy seguro de lo que acabo de controlar"
"un criterio de aceptacion"
if type(numberTwo) == int:
    print(numberOne + numberTwo)
else:
    print("que no se cumpla")

#TRY except
"nuestro programa se ha creado a base de detectar errores"
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    #se ejecuta si se produce una excepcion
    print("Se ha producido un error")


#TRY except else
"esta linea solo se ejecuta si el margen de error no alcansa el except"

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    #esto se ejecuta si no se produce una exepcion 
    print("La ejecucion continua correctamente")

#TRY except else finally
"se ejecuta siempre pase lo que pase"
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:#opcional
    #esto se ejecuta si no se produce una exepcion 
    print("La ejecucion continua correctamente")
finally:#opcional
    #se ejecuta siempre
    print("continua")

# Excepciones por tipo
"este bloque se ejecuta solo si se produce TypeError"  
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError: 
    #se ejecuta si se produce una excepcion
    print("Se ha producido un error")
except ValueError:#si se produce un error a valores muy concretos/tipo
    #se ejecuta si se produce una excepcion
    print("Se ha producido un error")

# Captura de la informacion de la excepcion
"ver los valores/informacion de los errores que puede contenr nuestro programa"
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
#"excepcion concretas"
except ValueError as error:
    print(error)
#"excepcion generica"
except Exception as exception:
    print(exception)
