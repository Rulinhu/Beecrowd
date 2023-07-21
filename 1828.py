n = int(input())

Jogo = {
    "la" : ["pe", "te"],
    "pa" : ["te", "la"],
    "te" : ["pe", "Sp"],
    "pe" : ["pa", "Sp"],
    "Sp" : ["pa", "la"],
}

def desenrolar(jogada):
    i = 0

    if jogada[0:2] == jogada[jogada.index(" ") + 1 : jogada.index(" ") + 3]:
        return "De novo!"
    else:
        while i < 2:
            if Jogo[jogada[jogada.index(" ") + 1 : jogada.index(" ") + 3]][i] == jogada[0:2]:
                return "Bazinga!"
            i+=1
        return "Raj trapaceou!"

for num in range(1, n + 1):
    jogada = input()

    print("Caso #" + str(num) + ": " + desenrolar(jogada))

    n-=1