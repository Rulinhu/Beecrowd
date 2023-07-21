quant = int(input())

val_co = 0
val_ra = 0
val_sap = 0
numcob = 0
cobaias = [0 for i in range(quant + 1)]
val = [0 for i in range(quant + 1)]
tipo = [0 for i in range(quant + 1)]

for i in range(0, quant):
    cobaias[i] = input()
    val[i] = int(cobaias[i][:-2])
    tipo[i] = cobaias[i][-1:]

    numcob += val[i]

    if tipo[i] == "C":
        val_co += val[i]
    elif tipo[i] == "R":
        val_ra += val[i]
    else:
        val_sap += val[i]

print("Total: %d cobaias" %numcob)
print("Total de coelhos: %d" %val_co)
print("Total de ratos: %d" %val_ra)
print("Total de sapos: %d" %val_sap)
print("Percentual de coelhos: %0.2f %%" %(val_co * 100 / numcob))
print("Percentual de ratos: %0.2f %%" %(val_ra * 100 / numcob))
print("Percentual de sapos: %0.2f %%" %(val_sap * 100 / numcob))