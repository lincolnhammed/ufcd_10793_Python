# Crie um programa que leia 20 números inteiros
# e os armazene num vetor. Armazene os números
# pares no vetor PAR e os números ímpares no vetor ÍMPAR.
# Imprima os três vetores.
num=0;
numPar=[];
numImpar=[];
num1=[];
for i in range(0,4,1):
    
    num1.append(int(input(f"digite a primeira numero{i+1}°: ")))

    if(num1[i]%2==0):
        numPar.append(num1[i]);
    else:
        numImpar.append(num1[i]);



for i in num1:
    print(f"vetor{i+1}: {i}")
print(f"vetor par: {numPar}")
print(f"vetor impar: {numImpar}")