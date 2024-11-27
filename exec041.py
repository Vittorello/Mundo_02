from datetime import datetime

ano_nascimento = int(input("Digite o ano do seu nascimento: "))
idade = datetime.now().year - ano_nascimento

if idade <= 9:
    print("MIRIM")
elif idade > 9 and idade <= 14:
    print("INFANTIL")
elif idade > 14 and idade <= 19:
    print("JUNIOR")
elif idade > 19 and idade <= 20:
    print("SÊNIOR")
elif idade > 20:
    print("MASTER")
