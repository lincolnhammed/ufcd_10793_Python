#Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai dar o nome para o serviço militar, 
# se é o ano exata de dar o nome ou se já passou do tempo do alistamento. 
# O programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = date.today().year
idade = anoAtual - anoNascimento    
if idade < 18:
    print(f"Ainda faltam {18 - idade} anos para o alistamento.")
elif idade == 18:
    print("Você deve se alistar este ano.")
else:
    print(f"Você já deveria ter se alistado há {idade - 18} anos.") 
print("")

 