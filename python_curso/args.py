"""    ARGUMENTOS
Agregar el * pegado al parametro, indica 
que todos los argumentos se genere una tupla
sin uso de corchetes y deben de nombrarse como *args
"""

def promedio(*args):
    
    return sum(args)/ len(args)

#resultado = promedio([10,10,5,7,10])
resultado = promedio(10, 10, 5, 7, 10)
print (resultado)