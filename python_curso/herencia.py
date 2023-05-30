

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