num = int(input())
eba = ["A", "Q", "J", "K"]

for i in range(num):
    cartas = input()

    for j in range(len(cartas)):
        for m in eba:
            if m in cartas[j]:
                eba.remove(m)

    if bool(eba) == False:
        print("Aaah muleke")
    else:
        print("Ooo raca viu")

    eba = ["A", "Q", "J", "K"]