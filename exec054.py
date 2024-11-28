from datetime import datetime

ano_atual = datetime.now().year
totmaior = 0
totmenor = 0

for pessoas in range(1,8):
    nasc = int(input("Digite sua data de nascimento: "))
    idade = ano_atual - nasc
    if idade >= 21:
        totmaior += 1
    elif idade < 21:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade')
