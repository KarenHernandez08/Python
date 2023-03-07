mensaje = "Hola mundo"

#ljust -> justifica a la izquierda
#rjust -> justifica a la derecha
#center -> centra el texto

mensaje = mensaje.ljust(20) #se le agregan los espacios añadidos 
hola = mensaje.rjust(20)
centro = mensaje.center(20)

print(mensaje)
print(hola)
print(centro)