"""       SCOPES (Donde fue creada)
Variables que tienen alacances diferentes, las 
variables globales se pueden usar en cualquier 
bloque, funcion, ciclo, o fuera de cualquier bloque 
etc. y las variables locales solo pueden ser 
utilizadas en ese bloque creadas.
"""
animal = 'Leon' # como no esta dentro de un bloque, se le llama variable global

def imprimir_animal():
    global animal ##no se crea una variable local
    animal= 'Ballena'# Variable local, unicamente se utiliza en el bloque donde fue creada
    print(animal)

imprimir_animal()