print ("\nSeja bem-vindo ao sistema de medias escolar automático!\n")
nota1=float(input("Escreva sua primeira nota:"))
nota2=float(input("Escreva sua segunda nota:"))
nota3=float(input("Escreva sua terceira nota:"))
nota4=float(input("Escreva sua quarta nota:"))
peso1=10
#Inicio do calculo ponderado:
MediaP1,MediaP2,MediaP3=(nota1 * 2),(nota2 * 3),(nota3 * 5)
soma1=(MediaP1 + MediaP2 + MediaP3)
Resultado_MediaP=(soma1 / peso1)

#Inicio da media final:
MediaF=(nota1 + nota2 + nota3+ nota4)/4
print(f"\nA sua media final é : {MediaF} \n")
#Media ponderada:
print("A sua nota ponderada : ",Resultado_MediaP)

#A partir daqui,são valores logicos que atribuiram uma resposta para cada critério na media ponderada

if (Resultado_MediaP>=8 and Resultado_MediaP<=10):
    print("\nParabéns você tirou nota A")
elif (Resultado_MediaP>=7 and Resultado_MediaP<8):
    print("\nParabéns você tirou nota B")
elif (Resultado_MediaP>=6 and Resultado_MediaP<7):
    print("\nVocê tirou nota C")
elif (Resultado_MediaP>=5 and Resultado_MediaP<6):
    print("\nVocê tirou nota D")
elif (Resultado_MediaP<5 and Resultado_MediaP>=0):
    print("\nInfelizmente você tirou nota E\n")
else:
    (print("\nErro:Valor inválido!"))