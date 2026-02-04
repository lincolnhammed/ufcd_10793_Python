# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
maioridade = 0
menoridade = 0
for i in range(7):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i+1}ª pessoa: "))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print(f"Total de pessoas maiores de idade: {maioridade}")
print(f"Total de pessoas menores de idade: {menoridade}")
