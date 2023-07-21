def triangle(meio, menor, maior1, maior2):
    for x, y, z in [(menor, meio, maior2), (meio, maior2, maior1)]:
        if x + y > z:
            return "S"
    return "N"

numeros = list(map(int, input().split(" ")))

maior1 = max(numeros)
numeros.remove(maior1)
maior2 = max(numeros)
numeros.remove(maior2)
menor = min(numeros)
numeros.remove(menor)

print(triangle(int(''.join(map(str, numeros))), menor, maior1, maior2))