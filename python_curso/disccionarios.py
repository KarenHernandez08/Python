"""Hay dos maneras de declarar un diccionario"""

diccionario = {}
diccionario = dict( )

#{los valores que queremos asociar}
diccionario= {"total" : 55}
print (diccionario)
diccionario={"total":55, "descuento": True}
print (diccionario)


#[son diccionarios inmutables, no pueden cambiar su valor]
elementos = {}
#dentro de la llave se le agrega la llave y después el valor que se le da a la llave

elementos['nombre']= 'Karen' 
print(elementos)
"""
si la llave no existe, la crea
si la llave si existe, actualiza el valor que la llave almacena

"""
elementos['nombre']= 'Jocelyn' #aquí se actualiza la llave con un nuevo valor
print(elementos)
