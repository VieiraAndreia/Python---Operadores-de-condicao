#Ler quatro notas escolares, calcular a média aritmética e apresentar a aprovação (ma >=7)ou reprovação junto ao valor da média.

#explicação variáveis:
# n1 a n4= notas
# ma= média aritmética

n1=float(input("Digite o valor da 1º nota:"))
n2=float(input("Digite o valor da 2º nota:"))
n3=float(input("Digite o valor da 3º nota:"))
n4=float(input("Digite o valor da 4º nota:"))
ma=(n1+n2+n3+n4)/4

if ma>=7:
    print("Aluno(a) aprovado! Sua média foi:",ma)
else: print("Aluno(a) reprovado! Sua média foi:", ma)