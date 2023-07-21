carac1 = input()
carac2 = input()
carac3 = input()

if carac1 == "vertebrado":
    if carac2 == "ave":
        if carac3 == "carnivoro":
            resposta = "aguia"
        else:
            resposta = "pomba"
    else:
        if carac3 == "onivoro":
            resposta = "homem"
        else:
            resposta = "vaca"
else:
    if carac2 == "inseto":
        if carac3 == "hematofago":
            resposta = "pulga"
        else:
            resposta = "lagarta"
    else:
        if carac3 == "hematofago":
            resposta = "sanguessuga"
        else:
            resposta = "minhoca"

print(resposta)