diccionario  ={"a" : 1, "b" : 2, "c" : 3, "d" : 4}

#del elimina la llave que coloquemos dentro de los corchetes
del diccionario ["a"]

print(diccionario)


#.pop extrae el valor pero igual lo elimina del diccionario
valor=diccionario.pop("b")
print(valor)
print(diccionario)

diccionario.clear() #elimina todos los elementos del dicionario
print(diccionario)