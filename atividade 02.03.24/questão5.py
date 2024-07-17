#Ler 4 valores inteiros e apresentar aqueles que são divisiveis por 2 e 3

#Explicação variáveis:
# v1 a v4= valores inteiros

v1=int(input("Digite um valor:"))
v2=int(input("Digite um valor:"))
v3=int(input("Digite um valor:"))
v4=int(input("Digite um valor:"))

if v1%2==0 and v1%3==0:           #condição para cada valor
    
    if v2%2==0 and v2%3==0:
        
        if v3%2==0 and v3%3==0:
            
            if v4%2==0 and v4%3==0:
                
                print("Esses números são divisíveis por 2 e 3.")
else:
    print("Esses números não são divisiveis por 2 e 3.")