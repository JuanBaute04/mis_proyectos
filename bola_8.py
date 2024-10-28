import random
question = input("Cual es tu pregunta?:")
random_number =random.randint(1,9)
if random_number == 1:
              answer = "En este momento no lo se, quiza despues lo sepa"
elif random_number == 2:
              answer = "Creo que es una idea increible"
      
elif random_number == 3:
              answer = "Deberias intentarlo"
              
      
elif random_number == 4:
              answer = "Es lo mejor que podrias hacer en tu vida"
              
elif random_number == 5:
              answer = "Puede que en este momento no sea lo mejor"
              
      
elif random_number == 6:
              answer = "Ahora mismo no"
elif random_number == 7:
              answer = "Quiza es lo mejor, hazlo"
elif random_number == 8:
              answer = "Completamente si"
          
elif random_number == 9:
              answer = "Completamente no"
else:
    answer ="ERROR"      

print(f"La bola magica dice:{answer}")                         
                            
                                                                      
              
              