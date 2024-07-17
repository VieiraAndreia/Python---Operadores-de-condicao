#Ler 3 valores e apresentar em ordem crescente

#explicação variáveis:
# v1 a v3= valores
#ordem= como deve ser a organização em ordem crescente

v1=float(input("Digite um valor:"))
v2=float(input("Digite um valor:"))
v3=float(input("Digite um valor:"))

if v1>v2:
    v1,v2= v2,v1
if v1>v3:
    v1,v3=v3,v1
if v2>v3:
    v2,v3= v3,v2
    
print("A ordem crescente desses numeros é:", v1,v2,v3)