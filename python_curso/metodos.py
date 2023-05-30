

class Usuario:


    def inicializar(self, username, password):
        #Añadiendo atributos al objeto
        self.username = username
        self.password = password

user1 = Usuario()
user2 = Usuario()

user1.inicializar('User1', 'password1')
user2.inicializar('User2', 'password2')

print(user1.__dict__)
print(user2.__dict__)


# metodo init
# Definir e inicializar atributos para los objetos de una misma clase
class Usuario:
    # cuando el bjeto sea instanciado 
    def __init__(self, username='', password=''): #metodo init
        self.username=username
        self.password = password

user1= Usuario('User1', 'password1')
user2= Usuario('User2', 'password2')
user3= Usuario()

print(user1.__dict__)#es un diccionario
print(user2.__dict__)
print(user3.__dict__)