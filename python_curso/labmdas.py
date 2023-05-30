#  CIUDADANOS DE PRIMERA CLASE

def centigrados_a_farhenheit(grados):
    return grados * 1.8 +32


funcion = centigrados_a_farhenheit #este es de tipo funcion

print(funcion(10))


"""
        LAMBDA
es una función expresada en una sola línea de codigo,
no posee nombres.

la palabra lambda + parametros + : + cuerpo de la funcion
"""

funcion_grados = lambda grados : grados *1.8 +32

print(funcion_grados(10))


