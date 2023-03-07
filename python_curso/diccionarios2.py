diccionario  ={"a" : 1, "b" : 2, "c" : 3, "d" : 4}
 
"""para obtener un valor, se declara una variable, 
llamamos al diccionario y depúes entre corchetes la
 llave de la que vamos a obtener el valor"""

valor =diccionario["d"]
print (valor)

"""
el in quiere decir que si esta en el diccionario
si esta en el diccionario imprime un valor booleando True
si no esta en e diccionario imprime un valor booleando False
print('a' in diccionario)
"""

#get para obtener tambien el valor de una llave
#si la llave a buscar no existe, imprime un None
#se puede colocar un mensaje despúes de la llave para que cuando no exista, se imprima el mensaje
valor = diccionario.get("z", "No existe")
print(valor)

"""
.setdefault va a retornar el valor de la llave
si la llave no existe se le agrega el valor dentro de el diccionario
a la hora de imprimir el diccioanrio ya se mostrara el valor de e
valor =diccionario.("e",5)
print(valor)
print(diccionario)
"""

# devuelve solo las llaves
llaves = tuple(diccionario.keys())
print(llaves)

#devuelve solo los valores
valores=tuple(diccionario.values())
print(valores)

#devuelven las tuplas, la llave y el valor que le corresponde a la llave
elementos= tuple(diccionario.items())
print(elementos)

