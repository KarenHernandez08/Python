resultado = 10

if resultado > 10 and resultado < 20:
    print("la variable cumple con la condición")
else:
    print("la variable no cumple con la condición :(")


    #Multiples condiciones 
calificaciones = 5

if calificaciones == 10:
    print("Felicidades aprobaste")
elif calificaciones==9 or calificaciones ==8:
    print("Aprobaste la materia")
elif calificaciones ==7 or calificaciones ==6:
    print ("Aprobaste")

else:
    print("lo siento, estas reprobado")



#Ternario

calificacion =5
color = "verde" if calificacion >=7 else "rojo"

print(calificacion,color)

