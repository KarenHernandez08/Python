"""
Funcion que retorna objetos que facilmente 
se puedan iterar sin que finalice
"""

#numeros pares del 0 al 100

def pares():
    for numero in range(0,100,2):
        yield numero #yield suspenderemos de forma momentanea la ejecucón de la fucnion 
    
        print('un mensaje después de return')

for par in pares():

    print(par)



def pares():
    for numero in range(0,100,2):
        yield numero #yield suspenderemos de forma momentanea la ejecucón de la fucnion 
    
        print('Distribución perezosa')

generador =pares()
while True:
    try: 
        par=next(generador)
        print(par)
    except StopIteration:
        print("El generador Finalizo")
        break