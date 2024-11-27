from datetime import datetime

while True:
    try:
        nome = str(input("Digite o seu nome: "))
        ano_nascimento = int(input("Digite o seu ano de nascimento: "))
        idade = datetime.now().year - ano_nascimento
        idade_faltante = 18 - idade
        idade_sobrando = idade - 18

        if idade == 18:
            print(f"Parabéns {nome}, está na hora de você se alistar!")
            break
        elif idade < 18:
            print(f"Olá {nome}, você ainda não possui idade suficiente para se alistar, espere mais {idade_faltante} anos para se alistar.")
            break
        elif idade > 18:
            print(f"Olá {nome}, já passou {idade_sobrando} anos do seu tempo de alistamento.")
            break

    except ValueError:
        print("Digite os dados corretamente.")

