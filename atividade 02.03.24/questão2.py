#Ler 4 notas e calcular a média aritmetica, caso o resultado seja >=7 é aprovado, caso contrário deve ser solicitado a nota no Exame final e calcular uma nova média aritmética.

#explicação variáveis: 
# n1 a n4= notas
# ma= media aritmetica
# n5= nota do exame final
# mf= nova media aritmetica

n1=float(input("Digite o valor da 1º nota:"))
n2=float(input("Digite o valor da 2º nota:"))
n3=float(input("Digite o valor da 3º nota:"))
n4=float(input("Digite o valor da 4º nota:"))
ma=(n1+n2+n3+n4)/4

if ma>=7:                                                      #1º bloco
    print("Aluno(a) aprovado! Sua média foi:",ma)
else: 
    print("Aluno(a) reprovado! Sua média foi:", ma)
    n5=float(input("Digite o valor da nota do Exame Final:"))
    mf=(ma+n5)/2
    
    if mf>=5:                                                   #2º bloco
        print("Aluno(a) aprovado! Sua média foi:", mf)
    else:
        print("Aluno(a) reprovado! Sua média foi:", mf)