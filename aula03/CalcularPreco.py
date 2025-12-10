# Desenvolva um programa que pergunte a distância 
# de uma viagem em Km. Calcule o preço do bilhete, 
# cobrando 0,50€ por Km para viagens até 200Km e 
# 0,45€ parta viagens mais longas.


KmPercorrido = int(input("qual distancia a ser percorrida"))

if(KmPercorrido <0):
    print("O valor da distancia é invalida")
else:
    if(KmPercorrido <=200):
        calculo = 0.50* KmPercorrido
    else:
     calculo = 0.45*KmPercorrido
print(f"o preço a ser pago é {calculo:2f}$")
