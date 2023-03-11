"""Así podemos crear una funcion con la palabra reservada "def"
el nombre de la función va a seguir la nomenclatura, si la variable 
tiene 2 palabras se unen con "_" y siempre en minusculas
Las variables que estan dentro de la función o el parentesis se 
llaman PARAMETROS : y el bloque, para que nosotros podamos llamar la 
función basta con colocar el nombre de la función y parentesis, dentro
de los parentesis, los argumentos

Nos ayudan a disminuir tareas complejas"""


def suma():
    numero_uno = int(input("Ingresa el primer numero: "))
    numero_dos = int(input("Ingresa el segundo numero: "))
    resultado = numero_uno + numero_dos
    print(resultado)

suma()

"""
      Funciones con 2 parametros
Las funciones la mayoria de veces necesitan valores de entradas
variables como parametros
va el def, despues el nombre y en el parentesis van a ir los 
parametros, se van a separar por una ","

Las variables parametros son unicamente declarados por el uso del bloque
Los valores de entrada se conocen como argumentos
"""

def suma(numero_uno, numero_dos):
    
    resultado = numero_uno + numero_dos
    print(resultado)

numero_uno = int(input("Ingresa el primer numero: "))
numero_dos = int(input("Ingresa el segundo numero: "))

suma(numero_uno, numero_dos)


