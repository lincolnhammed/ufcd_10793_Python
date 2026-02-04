"""
Docstring for exerciciosLista.Exercício_Python_005

Faça um programa que leia um número qualquer de valores, correspondentes anotas, 
terminando a entrada de dados quando for introduzido um valor igual a -1 (que não deve ser guardado). 
Após esta entrada de dados, faça o seguinte o Exibir o número de valores que foram lidos;

* Mostrar todos os valores pela ordem em que foram introduzidos, lado a lado;
* Mostrar todos os valores na ordem inversa em que foram introduzidos,um por baixo do outro;
* Calcular e apresentar a soma dos valores;
* Calcular e apresentar a média dos valores;
* Calcular e mostrar o número de valores acima da média calculada;
* Calcular e mostrar o número de valores abaixo de sete;
* Fechar o programa com uma mensagem;

"""
notas=[]

nLidos=0

while True:
    num = float(input(f"digite {nLidos+1}° nota"))
    if (num ==-1):
        break
    
    notas.append(num)   
    nLidos+=1
    
if len(notas) > 0:
    print(f"Total numeros lidos: {nLidos}")
    print(f"ordem em que foram introduzidos, lado a lado:\n {notas}")
    naoSei=len(notas)-1
    soma=0
    print(f"ordem inversa em que foram introduzidos,um por baixo do outro:")
    for i in range(len(notas)):
        print(f"{notas[naoSei]}")
        soma += notas[naoSei]
        naoSei-=1
    media=soma/len(notas)
    print(f"Soma dos valores:{soma}")   
    print(f"Média dos valores:{media}")   

    acima_media=0
    for i in notas:
        if(i>media):
         acima_media+=1
    print(f"número de valores acima da média calculada: {acima_media}")  
    abaixo_sete=0    
    for i in notas:
        if(i<7):
         abaixo_sete+=1 
    print(f"número de valores abaixo de sete: {abaixo_sete}")   
else:
    print("Nenhuma nota foi informada.")
print("FIM")