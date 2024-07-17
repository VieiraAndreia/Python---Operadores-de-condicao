#Teste para identificar um triangulo e seu tipo com 3 valores distintos.

#OBS: Nesse código há 3 diagramas de blocos, que resultam na análise da formação de um triangulo.

#Introdução dos valores a serem testados.
a=int(input("Valor do 1º lado do triangulo:"))
b=int(input("Valor do 2º lado do triangulo:"))
c=int(input("Valor do 3º lado do triangulo:"))

#Condições para que esses valores formem um triangulo
if a<b+c and b<a+c and c<a+b:                                                       #1º bloco
    
    if a==b and b==c:                                                               #2º blobo
        print("Todos os lados são iguais, ou seja, um triangulo equilatero.")
    if a==b or a==c or c==b:                                                        #3º bloco
        print("Dois desses valores são iguais, ou seja, formam um triangulo isosceles.")
    else:
        print("Todos esses valores são diferentes, ou seja, formam um triangulo escaleno.")
else:                                                                                #falsidade do 1º bloco
    print("Esses valores não formam um triangulo.")