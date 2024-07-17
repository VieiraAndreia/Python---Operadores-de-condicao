salário:float(input("Digite o valor do salário:"))
if salário<500:
    salário=salário+1.15
else:
    if salário<=1000:
       salário=salário+1.18
    else:
        salário=salário+1.05

print("O salário é:", salário)