"""
Para trabajar con diccionarios se usa la palabra
 kwargs y antes dos **
"""

def usuarios(**kwargs):
    print(kwargs)
    print(type(kwargs))

usuarios(eduardo=[10, 10, 8], fernando=[10,8,9])


#con args y kwargs
def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)

combinacion(1,2,3,4,5, cody=True, curso='Python')