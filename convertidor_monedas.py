pesos = int(input("Ingrese la cantidad de pesos que desea convertir:"))
soles = int(input("Ingrese la cantidad de soles que desea convertir:"))
reales =int(input("Ingrese la cantidad de reales que desea convertir:"))

dolar_peso = pesos / 4150 #Precio de un dolar
dolar_reales = reales / 5.45 #Precio de un dolar
dolar_soles= soles / 3.74

total = dolar_peso + dolar_reales + dolar_soles

print(f"El total de dolares al cambio es de:{total}")
