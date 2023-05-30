"""
Un decorador es una función que tiene como objetivo extender
funcionalidades a una función.


Una función que toma un input como valore de entrada
y a su vez retorna otra función

a -> la funcion principal (decorador)
b -> la funcion de decorar
c -> la funcion decorada

a(b) --> c
"""


def funcion_a(funcion_b):
    def funcion_c():
        print ('Antes del llamado')
        funcion_b()

        print('despues del llamado')

    return funcion_c

@funcion_a
def saludar():
    print('hola, nos encontramos en funcion a')

saludar()
    