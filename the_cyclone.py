heigth = int(input("Cual es tu altura:"))
credit = int(input("Cual es tu cantidad de creditos:"))

#La altura minima es de 155
#Los creditos necesarios son 10
#Aca el algoritmo

if heigth >= 155 and credit >= 10:
    print("Disfruta tu viaje!!!!")
elif heigth < 155 and credit >= 10:
    print("No cumples con el minimo de altura") 
elif heigth >= 155 and credit < 10:
    print("No tienes los creditos suficientes para subirte")
else:
    print("No cumples con los resquisitos")


    
    
    
    
    