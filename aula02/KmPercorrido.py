# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi 
# alugado. Calcule o preço a pagar, sabendo que o carro custa 60€ 
# por dia e 0.15€ por Km rodado.

diaria = int(input("Quantidade de dias: "))
qtdKm = float(input("Quantidade de km percorridos: "))

precoDiaria = diaria * 60
precoQtdKm = qtdKm * 0.15

print(f"O preço da diária é: {precoDiaria}€")
print(f"O preço por km percorrido é: {precoQtdKm}€")
print(f"O preço total a pagar é: {precoDiaria + precoQtdKm:.2f}€")

