gas = 0
diesel = 0
gasolina = 0
alcool = 0

while gas != 4:
    gas = int(input())

    if gas == 1:
        alcool += 1
    elif gas == 2:
        gasolina += 1
    elif gas == 3:
        diesel += 1

print("MUITO OBRIGADO")
print("Alcool: %d" %alcool)
print("Gasolina: %d" %gasolina)
print("Diesel: %d" %diesel)