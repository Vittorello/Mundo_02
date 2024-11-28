soma_idade = 0
media_idade = 0
mulher20 = 0
nomevelho = ""
idadevelho = 0
for c in range(1,5):
    print(f'----- {c} PESSOA -----')
    nome = str(input(f"Nome: ")).strip().capitalize()
    idade = int(input(f"Idade: "))
    sexo = str(input(f"Sexo [M/F]: ")).upper()
    soma_idade += idade
    if c == 1 and sexo == 'M':
        nomevelho = nome
        idadevelho = idade 
    if sexo == 'M' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulher20 += 1
media_idade = soma_idade / 4
print(f'''O total de mulheres com menos de 20 anos é {mulher20}
{nomevelho} é o homem mais velho e tem {idadevelho} anos.
De acordo com as {c} idades, a média de idade é {media_idade}''')