#Ler 3 valores e calcular uma equação do 2º grau com bhaskara e delta, onde os valores são diferentes de 0.

#Explicação variáveis
# a,b,c= valores 
# delta= formula de delta
# x1= formula de bhaskara positiva
# x2= formula de bhaskara negativa

a=int(input("Digite o valor de a:"))
b=int(input("Digite o valor de b:"))
c=int(input("Digite o valor de a:"))

delta= (b**2)-4*a*c

x1=(-b + (delta**0.5))/2*a
x2=(-b - (delta**0.5))/2*a

if a!=0 and b!=0 and c!=0:          #condição que a, b e c devem seguir
     #condições para o valor de delta 
    if delta>0:                     
        print("O delta é positivo, assim, os valores das raízes são:", x1, x2)
    if delta==0:
        print("O delta é 0, assim, seu valor de suas raízes são iguais:", x1,x2)
    if delta<0:
        print("Não existe raíz real quando o valor do delta é negativo.")
else: 
    print("Algum desses valores não satisfazem as condições para a resolução de uma equação do 2º grau com a formula de Bhaskara e Delta.")