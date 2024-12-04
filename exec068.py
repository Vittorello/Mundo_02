mais18 = 0
homens = 0
menos20 = 0

while True:    
    print("=-=" * 10)
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()
    while sexo not in ['M', 'F']:
        sexo = input("Entrada inválida. Sexo [M/F]: ").strip().upper()
    
    if idade > 18:
        mais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        menos20 += 1
    
    escolha = input("Você quer continuar? [Sim/Não]: ").strip().upper()
    while escolha not in ['SIM', 'NAO']:
        escolha = input("Entrada inválida. Você quer continuar? [Sim/Não]: ").strip().upper()
    
    if escolha == 'NAO':
        break

print("\nResumo do levantamento:")
print(f"Total de pessoas com mais de 18 anos: {mais18}")
print(f"Total de homens cadastrados: {homens}")
print(f"Total de mulheres com menos de 20 anos: {menos20}")
