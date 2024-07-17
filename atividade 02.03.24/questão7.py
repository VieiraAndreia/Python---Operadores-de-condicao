#Ler nome e sexo de uma pessoa e apresentar em cada  mensagens "Sr. ou Sra." junto ao seu nome.

#Explicação variáveis:
#n=nome
#s=sexo

n=input("Digite seu nome:")
s=input("Digite seu sexo (feminino ou masculino):")

if s=="feminino":                #caso a resposta de "s" seja feminino
    print("Olá Sra.", n)
else:
    print("Olá Sr.", n)