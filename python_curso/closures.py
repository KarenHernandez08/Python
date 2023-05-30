#funciones pueden retornar funciones
def saludar():

    def mensaje():
        print('hola')

    return mensaje

respuesta = saludar()
respuesta()

"""    
      CLOSURES
Una función que genera de forma dinamica a otra función y
esta función puede acceder a las variables locales, aunque 
la primera haya finalizado
"""

def saludar(username):
    mens = f'hola {username}'

    def mensaje():
        print(mens)

    return mensaje

username = 'Karen'
respuesta = saludar(username)
respuesta()