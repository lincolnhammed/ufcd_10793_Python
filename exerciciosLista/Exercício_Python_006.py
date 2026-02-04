

"""
Docstring for exerciciosLista.Exercício_Python_006


A Organização XPTO decidiu atribuir aos seus colaboradores um bónus em
reconhecimento dos bons resultados obtidos durante o ano transato. Para tal,
contratou-o para desenvolver uma aplicação que sirva de projeção do montante que
será destinado ao pagamento deste bónus.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e representantes
sindicais, chegou-se à seguinte forma de cálculo:
a. Cada funcionário receberá o equivalente a 20% do seu salário bruto de
dezembro;
b. O piso do abono será de 100 euros, ou seja, aqueles funcionários cujo
salário é muito baixo receberão este valor mínimo;
Neste momento, não se deve preocupar com funcionários com menos tempo de
trabalho, descontos, impostos ou outras particularidades. Seu programa deve permitir 
que você insira o salário para um número indefinido (desconhecido) de salários. Um
valor de salário de 0 (zero) encerra a entrada. Depois de introduzidos todos os dados, o
programa deve calcular o valor da retribuição atribuída a cada trabalhador, de acordo
com a regra definida anteriormente. No final, o programa deve exibir:
✓ O salário de cada empregado, juntamente com o montante da
indemnização;
✓ O número total de empregados processados;
✓ O valor total a ser utilizado para o pagamento do abono;
✓ O número de funcionários que receberão o valor mínimo de 100 reais;
✓ O valor máximo pago a título de abono; A tela a seguir é um exemplo de
execução do programa, apenas para fins ilustrativos. Os valores podem ser
alterados a cada execução do programa.
"""

salarios = []
bonus = []


while True:
    salario = float(input("Introduza o salário (0 para terminar): "))

    if salario == 0:
        break

    salarios.append(salario)


for salario in salarios:
    valor_bonus = salario * 0.20

    if valor_bonus < 100:
        valor_bonus = 100

    bonus.append(valor_bonus)


total_bonus = 0
minimos = 0
maior_bonus = 0

print("\nSalário | Bónus")
print("----------------")

for i in range(len(salarios)):
    print(f"{salarios[i]:.2f} € | {bonus[i]:.2f} €")

    total_bonus += bonus[i]

    if bonus[i] == 100:
        minimos += 1

    if bonus[i] > maior_bonus:
        maior_bonus = bonus[i]

print("\nResumo final")
print("------------")
print(f"Total de empregados: {len(salarios)}")
print(f"Total gasto em bónus: {total_bonus:.2f} €")
print(f"Funcionários com bónus mínimo: {minimos}")
print(f"Maior bónus pago: {maior_bonus:.2f} €")
