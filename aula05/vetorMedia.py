#Crie um programa que leia 4 notas, mostre as notas e a média no ecrã.
 

notas=[]
media=0
cont=0
for i in range(0,4,1):
    notas.append(float(input(f"digite a primeira nota{i+1}°: ")))
    media+=notas[i]


for i in notas:
    cont+=1;
    print(f"{cont}° nota é: {i}")
print(f"a media do aluno foi{media/len(notas)}")