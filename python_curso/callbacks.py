promedio = lambda *args: sum(args) / len(args)


aprobado = lambda calificacion : calificacion >=7

def mensaje(prom, aprob, *args):
    promedio = prom(*args)
    
    if aprob(promedio):
        print (f'Felicidades, aprobaste la materia {promedio}')
   
    else:
        print('no aprobaste')

mensaje(promedio, aprobado, 5,5,7,8,7)