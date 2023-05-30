#DOCSTRING : Un comentario en la primera línea de código de la función
#colocamos una breve descripción de la tarea de la función

#__doc__ (modulos, clases, métodos, funciones) 

def suma(n1, n2):
    """ 
    La función suma dos numeros enteros.

    Argumentos:
    n1(int)
    n2(int)

    se retorna la suma de los parametros.

    TODO:
        +

    >>> suma(10,20)
    30
    >>> suma(100,200)
    300
    """
    return n1 + n2
#print(suma.__doc__) #esto da la documentación 
print(help(suma))# esta también nos ayudara a dar la documentación

