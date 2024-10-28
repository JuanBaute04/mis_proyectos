print("BANK OF CODEDEX")

pin = int(input("Enter your pin:"))

while pin != 1234:
    pin = int(input("Incorrect pin. Enter pin again:"))
    
    if pin == 1234:
        print('PIN Accepted')