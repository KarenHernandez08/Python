#el nombre de la clase va en mayusculas y es uso de <CamelCase>

class Usuario:
    pass #el bloque no realiza ningun tipo de acción
kar = Usuario()
print (kar)

"""
ATRIBUTOS

Atributos de clase: los cuales les pertenezcan a una clase

Atributos de instancia: atributos los cuales les pertenezcan a un objeto
"""

#atributos de clase, definir variables dentro de la clase
class Usuario:
    username= 'Karen'
    email = ''

Usuario.username='Jocelyn'#para modificar el atributo

print(Usuario.username) #clase + . + el atributo ya sea para lectura o modificar


#atributos de instancia

