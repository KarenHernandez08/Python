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


#Asignación de argumentos en un parametro con 3mparametros
def combincion(p1, p2, *args):
    print(p1)
    print(p2)
    print(args)

combincion(10,20,1 ,2,3, 4, 5, 6, 7, 8)