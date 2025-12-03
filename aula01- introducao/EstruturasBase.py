#variavel nao presisa ser declarada
num=0;

# maneira de imprimir no python
print(f"Helo Word\n{num}");

# Solicita ao usuário que digite sua idade
idade =int (input("Digite sua idade: "));

# estrutura condicional if, elif, else
x = 10
if x > 5:
    print("Maior que 5")
elif x == 5: 
    print("Igual a 5")
else:
    print("Menor que 5")


# estrutura condicional match case (disponível a partir do Python 3.10)
opcao = 2
match opcao:
    case 1:
        print("Um")
    case 2:
        print("Dois")
    case 3:
        print("Três")
    case _:
        print("Outra coisa")


# estrutura de repetição while
i = 0

while i < 5:
    print(i)
    i += 1

# estrutura de repetição for
numero =5
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# estrutura de vetor
numeros = [10, 20, 30]

print(numeros[0])  # 10
numeros.append(40)