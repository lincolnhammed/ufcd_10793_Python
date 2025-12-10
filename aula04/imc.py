# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (peso / (altura * altura)) 
# e mostre seu status, de acordo com a tabela abaixo:
# o	IMC abaixo de 16: baixo peso severo
# o	Entre 16 e 17: baixo peso
# o	18 até 25: Peso ideal
# o	30 até 40: Pré-Obesidade
# o	Acima De 40: Obesidade Alta

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
if imc < 16:
    print("Status: Baixo peso severo")
elif 16 <= imc < 18:
    print("Status: Baixo peso")
elif 18 <= imc < 25:
    print("Status: Peso ideal")
elif 25 <= imc < 30:
    print("Status: Pré-Obesidade")
elif 30 <= imc < 40:
    print("Status: Obesidade")
else:
    print("Status: Obesidade Alta")
print("")
