from random import choice
from time import sleep

palpite = 0
tentativas = 0

print("Bem-vindo ao jogo de adivinhação!")
print("Estou pensando em um número entre 1 e 10. Você tem apenas 10 tentativas para descobrir. Boa sorte!\n")

while tentativas < 10:
    try:
        valor = int(input("Qual é o seu palpite? "))
        print("Deixe-me verificar se você acertou...")
        num = range(1, 11)
        numero = choice(num)
        sleep(1)
        
        if valor != numero:
            tentativas += 1
            palpite += 1
            if tentativas < 10:
                print(f"Que pena! O número era {numero}. Você ainda tem {10 - tentativas} tentativas. Tente novamente!\n")
            else:
                print(f"Acabaram suas tentativas! O número era {numero}. Você fez {palpite} palpites. Não desista, jogue novamente!\n")
        else:
            print(f"🎉 Uau! Você acertou! O número era {numero}. Foram necessários {palpite + 1} palpites para vencer. Parabéns! 🎉")
            break
    except ValueError:
        print("⚠️ Ops! Você deve digitar um número válido. Tente novamente.\n")
else:
    print("Fim do jogo! Espero que tenha se divertido. Até a próxima!")
