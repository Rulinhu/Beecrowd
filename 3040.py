q = int(input())

for i in range(q):
    tam, esp, gal = map(int ,input().split())

    if tam < 200 or tam > 300 or esp < 50 or gal < 150:
        print("Nao")
    else:
        print("Sim")