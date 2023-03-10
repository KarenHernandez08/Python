"""
Existen dos palabras las cuales nos permitiran
modificar el comportamiento de nuestros ciclos
ya sea en el ciclo while o un cico foreach
1. break: finaliza de manera inmediata
2. continue: pasa a la siguiente iteracción
"""

titulo="Harry potter"
for caracter in titulo: #Vemos cada uno de los caracteres
    print(caracter)

#Cuando el caracter sea igual a "t" se finnalizara y solo se imprime lo que estaba antes
for caracter in titulo: 
    if caracter == "t":
        break
    print(caracter)

#Hara que el ciclo salte, excentuando el caracter
for caracter in titulo: 
    if caracter == "t":
        continue
    print(caracter)

