"""
          Ciclo While
Nos permite ejecutar una n cantidad de veces un 
bloque de código hasta que una condicón se cumpla
"""

contador =1

while contador <=10:
    print(contador)
    contador = contador + 1
    

numero = 12345
contador_digitos=0
while numero >1:
    contador_digitos = contador_digitos+1
    numero = numero /10
print(contador_digitos)


"""Tiene una manera de simplificar el contador =contador +1
quedaria como contador +=1
Así mismo en el ciclo while se puede usar else si se necesitara
"""
