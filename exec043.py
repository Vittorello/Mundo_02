nome = str(input("Digite o seu nome: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Olá {nome}, de acordo com seu IMC '{imc:.2f}' você está abaixo do peso.")
elif imc >= 18.5 and imc <= 25:
    print(f"Olá {nome}, de acordo com seu IMC '{imc:.2f}' você está no peso ideial.")
elif imc > 25 and imc <= 30:
    print(f"Olá {nome}, de acordo com seu IMC '{imc:.2f}' você está com sobrepeso.")
elif imc > 30 and imc <= 40:
    print(f"Olá {nome}, de acordo com seu IMC '{imc:.2f}' você está com obesidade.")
elif imc > 40:
    print(f"Olá {nome}, de acordo com seu IMC '{imc:.2f}' você está com obesidade mórbida.")
