# Faça um programa que leia um vetor de 10 caracteres
# e lhe diga quantas consoantes foram lidas. Imprime as consoantes.

vogais = "AEIOU"
consoantes = []

frase = input("Digite uma frase (máx. 10 caracteres): ").upper()

if len(frase) > 10:
    print("A frase tem mais de 10 caracteres.")
else:
    for i in range(len(frase)):
        if frase[i].isalpha() and frase[i] not in vogais:
            consoantes.append(frase[i])

    print(f"\nConsoantes encontradas: {consoantes}")
    print(f"Total de consoantes: {len(consoantes)}")
