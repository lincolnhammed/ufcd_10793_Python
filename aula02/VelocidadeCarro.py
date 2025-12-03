# Escrever um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo 
# que ele foi multado. A multa vai custar 7,00€ por cada 
# Km acima do limite.

velocidade = int(input("Velocidade (Km/h): "))

limite = 80
valor_multa = 7

if velocidade > limite:
    excesso = velocidade - limite
    multa = excesso * valor_multa
    print(f"Multa: {multa:.2f}€ (Excesso de {excesso} Km/h)")
else:
    print("Sem multa.")
