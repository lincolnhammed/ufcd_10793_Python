#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 9.4: REPROVADO
#Média entre 9.5 e 11.9: RECUPERAÇÃO
#Média 12.0 ou superior: APROVADO

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media < 9.5:
    print("REPROVADO")
elif 9.5 <= media <= 11.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
print(f"Sua média é {media:.2f}")
