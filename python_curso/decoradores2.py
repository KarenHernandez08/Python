

def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):#funcion c tiene más funciones a realizar
        print ('Antes del llamado')

        resultado= funcion_b(*args, **kwargs)

        print('despues del llamado')

        return resultado

    return funcion_c

@funcion_a
def suma(n1, n2):
    return n1 +n2
resultado= suma(10, 20)
print (resultado)