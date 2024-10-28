gryffindor = 0
Hufflepuff = 0
Ravenclaw = 0
Slytherin = 0

print('===============')
print('The Sorting Hat')
print('===============')

#PREGUNTA 1

print("Q1) ¿Te gusta el amanecer o el anochecer?")    
print(" 1) amanecer")
print(" 2) Anochecer")


answer = int(input("Cual es tu respuesta?:"))

if answer == 1:
    Gryffindor = +1
    Ravenclaw = +1
elif answer ==2:
    Hufflepuff = +1
    Slytherin = +1
else:
    print("Entrada incorrecta")
    
    
#PREGUNTA 2


print("Q2) Cuando esté muerto, quiero que la gente me recuerde como:")
print(" 1) El Bien")
print(" 2) El Grande")
print(" 3) Los sabios")
print(" 4) El audaz")

answer = int(input("Cual es tu respuesta?:"))

if answer == 1:
    Hufflepuff = +1
elif answer ==2:
    Slytherin = +2
elif answer == 3:
        Ravenclaw = +2    
elif answer == 4:
        Gryffindor = +2
else:
    print("Entrada incorrecta")
        

#PREGUNTA 3

print("P3) ¿Qué tipo de instrumento le agrada más al oído?")
print(' 1) el violín')
print(' 2) la trompeta')
print(' 3) el piano')
print(' 4) El tambor')
answer = int(input("Cual es tu respuesta?:"))

if answer == 1:
    Slytherin = +4
elif answer ==2:
     Hufflepuff = +4
elif answer == 3:
        Ravenclaw = +4  
elif answer == 4:
        Gryffindor = +4
else:
    print("Entrada incorrecta")

print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)

most_point = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)

if Gryffindor == most_point:
      print('🦁 Gryffindor!')
elif Ravenclaw == most_point:
 print('🦅 Ravenclaw!')
elif Hufflepuff == most_point:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')