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


