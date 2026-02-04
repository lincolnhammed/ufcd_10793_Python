"""
Docstring for exerciciosLista.Exercício_Python_002

Desenvolva um programa que leia quatro valores pelo teclado e guarde-os numa
lista. No final, mostre:
o Quantas vezes apareceu o valor 9.
o Em que posição foi digitado o primeiro valor 3.
o Quais foram os números pares.

"""
cont=0
primeiraPosicao=0
vet=[]
par=[]
print("Escreva um numero no vetor\n")
for i in range(4):
    
    num=(int(input(f"vetor[{i}]")))
    vet.append(num)

for i in range(len(vet)):
    
    if(vet[i]==9):
        cont+=1
    if(vet[i]%2==0):
        par.append(vet[i])
       

for i in range(len(vet)):
    if(vet[i]==3):
        primeiraPosicao= i
        break


print(f"O numero 9 aparece - {cont} vezes")
print(f"os numeros pares - {par}")
print(f"A primeira posicao do numero 3 é - {primeiraPosicao}")
