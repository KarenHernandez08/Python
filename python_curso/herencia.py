

class Mascota: #clase padre

    def comer (self):
        print('La mascota come')

    def dormir(self):
        print('La mascota duerme')


class Perro(Mascota): #clase hija, entre parentesis se pone la clase que vamos a heredar

    pass

duke = Perro()#la clase hija 
duke.comer()#imprime el mensaje que esta en la clase mascota(padre)
duke.dormir()



"""
      HERENCIA MULTIPLE
python permite la herencia multiple, una clase puede heredar de 
multiples clases
"""
class Animal:
    def comer (self):
        print('El animal come')

    def dormir(self):
        print('El animal duerme')


class Mascota(Animal): #clase padre ouede tabien heredar

    pass

class Felino:
    def cazar(self):
        print('el perro caza')

class Perro(Mascota, Felino): #las clases separadas por una , aquellas clases a heredar

    pass

duke = Perro()#la clase hija 
duke.comer()#imprime el mensaje que esta en la clase mascota(padre)
duke.dormir()
duke.cazar()#este de de la clase felino