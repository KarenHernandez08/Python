"""
          Función range
seremos capaces de crear una secuencia de numeros
enteros que facilmente se pueden iterar

range(10) #va del 0 al 10

range(1,10) #va del 1 al 10, el primer numeró es donde va a 
iniciar nuestra secuencia y el segundo donde acaba

range(1,10,2) va deñ 1 al 0 pero con saltos de 2 en dós
el tercer valor son los saltos
"""



rango= range(1,10,2) #va del 0 al 10

for valor in rango:
    print(valor)

"""
         Función enumerate
la función enumerate nos permite enuerar cada uno
de los elementos de una colección

Regresa una tupla con dos valores, el primero hace referencia al 
índice del elemento dentro de la colección y el segundo al elemento perce de
la coleccón (el valor)
"""


numeros= [10,20,30,40,50]

for indice, numero in enumerate(numeros):
    print(indice, numero)